from pdf2docx import Converter
pdf_file = 'consolidated_report.pdf'
word_file  = 'consolidated_report.docx'
#converter
cv = Converter(pdf_file)
cv.convert(word_file,start=0,end= None)
cv.close()