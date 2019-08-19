from tkinter import *
import os

window = Tk()

window.title("Lead&Camp")
window.geometry("450x400")
window.iconbitmap(r"C:\users\trist\python\beno.ico")

def leadDEV():
    Label(window,text="DEV LEAD!", font=50).grid(row=2,column=1,sticky=W)
    os.startfile(r"C:\Users\trist\Python\__pycache__\leadGenerator_DEV.cpython-37.pyc")
    
def campDEV():
    Label(window,text="DEV CAMP!", font=50).grid(row=4,column=1,sticky=W)
    os.startfile(r"C:\Users\trist\Python\__pycache__\campGenerator_DEV.cpython-37.pyc")

def leadQA():
    Label(window,text="QA LEAD!", font=50).grid(row=6,column=1,sticky=W)
    os.startfile(r"C:\Users\trist\Python\__pycache__\leadGenerator_QA.cpython-37.pyc")

def campQA():
    Label(window,text="QA CAMP!", font=50).grid(row=8,column=1,sticky=W)
    os.startfile(r"C:\Users\trist\Python\__pycache__\campGenerator_QA.cpython-37.pyc")

def leadPROD():
    Label(window,text="PROD LEAD!", font=50).grid(row=10,column=1,sticky=W)
    os.startfile(r"C:\Users\trist\Python\__pycache__\leadGenerator_PROD.cpython-37.pyc")

def campPROD():
    Label(window,text="PROD CAMP!", font=50).grid(row=12,column=1,sticky=W)
    os.startfile(r"C:\Users\trist\Python\__pycache__\campGenerator_PROD.cpython-37.pyc")

Label(window, text="Create Leads or Campaigns", font=18).grid(row=0, column=0, sticky=W)

Button(window, text = "Generate Lead in DEV", width = 30, command=leadDEV).grid(row=2,column=0,sticky=W)
Button(window, text = "Generate Camp in DEV", width = 30, command=campDEV).grid(row=4,column=0,sticky=W)

Button(window, text = "Generate Lead in QA", width = 30, command = leadQA).grid(row=6, column=0,sticky=W)
Button(window, text = "Generate Camp in QA", width = 30, command = campQA).grid(row=8, column=0,sticky=W)

Button(window, text = "Generate Lead in PROD", width = 30, command = leadPROD).grid(row=10, column=0,sticky=W)
Button(window, text = "Generate Camp in PROD", width = 30, command = campPROD).grid(row=12, column=0,sticky=W)

Label(window, text = "Generate DEV lead or camp").grid(row=1,column=0,sticky=W)
Label(window, text = "   ").grid(row=3, column=0, sticky=W)
Label(window, text = "Generate QA lead or camp").grid(row=5,column=0,sticky=W)
Label(window, text = "   ").grid(row=7, column=0, sticky=W)
Label(window, text = "Generate PROD lead or camp").grid(row=9,column=0,sticky=W)
Label(window, text = "   ").grid(row=11, column=0, sticky=W)

window.mainloop()
 