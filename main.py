from tkinter import *

mainWindow = Tk()
mainWindow.title("Cash G Bank")
mainWindow.geometry("400x500")

title_page = Label(mainWindow, text="Welcome to Cash G Bank", font=("Arial", 12))
title_page.pack(side="top", padx=5)

mainWindow.mainloop()