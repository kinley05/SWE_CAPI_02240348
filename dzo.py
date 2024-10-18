import docx2txt as d2t

docxfile="dictionary.docx"
txtfile="dictionary.txt"

doc=d2t.process(docxfile)

file=open(txtfile, 'w', encoding='utf-8')
file.write(doc)
file.close()

print('file converted')