#1
#browse option
# Python program to extract text from all the images in a folder 
# storing the text in corresponding files in a different folder 

from PIL import Image 

import pytesseract as pt 

import os 

      

def main(): 

    # path for the folder for getting the raw images 

    path ="E:\\mucomputer\\images"

  

    # path for the folder for getting the output 

    tempPath ="E:\\mufile\\textFiles"

  

    # iterating the images inside the folder 

    for imageName in os.listdir(path): 

              

        inputPath = os.path.join(path, imageName) 

        img = Image.open(inputPath) 

  

        # applying ocr using pytesseract for python 

        text = pt.image_to_string(img, lang ="eng") 

  

        # for removing the .jpg from the imagePath 

        imagePath = imagePath[0:-4] 

  

        fullTempPath = os.path.join(tempPath, 'time_'+imageName+".txt") 

        print(text) 

  

        # saving the  text for every image in a separate .txt file 

        file1 = open(fullTempPath, "w") 

        file1.write(text) 

        file1.close()  

  

if __name__ == '__main__': 

    main() 
 
# naming the GUI interface to image_conversion_APP

root.title("Image_Conversion_App")
 
# creating the Function which converts the jpg_to_png

def jpg_to_png():

    global im1
 

    # import the image from the folder

    import_filename = fd.askopenfilename()

    if import_filename.endswith(".jpg"):
 

        im1 = Image.open(import_filename)
 

        # after converting the image save to desired

        # location with the Extersion .png

        export_filename = fd.asksaveasfilename(defaultextension=".png")

        im1.save(export_filename)
 

        # displaying the Messaging box with the Success

        messagebox.showinfo("success ", "your Image converted to Png")

    else:
 

        # if Image select is not with the Format of .jpg 

        # then display the Error

        Label_2 = Label(root, text="Error!", width=20,

                        fg="red", font=("bold", 15))

        Label_2.place(x=80, y=280)

        messagebox.showerror("Fail!!", "Something Went Wrong...")
 
 
button1 = Button(root, text="JPG_to_PNG", width=20, height=2, bg="green",

                 fg="white", font=("helvetica", 12, "bold"), command=jpg_to_png)
 

button1.place(x=120, y=120)
root.geometry("500x500+400+200")
root.mainloop()

#2  as ‘fetch button’ and have a 
#functionality of fetching the weather on
 # a given location in text box
# Python program to find current
# weather details of any city
# using openweathermap api
 
# import required modules
import requests, json
 
# Enter your API key here
api_key = "Your_API_Key"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
city_name = input("Enter city name : ")
 
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object
# convert json format data into
# python format data
x = response.json()
 
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
 
    # store the value of "main"
    # key in variable y
    y = x["main"]
 
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
 
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
 
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
 
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
 
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
 
    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))
 
else:
    print(" City Not Found ")

#3
#Create two browse button and place
# the .pdf file for the buttons and create
# a merge pdf option -  Watermark
# Merger App
from pathlib import Path
from PyPDF2 import PdfFileReader

# Change the path below to the correct path for your computer.
pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice-files"
    / "Pride_and_Prejudice.pdf"
)

# 1
pdf_reader = PdfFileReader(str(pdf_path))
output_file_path = Path.home() / "Pride_and_Prejudice.txt"

# 2
with output_file_path.open(mode="w") as output_file:
    # 3
    title = pdf_reader.documentInfo.title
    num_pages = pdf_reader.getNumPages()
    output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")

    # 4
    for page in pdf_reader.pages:
        text = page.extractText()
        output_file.write(text)






