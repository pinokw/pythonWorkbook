import PyPDF2
import re
import sys, os
fileDir = os.path.dirname(os.path.realpath('__file__'))

pdf_dplist=[]
pdf_folder = os.path.join(fileDir, 'pdf')
for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
            pdf_dplist.append(os.path.join(pdf_folder, file))

def read_pdf(pdf):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # count=pdfReader.numPages
    list_all=[]
    i=0
    #for i in range(pdfReader.numPages):
    for i in range(1, 2):
        page = pdfReader.getPage(i)
        page_content = page.extractText()  
        print(page_content)    
        #for x, item in enumerate (list_all):
        #   print (x, item)
    return list_all

for pdf in pdf_dplist:
    read_pdf(pdf)