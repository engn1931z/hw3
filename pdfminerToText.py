# Following code from https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
# Tim Arnold article on "Manipulating PDFs from Python)

import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert(fname, pages=None):
    if not pages:   
        pagenums = set()
    else:
        pagenums = set(pages)
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    fp = open(fname, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenums, maxpages=0,
                                  password="",
                                  caching=True,
                                  check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text

# Note: For alternative implementations, see http://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python/
