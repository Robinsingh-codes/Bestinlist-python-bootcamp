

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    #from PIL import Image


    img =Image.open("study.jpg")
    print(img.format)

    import matplotlib.pyplot as plt

    plt.imshow(img)
    import PyPDF2

    pdf1File = open('100 Python Interview Questions.pdf', 'rb')
    pdf2File = open('Python Cheatsheet.pdf', 'rb')

    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    pdfOutputFile = open('MergedFiles.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)

    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()


    pdf3 = open("MergedFiles.pdf",'rb')

pdf3Reader = PyPDF2.PdfFileReader(pdf3)

print(pdf3Reader)
pdf3.close()
#mysql connector
import requests
import MySQLdb
from bs4
34"

)

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="Doctors1"
)
dbse = mydb.cursor()

url_to_scrape = 'https://news.ycombinator.com/news'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
