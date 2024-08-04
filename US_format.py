import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd
def select():
   file=filedialog.askopenfilename()
   
   df=pd.read_csv(file)
   df["HTS Number"]=df["HTS Number"].str.replace(".","")
   df = df[df["HTS Number"].apply(lambda x: len(str(x)) >= 10)]

   df=df.iloc[:,[0,2]]
   df=pd.DataFrame(df)
   df.rename(columns={"HTS Number":"HS code"}, inplace=True)
   df.to_csv("C:/Users/zaram/Desktop/data/US_fromated_data.csv", index=0, encoding="UTF-8")

