import pickle
import pandas as pd
import keras
from keras.layers import LeakyReLU
from keras.utils import plot_model
from sklearn.metrics import  confusion_matrix
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D,MaxPooling2D
from keras.utils import to_categorical
import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
#from Train_data_generator import *
from Test_data_generator import *
import itertools
from  sklearn.preprocessing import MinMaxScaler
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with open('Features_Dataset_trimmed_mfcc_200_Samples.obj', 'rb') as f:
    object_file = pickle.load(f)

    # converting lists to pandas data frame buffer
    df = pd.DataFrame(object_file, columns=['label', 'data'])
    x_data = df['data']
    y_label = df['label']
    print(df)
    X = []
    for x in x_data:
        X.append(x[0])

X = np.array(X)
X = pad_sequences(X)
y_label = np.array(y_label)
y_label = to_categorical(y_label)
print(X.shape)
print(y_label.shape)
X_data = X.reshape(X.shape[0],X.shape[1],X.shape[2],1)
print(X_data.shape)

# reshape into X=t and Y=t+1
X_train, X_test, y_train, y_test = train_test_split(X_data, y_label, test_size=0.2, shuffle=True)
'''
Xtrain, Ytrain = next(Train_gen())
Xtest, Ytest = next(Test_gen())
'''
verbose, batch_size = 1, 32
n_timesteps, n_features, n_outputs = 3001, 13,201
#y_train = y_train.reshape(y_train.shape[0],y_train.shape[1],y_train.shape[2],1)

#epochlist=[15,20]
#activationfunctionlist=["relu","sigmoid"]
#optimizerlist=["adam","sgd","adadelta","adagradew"]

epochlist=[15]
activationfunctionlist=["relu"]
optimizerlist=["sgd"]

plt.ioff()
resultfile=open("Speech_Reecognition_Results.csv","w")
resultfile.write("Activation,Epochs,Optimizer,Training_Accuracy,Training_Loss,Val_Accuracy,Val_Loss,Test_Accuracy,Test_Loss\n")

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion Matrix',
                          cmap =plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def createModel(activation_function):
    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=3, strides=1, padding='same', activation=activation_function,input_shape=(n_timesteps, n_features,1)))
    model.add(MaxPooling2D(pool_size=2, padding='same'))

    model.add(Conv2D(filters=32, kernel_size=3, strides=1, padding='same', activation=activation_function))
    model.add(MaxPooling2D(pool_size=2, padding='same'))

    model.add(Conv2D(filters=32, kernel_size=3, strides=1, padding='same', activation=activation_function))
    model.add(MaxPooling2D(pool_size=2,padding='same'))
    #model.add(LeakyReLU(alpha=0.1))

    model.add(Conv2D(filters=64, kernel_size=3, strides=1,padding='same', activation=activation_function))
    model.add(MaxPooling2D(pool_size=2,padding='same'))

    model.add(Conv2D(filters=64, kernel_size=3, strides=1,padding='same', activation=activation_function))
    model.add(MaxPooling2D(pool_size=2,padding='same'))

    model.add(Flatten())
    model.add(Dense(2000))
    model.add(Dropout(0.2))
    model.add(Dense(1000))
    model.add(Dropout(0.2))
    model.add(Dense(2000))
    model.add(Dropout(0.2))
    model.add(Dense(n_outputs, activation='softmax'))

    return model


for epochs in epochlist:

    for optimizer in optimizerlist:

        for activationfunction in activationfunctionlist:

            resultrow = str(activationfunction) + "," + str(epochs) + "," + str(optimizer) + ","
            # define model
            model = createModel(activationfunction)
            batch_size = 32
            model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

            model.summary()

            history = model.fit(X_train,y_train, batch_size=batch_size, epochs=epochs, verbose=1,
                                validation_data=(X_test,y_test))

            #             Saving Models and its weights
            #filename='finalize_model.sav'
            #pickle.dump(model,(filename,'wb'))

            # Serialize model to json
            model_json = model.to_json()
            with open("model.json","w") as json_file:
                json_file.write(model_json)

            #   serialize weights to HDF5
            model.save_weights("model.h5")
            print("Saved model to disk")

            # model.save(activationfunction + "_" + str(epochs) +"_" + optimizer + ".json")
            # model.save_weights(activationfunction + "_" + str(epochs) +"_" + optimizer + ".h5")

            print(history.history.keys())

            # summarize history for accuracy
            # plt.subplots(nrows=1,ncols=2)
            plt.plot(history.history['acc'])
            plt.plot(history.history['val_acc'])
            plt.title('Model Accuracy')
            plt.ylabel('accuracy')
            plt.xlabel('epoch')
            plt.legend(['train', 'val'], loc='upper left')
            #plt.show()
            plt.savefig("TrAcc_ValAcc_" + str(activationfunction) + "_" + str(epochs) + "_" + str(optimizer))
            plt.close()
            # summarize history for loss

            resultrow = resultrow + str(np.mean(history.history["acc"])) + ","
            resultrow = resultrow + str(np.mean(history.history["loss"])) + ","
            resultrow = resultrow + str(np.mean(history.history["val_acc"])) + ","
            resultrow = resultrow + str(np.mean(history.history["val_loss"])) + ","

            plt.plot(history.history['loss'])
            plt.plot(history.history['val_loss'])
            plt.title('Model Loss')
            plt.ylabel('loss')
            plt.xlabel('epoch')
            plt.legend(['train', 'val'], loc='upper left')
            #plt.show()
            plt.savefig("TrLoss_ValLoss_" + str(activationfunction) + "_" + str(epochs) + "_" + str(optimizer))
            plt.close()
            print("\n===============Evaluating Model===========\n")
            loss, accuracy = model.evaluate(X_test, y_test, verbose=1)

            resultrow = resultrow + str(accuracy) + ","
            resultrow = resultrow + str(loss) + ","
            print(model.metrics_names)
            print('Accuracy: %f' % (accuracy * 100))
            print('Loss: %f' % loss)
            plot_model(model, to_file='Speech_Model.png')
            classes = np.unique(y_train)
            y_test_pred = model.predict_classes(X_test)
            print(y_test_pred)
            cnf_matrix = confusion_matrix(y_test.argmax(axis=1), y_test_pred)
            plt.figure()
            plot_confusion_matrix(cnf_matrix, classes=classes,title='Confusion Matrix')
            #plt.show()
            plt.savefig("ConfusionMatrix " + str(activationfunction) + "_" + str(epochs) + "_" + str(optimizer))
            plt.close()
            resultrow = resultrow + ",\n"
            resultfile.write(resultrow)
            resultrow = ""
resultfile.close()
