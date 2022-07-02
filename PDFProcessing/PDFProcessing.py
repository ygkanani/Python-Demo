import PyPDF4
import sys

files = sys.argv[1:]

merger = PyPDF4.PdfFileMerger()
for file in files:
    with open(file, 'rb') as filename:
        merger.append(filename)
merger.write('combined.pdf')
