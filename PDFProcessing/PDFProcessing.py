import PyPDF4
import sys

files = sys.argv[1:]

merger = PyPDF4.PdfFileMerger()
for file in files:
    file = open(file, 'rb')
    merger.append(file)
merger.write('combined.pdf')
