from tkinter import W
import win32com.client
import docx

docx_filename = ''
pdf_filename = ''

doc = docx.Document()
doc.save(docx_filename)

wd_format_pdf = 17
word_obj = win32com.client.Dispatch('Word.Application')

doc_obj = word_obj.Documents.Open(docx_filename)
doc_obj.SaveAs(pdf_filename, FileFormat=wd_format_pdf)
doc_obj.Close

word_obj.Quit()