from tkinter import *

mainWindow = Tk()
mainWindow.title("BRat Bank")
mainWindow.geometry("300x400")

title_page = Label(mainWindow, text="Welcome to BRat Bank", font=("Arial", 12))
title_page.pack(side="top", padx=5)

mainWindow.mainloop()