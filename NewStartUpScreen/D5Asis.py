#importing in functions that we need for the program to work
import pygame as pg
import random
from textbox import TextBox

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

bg = pg.image.load('startscreen.png')

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

KEY_REPEAT_SETTING = (200,70)#textbox to appear in the same position after action 

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
    gameDisplay.fill(black)
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit function added 
                pg.quit()
                quit()
            
#Now creating the start-up screen
               
        gameDisplay.blit(bg,(x,y)) #displaying in starmenu bg being pygame, x and y being the position
        largeText = pg.font.Font('freesansbold.ttf',80)#font and font size
        TextSurf, TextRect = text_objects("Bargain Inspector", largeText)#Program name
        TextRect.center = ((display_width/2),(display_height/2)) #text allignment
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Start",80,450,120,85,white,bright_green,start_game) #Button which starts the program, position,size, colour and linked to the start game function 
        button("Quit Game",605,450,160,85,white,bright_red,quit_game) # Button which closes the program, position,size, colour and linked to the quit game function

        intrs = ["INSTRUCTIONS:","Enter colour for car type", "Enter co-ordinates", "Enter value of car models", "Enter time for robot",]#Instruction displayed on the screen
        space = int(150) #position of the instruction on the screen 
        
        while i != 5: #5 total strings
            prompt = instruction(i,space,intrs)#i=number of instructions, space = position, intrs = intructions
            gameDisplay.blit(*prompt)
            space = space + 40 #how close to each other the instructions
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

#Initialising the main program with class attribute
class MainProgram(object):
    def __init__(self):
        """The initialisation function of key components of the main program"""
        pg.init()
        pg.display.set_caption("D5's Bargain Inspector")
        bg = pg.image.load('mainScreen.png')
        gameDisplay.blit(bg,(0,0))
        self.red = []
        self.blue = []
        self.green = []
        self.pink = []
        self.colourA =[]
        self.colour = ""
        self.num_items = 0
        self.finishedList =[]
        self.time = 0
        self.frame_count = 0
        self.frame_rate = 60
        self.start_time = 180
        self.screen = menuDisplay
        self.clock = pg.time.Clock()
        self.robot_loc = []
        self.fps = 60.0
        self.done = False
        self.input = TextBox((900,200,200,40),command=self.get_input,           #setting the size and position of the text box
                              clear_on_enter=True,inactive_on_enter=False)
        self.user_input = ""
        self.color = white
        self.prompt = self.make_prompt('Enter Red:BMW, Blue:Vauxhall, Green:Land Rover, Pink:Lexus')
        pg.key.set_repeat(*KEY_REPEAT_SETTING) #textbox to appear in the same position after action 

    def make_prompt(self,Message):
        """ Function to create the labels, called everytime a new input is entered """
        pg.draw.rect(menuDisplay , white,(820,165,400,30)) #1 is left right position, 2 is up down, 3 is width, 4 is height 
        font = pg.font.SysFont("Times", 14)
        message = Message
        rend = font.render(message, True, pg.Color("black"))
        return (rend, rend.get_rect(topleft=(820,165)))#position of the text in the screen

    def event_loop(self):
        """ A continuous FOR loop which allows an exit for our main program"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.input.get_event(event)

    def random_types(self):
        """Randomly generates colours into the screen and randomly gives them a price and a name eg. red-bmw,price """
        names = ["BMW", "Vauxhall", "Land Rover", "Lexus"]
        for i in range(50):
            item = random.randint(1,3)
            radx = random.randint(0,790)
            rady = random.randint(0,590)
            radp = random.randint(1,20)
            radnum = random.randint(1,4) - 1
            radn = names[radnum]
            coords = [radx,rady,radp,radn]

            if item == 1:
                pg.draw.rect(menuDisplay , red,(radx,rady,10,10))
                self.red.append(coords)
            elif item == 2:
                pg.draw.rect(menuDisplay , blue,(radx,rady,10,10))
                self.blue.append(coords)
            elif item == 3:
                pg.draw.rect(menuDisplay, green,(radx,rady,10,10))
                self.green.append(coords)
            elif item == 4:
                pg.draw.rect(menuDisplay, pink,(radx,rady,10,10))
                self.pink.append(coords)
            i = i +1

    def get_input(self,id,input):
        """ allows the user to search for cars by enterin a specific colour """
        try:
            input = input.lower()
            self.user_input = input
            self.colour = input
            if self.user_input == "red" or self.user_input == "blue" or self.user_input == "green" or self.user_input == "pink":
                self.prompt = self.make_prompt('Where do you want to start : e.g. NW')
                self.input = TextBox((900,200,200,40),command=self.robot_start, # textbox position 
                              clear_on_enter=True,inactive_on_enter=False)
            if input == "red":
                for coord in self.red:
                    x = coord[0]
                    y = coord[1]
                    pg.draw.rect(menuDisplay, red,(x,y,15,15))
                    self.colourA = self.red

            elif input == "blue":
                for coord in self.blue:
                    x = coord[0]
                    y = coord[1]
                    pg.draw.rect(menuDisplay, blue,(x,y,15,15))
                    self.colourA = self.blue

            elif input == "green":
                for coord in self.green:
                    x = coord[0]
                    y = coord[1]
                    pg.draw.rect(menuDisplay, green,(x,y,15,15))
                    self.colourA = self.green

            elif input == "pink":
                for coord in self.pink:
                    x = coord[0]
                    y = coord[1]
                    pg.draw.rect(menuDisplay, pink,(x,y,15,15))
                    self.colourA = self.pink
                    
            else:
                self.prompt = self.make_prompt('Please enter the colour type given')
            self.screen = menuDisplay

        except ValueError:
            print("ERROR")

    def robot_start(self,id,input):
        """ Allows the user to choose the starting position of the robot"""
        input = input.upper()
        self.robot_loc = input
        if input == "N":
            pg.draw.rect(menuDisplay, red,(400,0,20,30))
            self.robot_loc = [400,0]
        elif input == "E":
            pg.draw.rect(menuDisplay, blue,(750,300,20,30))
            self.robot_loc = [750,300]
        elif input == "S":
            pg.draw.rect(menuDisplay, pink,(400,550,20,30))
            self.robot_loc = [400,550]
        elif input == "W":
            pg.draw.rect(menuDisplay, green,(10,300,20,30))
            self.robot_loc = [10,300]
        elif input == "NW":
            pg.draw.rect(menuDisplay, bright_green,(10,10,20,30))
            self.robot_loc = [10,10]
        elif input == "NE":
            pg.draw.rect(menuDisplay, bright_red,(750,10,20,30))
            self.robot_loc = [750,10]
        elif input == "SW":
            pg.draw.rect(menuDisplay, red,(10,550,20,30))
            self.robot_loc = [10,550]
        elif input == "SE":
            pg.draw.rect(menuDisplay, pink,(750,550,20,30))
            self.robot_loc = [750,550]
        else:
            self.prompt = self.make_prompt('Please enter a valid co-cordinate for the robot to search')
        if input == "N" or input == "E" or input == "S" or input == "W" or input == "NW" or input == "NE" or input == "SW" or input == "SE":
            self.prompt = self.make_prompt('Please enter the number of car types you will like to find?')
            self.input = TextBox((900,200,200,40),command=self.number_of_items, #textbox position
                        clear_on_enter=True,inactive_on_enter=False)

    def number_of_items(self,id,input):
        """ This will allow the user to enter the number of chosen car models they want to find"""

        if input.isdigit() and (int(input) <= len(self.colourA)):
            self.num_items = int(input)
            self.prompt = self.make_prompt('Enter the minutes you want the robot to search for?')
            self.input = TextBox((900,200,200,40),command=self.input_time, #textbox pisition
                                clear_on_enter=True,inactive_on_enter=False)

        else:
           self.prompt = self.make_prompt('Please enter how many chosen car models to find?')

    def input_time(self,id,input):
        """ Allows the user to enter the time for the robot to search for car types"""

        if input.isdigit() and int(input) <= 15:
            self.time = input
            self.start_time = int(self.time) * 60

        else:
            self.prompt = self.make_prompt('Please enter a valid time, e.g 1 for 1 minute')

    def collide(self,c1, p1, p2, p3,xORy):
        """ Tests to see if the next pixals are not white"""
        locations = [p1,p2,p3]
        self.Collide = False
        i = 0
        if xORy == "X":
            while i != 3:
                colour = menuDisplay.get_at((c1,locations[i]))  # gets the colour of the pixal at the coordinates
                if (c1 >= self.nextX and c1 <= (self.nextX + 15)) and (p1 >= self.nextY and p1 <= (self.nextY + 15)):
                    i=i+1
                    continue
                elif (colour[0] != 255 or colour[1] != 255 or colour[2] != 255):
                    self.Collide = True
                    break
                else:
                    i=i+1
                    continue
        elif xORy == "Y":
            while i != 3:
                colour = menuDisplay.get_at((locations[i],c1))
                if (c1 >= self.nextY and c1 <= (self.nextY + 15)) and (p1 >= self.nextX and p1 <= (self.nextX + 1)):
                    i=i+1
                    continue
                elif (colour[0] != 255 or colour[1] != 255 or colour[2] != 255):
                    self.Collide = True
                    break
                else:
                    i=i+1
                    continue

    def bubbleSort(self,colourL):
        """ Used to sort the list in order of price, cheapest first"""
        for passnum in range(len(colourL)-1,0,-1):
            for i in range(passnum):
                if colourL[i][2]>colourL[i+1][2]:
                    temp = colourL[i]
                    colourL[i] = colourL[i+1]
                    colourL[i+1] = temp

    def binarySearch(self, alist, item):
        """Used to search a list for the search item and returns all infomation about that item"""
        first = 0
        last = len(alist)-1
        found = False

        while first<=last and not found:
            midpoint = (first + last)//2
            if alist[midpoint][0] == item:
                return(alist[midpoint])
            else:
                if item < alist[midpoint][0]:
                    last = midpoint-1
                else:
                    first = midpoint+1

        return found

    def quick_sort(self,items):
        """ Used to sort a list in order by x coords for binary search"""
        if len(items) > 1:
            pivot_index = len(items) // 2
            smaller_items = []
            larger_items = []

            for i, val in enumerate(items):
                if i != pivot_index:
                    if val < items[pivot_index]:
                        smaller_items.append(val)
                    else:
                        larger_items.append(val)


            self.quick_sort(smaller_items)
            self.quick_sort(larger_items)
            items[:] = smaller_items + [items[pivot_index]] + larger_items

    def robot_move(self):
        """Makes the robot move visually and makes a countdown timer that countdowns from the users input"""
        i = 0
        if self.colour == "red":
            self.bubbleSort(self.red)
            locations = self.red
        elif self.colour == "blue":
            self.bubbleSort(self.blue)
            locations = self.blue
        elif self.colour == "green":
            self.bubbleSort(self.green)
            locations = self.green
        elif self.colour == "pink":
            self.bubbleSort(self.pink)
            locations = self.pink
#pg.draw.rect(menuDisplay, white,(self.robot_loc[0],self.robot_loc[1],20,30))
        print(locations)
        while i != self.num_items :   #Makes the robot move visually
            self.event_loop()
            nextX = locations[i][0]
            nextY = locations[i][1]

            if self.robot_loc[0] == nextX and self.robot_loc[1] == nextY:
                pg.draw.rect(menuDisplay, black,(nextX,nextY ,15,15))
                self.finishedList.append(locations[i][0])
                i = i + 1

            elif self.robot_loc[0] < nextX:
                pg.draw.rect(menuDisplay, white,(self.robot_loc[0],self.robot_loc[1],20,30))
                self.robot_loc[0] = self.robot_loc[0] + 1
                pg.draw.rect(menuDisplay, pink,(self.robot_loc[0],self.robot_loc[1],20,30))
                self.input.draw(self.screen)

            elif self.robot_loc[1] < nextY:
                pg.draw.rect(menuDisplay,white,(self.robot_loc[0],self.robot_loc[1],20,30))
                self.robot_loc[1] = self.robot_loc[1] + 1
                pg.draw.rect(menuDisplay, pink,(self.robot_loc[0],self.robot_loc[1],20,30))
                self.input.draw(self.screen)

            elif self.robot_loc[0] > nextX:
                pg.draw.rect(menuDisplay, white,(self.robot_loc[0],self.robot_loc[1],20,30))
                self.robot_loc[0] = self.robot_loc[0] - 1
                pg.draw.rect(menuDisplay, pink,(self.robot_loc[0],self.robot_loc[1],20,30))
                self.input.draw(self.screen)

            elif self.robot_loc[1] > nextY:
                pg.draw.rect(menuDisplay, white,(self.robot_loc[0],self.robot_loc[1],20,30))
                self.robot_loc[1] = self.robot_loc[1] - 1
                pg.draw.rect(menuDisplay, pink,(self.robot_loc[0],self.robot_loc[1],20,30))
                self.input.draw(self.screen)

            self.event_loop()
            # Starts the timer countdown
            pg.draw.rect(menuDisplay, green,(810,540,400, 60))
            total_seconds = self.frame_count // self.frame_rate
            total_seconds = self.start_time - (self.frame_count // self.frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
            text = font.render(output_string, True, black)
            menuDisplay.blit(text, [810, 540])
            if output_string == "Time left: 00:00":
                self.done = True
            self.frame_count += 1
            clock.tick(frame_rate)
            pg.display.flip()

            self.input.draw(self.screen)
            self.screen.blit(*self.prompt)

            pg.display.update()

        if self.colour == "red":
            self.quick_sort(self.red)
        elif self.colour == "blue":
            self.quick_sort(self.blue)
        elif self.colour == "green":
            self.quick_sort(self.green)
        elif self.colour == "pink":
            self.quick_sort(self.pink)

        self.clock.tick(self.fps)
        if self.time != 0:
            self.done = True

    def output_lists(self,i,Space):
        """Displays the list of cheapest items picked up"""
        if self.colour == "red":
            output = self.binarySearch(self.red, self.finishedList[i])
        elif self.colour == "blue":
            output = self.binarySearch(self.blue, self.finishedList[i])
        elif self.colour == "green":
            output = self.binarySearch(self.green, self.finishedList[i])
        elif self.colour == "pink":
            output = self.binarySearch(self.pink, self.finishedList[i])

        font = pg.font.SysFont("Times", 20)
        message = str(output[3]) + " | " + str(output[2])
        rend = font.render(message, True, pg.Color("black"))
        return (rend, rend.get_rect(topleft=(820,35+Space)))

    def main_loop(self):
        """ Makes the program loops and call certain function only if an event has been met"""
        i = 0



        """adds sound to the code"""
        pg.mixer.music.load('programsound.wav')
        pg.mixer.music.play(-1)
        
        space = 0
        self.random_types()
        while not self.done:
            self.event_loop()
            self.input.update()
            self.input.draw(self.screen)
            self.screen.blit(*self.prompt)

            pg.display.update()
            self.clock.tick(self.fps)
            if self.time != 0:
                self.done = True
        self.done = False
        if self.time != 0:
            self.robot_move()
            pg.draw.rect(menuDisplay , green,(810,0,450,540))
            pg.display.update()
            while i != self.num_items:
                self.prompt = self.output_lists(i,space)
                self.screen.blit(*self.prompt)
                space = space + 20
                pg.display.update()
                i = i+1
                self.done = False
                #self.main_program()
            while not self.done:
                self.event_loop()

#Sets up the start-up screen
menuDisplay.fill(white)
pg.draw.rect(menuDisplay , black,(800,0,10,600))
#Calls mainprogram function to start the game
game_intro()


pg.display.update()
pg.quit()
quit()
