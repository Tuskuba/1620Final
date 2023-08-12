from gui import *
from tkinter import *
def main():
    window = Tk()
    window.title("Lab 10")
    window.geometry("500x500")
    window.resizable(False,False)
    Gui(window)
    window.mainloop()
if __name__== "__main__":
    main()