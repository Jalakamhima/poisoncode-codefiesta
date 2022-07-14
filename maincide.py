!pip3 install pdfminer3
!pip3 install deep_translator
!pip3 install nltk
import nltk
nltk.download('punkt')


#extracting text from test.pdf
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io

resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)

with open('/content/test.pdf', 'rb') as fh:

    for page in PDFPage.get_pages(fh,
                                  caching=True,
                                  check_extractable=True):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()

# close open handles
converter.close()
fake_file_handle.close()

print(text)

#traslating the extracted text and printing it


from nltk.tokenize import sent_tokenize
from deep_translator import GoogleTranslator
from tqdm import tqdm
sentences=sent_tokenize(text, language = "english")
translated_sentences = []
t_s = ''
translate = GoogleTranslator(source='auto', target='en').translate
for i in tqdm(range(len(sentences))):
  t_s = t_s + translate(sentences[i])
  
 print(t_s)
