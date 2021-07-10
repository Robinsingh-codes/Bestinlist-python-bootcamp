
#1
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width=550, height=550, bg='gray95', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Image Conversion From JPEG To PNG')
label1.config(font=('helvetica', 20))
canvas1.create_window(250,40, window=label1)


def getJPG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_JPG = tk.Button(text="      Import JPG File     ", command=getJPG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 200, window=browseButton_JPG)


def convertToPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)

saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 280, window=saveAsButton_PNG)

root.mainloop()

#***2
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebo

# configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['divya']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def getweather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin,temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")


# search city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3])+" Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


app = Tk()

app.title("Weather App")

app.geometry("300x300")

# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
Search_btn = Button(app, text="Search Weather",bg='royalblue', fg='white',font=('helvetica', 12, 'bold'), command=search)
Search_btn.pack()
location_lbl = Label(app, text="Location", font={'bold', 20})
location_lbl.pack()
temperature_label = Label(app, text="")
temperature_label.pack()
weather_l = Label(app, text="")
weather_l.pack()
app.mainloop()

#***3
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader
from pathlib import Path

filelist = []

# initiate merger Object
merger = PdfFileMerger()


def open_file(files):
    filepath = askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if not (filepath and Path(filepath).exists()):
        return
    files.append(filepath)
    # list out all filenames
    lbl_items["text"] = '\n'.join(str(f) for f in files)
    if len(files) >= 2 and btn_merge['state'] == "disabled":
        btn_merge["state"] = "normal"


def merge_pdfs(files):
    for f in files:
        merger.append(PdfFileReader(open(f, "rb")))

    output_filename = ent_output_name.get()

    if not output_filename:
        output_filename = "Untitled.pdf"
    elif ".pdf" not in output_filename:
        output_filename += ".pdf"
    merger.write(output_filename)


# create desktop GUI
window = tk.Tk()
window.title("PDFMerger Tk")
window.geometry("500x500")
# not allowed resizing x y direction
window.resizable(0, 0)

# --- Ask open files ---
fr_bg1 = tk.Frame(window, bd=3)
lbl_open = tk.Label(fr_bg1, text="Please choose PDFs to join: (2 and above)")
lbl_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_open = tk.Button(fr_bg1, text="Open file", bg='royalblue', fg='white', font=('helvetica', 12, 'bold'),
                     command=lambda: open_file(filelist))
btn_open.grid(row=1, column=0, sticky="ew", padx=5)
lbl_items = tk.Label(fr_bg1, text="")
lbl_items.grid(row=2, column=0, pady=5)
fr_bg1.pack()

# --- Button to merge PDFs ---
fr_bg2 = tk.Frame(window, bd=3)
lbl_to_merge = tk.Label(fr_bg2, text="Merge selected files (in PDF)")
lbl_to_merge.grid(row=0, column=0, sticky="ew", padx="5", pady="5")

ent_output_name = tk.Entry(master=fr_bg2, width=7)
ent_output_name.grid(row=1, column=0, sticky="ew")

btn_merge = tk.Button(fr_bg2, bg='royalblue', font=('helvetica', 12, 'bold'),
                      text="Merge PDF",
                      state="disabled",
                      command=lambda: merge_pdfs(filelist))
btn_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
fr_bg2.pack()

btn_exit = tk.Button(window, text="Exit", command=window.destroy, bd=2, bg='royalblue', fg='black',
                     font=('helvetica', 12, 'bold'), )
btn_exit.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.FALSE)

if __name__ == "__main__":
    window.mainloop()
