from Tkinter import *
root =Tk()
canvas = Canvas(width = 1280, height = 600, bg = 'silver')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'startmenu2.gif')
canvas.create_image(30, 10, image = gif1, anchor = NW)

Start = Button(root, text="START", height = 4, width = 10,fg="green",)
Start.pack(side = 'bottom', padx = 10, pady = 10)
Start.pack(side = 'left')

QUIT = Button(root, text="QUIT GAME", height = 4, width = 10, fg="red", command=root.destroy)
QUIT.pack(side = 'bottom', padx = 10, pady = 10)
QUIT.pack(side = 'right')

mainloop()
