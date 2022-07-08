# Packaged used
# pyttsx3
# It is a python library for text to speech. it has many 
# functions which will help the machine to communicate 
# with us. It will help the machine to speak to us.

# PyPDF2
# It will help to the text from the PDF. A pure-python library 
# built as a PDF toolkit. It is capable of extracting document
# information, spiltting documents page by page, merging 
# documnets page by page etc.

# pip install pyttsx3
# pip install PyPDF2

# Approach
# Import the PyPDF2 and pyttsx3 modules
# open the PDF file
# use PdfFileReader() to read the PDF.
# We just have to give the path of the PSD as the argument
# Use the getPage() method to selet the page to be read.
# Extract the text from the usage using extractText().
# Instantiate a pyttsx3 object
# use the say() and runwait()a methods to speak out the text

import pyttsx3
import PyPDF2

# path of the pdf file
path = open("file.pdf", "rb")

# Creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# The page with which you want to start
# this will read the page of 25th page
from_page = pdfReader.getPage(90)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()