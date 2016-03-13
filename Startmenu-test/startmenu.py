from Tkinter import *
root =Tk()
canvas = Canvas(width = 1280, height = 600, bg = 'silver')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'start menu1.gif')
canvas.create_image(30, 10, image = gif1, anchor = NW)

QUIT = Button(root, text="QUIT GAME", fg="red",command=root.destroy)
QUIT.pack(side="bottom")
QUIT.pack(side="right")

Start = Button(root, text="Start", fg="green",)
Start.pack(side="bottom")
Start.pack(side="left")

mainloop()

