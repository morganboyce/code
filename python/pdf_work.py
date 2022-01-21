# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyPDF2 import PdfFileMerger
import os

root = r'..\dissertation\monograph\dissertation'
pdfs = [os.path.join(root,'Boyce final draft 2.pdf'),
        os.path.join(root,'admin/Approvals/Approval Page Only (signed).pdf')]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.merge(4, pdf)

merger.write(os.path.join(root,"result.pdf"))
merger.close()


from PyPDF2 import PdfFileWriter, PdfFileReader
pages_to_delete = [3] # page numbering starts from 0
infile = PdfFileReader(os.path.join(root,"result.pdf"), 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i not in pages_to_delete:
        p = infile.getPage(i)
        output.addPage(p)

with open(os.path.join(root,"Boyce_w_Approval.pdf"), 'wb') as f:
    output.write(f)