from pdf2docx import Converter
pdf_file = 'demo.pdf'
word_file  = 'demo.docx'
#converter
cv = Converter(pdf_file)
cv.convert(word_file,start=0,end= None)
cv.close()
