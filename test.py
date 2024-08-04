import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import webbrowser
from PIL import Image, ImageTk
from tkinter import filedialog
from UK_data import update_data
from US_format import select
def download_csv(url):
    
    webbrowser.open(url)
    


window = tk.Tk()
window.geometry("500x500")
window.title("HS NOMENCLATURE")
def details(b_row, b_col,c_row,c_col,i_row,i_col,path,c_name,f_url):
    if path is not None:
        image=Image.open(path)
        image.thumbnail((100,30))
        imagep=ImageTk.PhotoImage(image)
        image_label=tk.Label(window, image=imagep)
        image_label.grid(row=i_row, column=i_col)
        image_label.image=imagep

    download_button = tk.Button(window, text="Download", command=lambda:download_csv(f_url))
    download_button.grid(row=b_row, column=b_col,pady=5)
    country_l=tk.Label(window, text=c_name)
    country_l.grid(row=c_row,column=c_col)
    
    for i in range(7):  
       window.columnconfigure(i, weight=1)
       window.rowconfigure(i, weight=0)
       # window.rowconfigure()
#this part is for uk data         
btn=tk.Button(window, text="Download", command=update_data).grid(row=2, column=4) 
image_uk=Image.open("C:/Users/zaram/Desktop/python/iStock-1217765834.jpg")
image_uk.thumbnail((105,35))
image_ukp=ImageTk.PhotoImage(image_uk)
image_uk_label=tk.Label(window,image=image_ukp).grid(row=0,column=4)
country=tk.Label(window, text="UK").grid(row=1, column=4)
#this is button for us data formating
bttn=tk.Button(window,text="US Formating", command=select)
bttn.grid(padx=30, pady=20)

details(2,0,1,0,0,0,"C:/Users/zaram/Desktop/python/download.jpg","US","https://hts.usitc.gov/reststop/exportList?from=0101&to=9922.52.12&format=CSV&styles=true")

details(2,2,1,2,0,2,"C:/Users/zaram/Desktop/python/istockphoto-465702446-612x612.jpg","EU","https://circabc.europa.eu/ui/group/0e5f18c2-4b2f-42e9-aed4-dfe50ae1263b/library/b0e19770-7978-424e-9891-507d42a5558a/details?download=true")
details(2,3,1,3,0,0,None,"EU Import Duties","https://circabc.europa.eu/ui/group/0e5f18c2-4b2f-42e9-aed4-dfe50ae1263b/library/22cb6734-50d1-49a7-b87d-03c8720a538c/details?download=true")
window.mainloop() 

