from tkinter import *

root =Tk()
canvas = Canvas(width = 1280, height = 600, bg = 'silver')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'startmenu2.gif')
canvas.create_image(30, 10, image = gif1, anchor = NW)

Start = Button(root, text="START", height = 4, width = 10,fg="green",)
Start.pack(side = 'bottom', padx = 10, pady = 10)
Start.pack(side = 'left')

def button (Start):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    command=root2.start
    
QUIT = Button(root, text="QUIT GAME", height = 4, width = 10, fg="red", command=root.destroy)
QUIT.pack(side = 'bottom', padx = 10, pady = 10)
QUIT.pack(side = 'right')

mainloop()

root2 = game()

class Application(Frame):
    """ A GUI application with buttons. """

    def __init__(self,master):
        "Initiaize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):

        self.result = Text(self, width =40, height =4, wrap = WORD)
        self.result.grid(row =19, column = 0, columnspan =3)

        
        """Create widgets for car type choices."""
        Label(self,
              text = "Choose manufacturer:"
              ).grid(row =0, column =0, sticky =W)
        #MANUFACTURER
        self.manu = StringVar()

        Radiobutton(self,
                    text = "Vauxhall",
                    variable = self.manu,
                    value = "Vauxhall",
                    command = self.update_text
                    ).grid(row =2, column = 0, sticky =W)
        Radiobutton(self,
                    text = "BMW",
                    variable = self.manu,
                    value = "BMW",
                    command = self.update_text
                    ).grid(row =3, column = 0, sticky =W)
        Radiobutton(self,
                    text = "Lexus",
                    variable = self.manu,
                    value = "Lexus",
                    command = self.update_text
                    ).grid(row =4, column = 0, sticky =W)
        Radiobutton(self,
                    text = "Range Rover",
                    variable = self.manu,
                    value = "Range Rover",
                    command = self.update_text
                    ).grid(row =5, column = 0, sticky =W)

        #CONDITION
        Label(self,
              text = "Car condition:"
              ).grid(row =7, column =0, sticky =W)

        self.cond = StringVar()

        Radiobutton(self,
                    text = "New",
                    variable = self.cond,
                    value = " in new condition new",
                    command = self.update_text
                    ).grid(row =8, column = 0, sticky =W)
        Radiobutton(self,
                    text = "Used",
                    variable = self.cond,
                    value = " in used condition",
                    command = self.update_text
                    ).grid(row =9, column = 0, sticky =W)
        #GAS TYPE
        Label(self,
              text = "Gas type:"
              ).grid(row =10, column =0, sticky =W)

        self.gas = StringVar()

        Radiobutton(self,
                    text = "Petrol",
                    variable = self.gas,
                    value = " with petrol engine, ",
                    command = self.update_text
                    ).grid(row =11, column = 0, sticky =W)
        Radiobutton(self,
                    text = "Diesel",
                    variable = self.gas,
                    value = " with diesel engine, ",
                    command = self.update_text
                    ).grid(row =12, column = 0, sticky =W)

        #Price range
        Label(self,
              text = "Price range:"
              ).grid(row =13, column =0, sticky =W)

        self.price = StringVar()

        Radiobutton(self,
                    text = "<10.000 GBP",
                    variable = self.price,
                    value = " price range less than 10.000 GBP",
                    command = self.update_text
                    ).grid(row =14, column = 0, sticky =W)
        Radiobutton(self,
                    text = "<15.000 GBP",
                    variable = self.price,
                    value = " price range less than 15.000 GBP",
                    command = self.update_text
                    ).grid(row =16, column = 0, sticky =W)
        Radiobutton(self,
                    text = "<25.000 GBP",
                    variable = self.price,
                    value = " price range less than 25.000 GBP",
                    command = self.update_text
                    ).grid(row =17, column = 0, sticky =W)
        Radiobutton(self,
                    text = ">30.000 GBP",
                    variable = self.price,
                    value = " price range over 30.000 GBP",
                    command = self.update_text
                    ).grid(row =18, column = 0, sticky =W)

        
    def update_text(self):
        """Update the text area"""
        message = "Your current car selection is "
        message += self.manu.get()
        message += self.cond.get()
        message += self.gas.get()
        message += self.price.get()
        self.result.delete(0.0, END)
        self.result.insert(0.0, message)
root = Tk()
root.title("Bargain Inspector")
app = Application(root)
root.mainloop()
