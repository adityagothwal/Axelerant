import tkinter as tk
import csv

root = tk.Tk()

v = tk.IntVar()
v.set(1)
#a = v.get()

Authors = [
        "Miguel de Cervantes",
        "Charles Dickens",
        "J.R.R. Tolkein",
        "Antoine de Saint-Exuper"
        ]

def ShowChoice():
    if v.get()==0:
        print("Miguel de Cervantes")
            

    elif v.get()==1:
        print("Charles Dickens")

    elif v.get()==2:
        print("J.R.R. Tolkein")

    else:
        print("Antoine de Saint-Exuper")

    #print(v.get())

tk.Label(root,
         text="Who is your favourite Author?",
         justify = tk.LEFT,
         padx = 20).pack()

for val, Author in enumerate(Authors):
    tk.Radiobutton(root,
                   text=Author,
                   padx=20,
                   variable=v,
command =ShowChoice,
value=val).pack(anchor=tk.W)
root.mainloop()



#Database

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  FavAuthor= v.get()
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
