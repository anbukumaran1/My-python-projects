import pygame #importing the pygame module
from sys import exit #importing the exit module from the sys module
pygame.init()#very important to always run before entering other code
screen = pygame.display.set_mode((800,400)) #creates a window of width, height
pygame.display.set_caption("The Runner Game")#it names the window the sting in it
clock = pygame.time.Clock() #it creates a clock or ablitiy to control the speed of the game
test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf',50)#it creates a font (font type,font size) none means default style

#test_surface = pygame.Surface((100,200)) #creates a plain surface
#test_surface.fill('Red') #it fills the display with a specified color
sky_surface = pygame.image.load('UltimatePygameIntro-main/graphics/Sky.png') #imports the image in specifed path
ground_surface = pygame.image.load('UltimatePygameIntro-main/graphics/Ground.png') #imports the image in specifed path
text_surface = test_font.render('The Runner',False,'Black')#it creates the surface with specifed font (text,AA,color) AA-smooth edges

while True: #entire game inside the loop
    #draw all the elements
    #update everything
    for event in pygame.event.get(): #it gets all event that is happenin100,200g  #creates a plain surfaceeg) player input, collision ,etc...
     
        if event.type == pygame.QUIT: #if the user presses the X button
            pygame.quit() #it closes the window
            quit() #it closes the program
            exit() #it closes the code 
        screen.blit(sky_surface,(0,0))#it displays the screen in main window (surface,position)
        screen.blit(ground_surface,(0,300))#it displays the screen in main window (surface,position)
        screen.blit(text_surface,(300,50))#it displays the text in main window (surface,position)
    pygame.display.update() #it updates everything inside the loop in the display   window
    clock.tick(60) #it sets 60 as frame rate
