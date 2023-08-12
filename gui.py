from tkinter import *
class Gui:
    def __init__(self, window):
        """
        creates the gui window for the menu
        :param window: takes the window specified in window.gui
        """
        self.window = window
        #gui for sandwich ordering
        self.frameSand = Frame(self.window)
        self.labelSand = Label(self.frameSand, text="Sandwiches $4.00 ea")
        self.inputSand = Entry(self.frameSand, justify="right")

        self.labelSand.pack(side="left")
        self.inputSand.pack(padx=5, side="left")
        self.frameSand.pack(anchor='w', padx=10, pady=10)

        #gui for cookie ordering
        self.frameCookie = Frame(self.window)
        self.labelCookie = Label(self.frameCookie, text="Cookie $1.50 ea")
        self.inputCookie = Entry(self.frameCookie, justify="right")

        self.labelCookie.pack(side="left")
        self.inputCookie.pack(padx=5, side="left")
        self.frameCookie.pack(anchor='w', padx=10, pady=10)

        #GUI for water ordering
        self.frameWater = Frame(self.window)
        self.labelWater = Label(self.frameWater, text="Water $1 ea")
        self.inputWater = Entry(self.frameWater, justify="right")

        self.labelWater.pack(side="left")
        self.inputWater.pack(padx=5, side="left")
        self.frameWater.pack(anchor='w', padx=10, pady=10)
        #Buttons that issue commands
        self.frameButton = Frame(self.window)
        self.buttonConfirm = Button(self.frameButton, text="Confirm Purchase", command=self.confirm)
        self.buttonLabel = Label(self.frameButton, text="Please fill out all values")

        self.buttonConfirm.pack(pady=20)
        self.buttonLabel.pack()
        self.frameButton.pack()

        self.frameButton2= Frame(self.window)
        self.buttonClear = Button(self.frameButton2, text="Clear Screen", command=self.clear)


        self.buttonClear.pack(pady=20)
        self.frameButton2.pack()

    def confirm(self):
        """
        a function that displays the totals for each item and the final total
        """
        try:
            sandTotal = float(self.inputSand.get())*4.00
            cookieTotal = float(self.inputCookie.get())*1.50
            waterTotal = float(self.inputWater.get())*1.00
            finalTotal = sandTotal+cookieTotal+waterTotal
        except:
            self.buttonLabel(text="Enter correct values.(they must be ints)")
        self.frameSandTot = Frame(self.window)
        self.labelSandTot = Label(self.frameSandTot, text=f'Sandwich total = ${sandTotal:.2f}')

        self.labelSandTot.pack(side='left')
        self.frameSandTot.pack(padx=5, pady=5, side='left')

        self.frameWatTot = Frame(self.window)
        self.labelWatTot = Label(self.frameWatTot, text=f'Water total = ${waterTotal:.2f}')

        self.labelWatTot.pack(side='left')
        self.frameWatTot.pack(padx=5, pady=10, side='left')

        self.frameCookieTot = Frame(self.window)
        self.labelCookieTot = Label(self.frameSandTot, text=f'Cookie total = ${cookieTotal:.2f}')

        self.labelCookieTot.pack(side='left')
        self.frameCookieTot.pack(padx=5, pady=15, side='left')

        self.frameTot = Frame(self.window)
        self.labelTot = Label(self.frameTot, text=f'Final total = ${finalTotal:.2f}')

        self.labelTot.pack(side='left')
        self.frameTot.pack(padx=5, pady=20, side='left')


    def clear(self):
        self.inputWater.delete(0,END)
        self.inputCookie.delete(0, END)
        self.inputSand.delete(0, END)
        self.frameTot.destroy()
        self.frameSandTot.destroy()
        self.frameWatTot.destroy()
        self.frameCookieTot.destroy()
