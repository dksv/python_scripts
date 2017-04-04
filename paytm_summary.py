#Extracts all Paytm bills from a directory and then process each to get amount, bill number and date
#Calculates total amount
#Merges all pdfs to single pdf  paytmbills_<month>

import os
import re
import PyPDF2
import datetime
year = datetime.datetime.now().year

def readPDF(filePath):
	pdfFileObj=open(filePath,'rb')
	pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(0)
	return pageObj.extractText()

def getPDFinDir(dirPath):
	files_list=os.listdir(dirPath)
	pdf_files=[]
	for f in files_list:
		if '.pdf' in f:
			pdf_files.append(f)
	return pdf_files

def megrePDF(pdf_files,dirPath):
	merger = PyPDF2.PdfFileMerger()
	for filename in pdf_files:
	    merger.append(PyPDF2.PdfFileReader(file(dirPath+"/"+filename, 'rb')))
	merger.write("paytmbills_"+str(datetime.datetime.now().month-1)+".pdf")

print "Enter  dir path"

dirPath=raw_input()

pdf_files=getPDFinDir(dirPath)

print "list of  pdf files"

for pdf in pdf_files:
	print pdf

print "Extracting files Info......"
readPDF(dirPath+"/"+pdf_files[0])

total=0

print "\n\nbill_number"+"   "+"amount"+"   "+"date"
for pdf in pdf_files:
	path=dirPath+"/"+pdf
	text=readPDF(path)

	#print text
	pattern= re.compile(r'#(\d*)'+str(year))
	bill_number=pattern.search(text).group(1)
	pattern= re.compile(r'(\d*)Amount')
	amount=pattern.search(text).group(1)
	pattern= re.compile(str(year)+r'-\d\d-\d\d')
	date=pattern.search(text).group(0)
	total=total+int(amount)
	print bill_number+"   "+amount+"   "+date

print "\n\nTOTAL AMOUNT ",total


megrePDF(pdf_files,dirPath)
print("\n\npdfs Merged")




