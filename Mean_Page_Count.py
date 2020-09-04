from PyPDF2 import PdfFileReader
import os, sys
import statistics

page_counts = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf = PdfFileReader(open(filename, 'rb'))
        page_counts.append(pdf.getNumPages())

if not page_counts:
    print("No PDF's found")
    sys.exit()

print("Mean page count of all PDF's in this folder: " + str(statistics.mean(page_counts)))
