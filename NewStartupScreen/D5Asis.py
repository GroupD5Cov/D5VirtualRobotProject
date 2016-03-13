#importing in functions that we need for the program to work
import pygame as pg



pg.init()

#setting up colour RGB values
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
pink = (255,20,147)
bright_red = (200,0,0)
bright_green = (0,200,0)

bg = pg.image.load('bg.png')

clock = pg.time.Clock()

font = pg.font.Font(None, 25)
frame_count = 0
frame_rate = 60
start_time = 180

menuDisplay = pg.display.set_mode((1200,600))
gameDisplay = pg.display.set_mode((1200, 600))
display_width = 800
display_height = 600

gameExit = False

KEY_REPEAT_SETTING = (200,70)

"""setting instruction colour and font"""
def instruction(i,Space,List):
    intrs = List
    font = pg.font.SysFont("Times", 25)
    message = intrs[i]
    rend = font.render(message, True, pg.Color("red"))
    return (rend, rend.get_rect(topleft=(900,35+Space)))

"""setting font and colour of the name displayed at the start"""
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

"""quit game button function"""
def quit_game():
    pg.quit()
    quit()
"""start game button function"""
def start_game():
    app = MainProgram()
    app.main_loop()

      
#Right hand side title screen colour
def game_intro():
    x=0
    y=0
    i = 0
    intro = True
    gameDisplay.fill(white)
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit function in the screen
                pg.quit()
                quit()
                
#Now creating the start-up screen
               
        gameDisplay.blit(bg,(x,y)) #displaying in starmenu file name bg x and y being the position
        largeText = pg.font.Font('freesansbold.ttf',80)#font and font size
        TextSurf, TextRect = text_objects("Bargain Inspector", largeText)#Program name
        TextRect.center = ((display_width/2),(display_height/2)) #text allignment
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Start",80,450,120,85,green,bright_green,start_game) #Button which starts the program, position,size, colour and linked to the start game function 
        button("Quit Game",605,450,160,85 ,red,bright_red,quit_game) # Button which closes the program, position,size, colour and linked to the quit game function

        intrs = ["INSTRUCTIONS:","Enter Car type", "Enter Condition", "Enter Gas Type", "Enter Price",]#Instruction displayed on the screen
        space = int(150) #position of the instruction on the screen 
        
        while i != 5: #5 total strings
            prompt = instruction(i,space,intrs)#i=number of instructions, space = position, intrs = intructions
            gameDisplay.blit(*prompt)
            space = space + 40 #how far wide the instruction
            pg.display.update() #for clock speed functuon
            i = i+1
            
        
        pg.display.update()
#limit the clock speed to 15 FPS (to prevent overflow)
        clock.tick(15)

#buttons function defined, event driven action (for the Start game and Quit button)        
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #when mouse button clicked outcome (1,0,0)
        pg.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None: #if mouse position (0,0,0 = no action, otherwise event driven action)
            action()
    else:
        pg.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pg.font.SysFont("Times",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#Sets up screen
menuDisplay.fill(white)
pg.draw.rect(menuDisplay , black,(800,0,10,600))
#Calls mainprogram to start game
game_intro()


pg.display.update()
pg.quit()
quit()

