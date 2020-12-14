import cv2
import numpy
import sys
import os
import os.path
from os import path


outfileparts = os.path.split(sys.argv[1])
outdir=outfileparts[0]+'\\jpeg'
if not os.path.exists(outdir):
    os.mkdir(outdir)
fileroot = os.path.splitext(outfileparts[1])
if (fileroot[1] != '.pdf'):
    print('ERROR: Input file:' + sys.argv[1] + '. Converts only pdf files.')
    sys.exit()
first_outfile = outdir+'\\'+fileroot[0]+'-1'+'.jpg'

# Don't convert if already converted
if path.exists(first_outfile):
    sys.exit()

from pdf2image import convert_from_path
pages = convert_from_path(sys.argv[1], 500)
pagenumber = 1
for page in pages:
    opencvImage = cv2.cvtColor(numpy.array(page), cv2.COLOR_RGB2GRAY )
    ret,thresh1 = cv2.threshold(opencvImage,127,255,cv2.THRESH_BINARY)
    outfile = outdir+'\\'+fileroot[0]+'-'+str(pagenumber)+'.jpg'
    print(outfile)
    cv2.imwrite(outfile , thresh1)
    pagenumber = pagenumber + 1
