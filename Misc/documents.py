from docx import Document
document = Document("C:\\Users\\My  PC\\Documents\\Kashmiri docs\\Corpus295.docx")
fulltext=[]
for para in document.paragraphs:
    print(para.text)
    fulltext.append(para.text)
    print("\n")
    print("".join(fulltext).replace(" ",","))
    thefile = open('test7.csv', 'w',encoding='utf8')
    for item in fulltext:
        thefile.write("%s\n" % item.replace(" ","'\n,'"))
    thefile.close()

