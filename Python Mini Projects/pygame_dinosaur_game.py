#import pygame module - pygame allows you to draw images and play sounds
import pygame 
from sys import exit 

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time #this shows the time in seconds and minus the previous start time of the player
    score_surf = test_font.render(f'Score: {current_time}', False, (50,150,200))
    score_rect = score_surf.get_rect(center = (364, 50))
    screen.blit(score_surf, score_rect)   


#initiates pygame
pygame.init() 

#gives a display or a window screen - with width 800 pixels and height 400 pixels 
screen = pygame.display.set_mode((728, 455)) 

#name of the game
pygame.display.set_caption("Helen's Game")

#frame rate or how many pixels per second
clock = pygame.time.Clock()

#creating text - font, writing text on surface, blit the text surface
test_font = pygame.font.Font(None, 50) #the font, font size 
    
game_active = False
start_time = 0


#surfaces are images in pygame
ground_surface = pygame.image.load("Graphics/sky&ground_pygame.jpg") #load an image from files as a surface or background

#enemy
enemy_surface = pygame.image.load("Graphics/kimono_girl_pygame_one.png") 
enemy_rect = enemy_surface.get_rect(topleft = (500, 300))


#player
player_surf = pygame.image.load("Graphics/player_side_pygame.png")
player_rect = player_surf.get_rect(topleft = (25, 300)) #takes the player surface and draws a rectangle around it
player_gravity = 0

player_front = pygame.image.load("Graphics/player_front_pygame.png")
player_front = pygame.transform.scale2x(player_front) #scaling the image to a bigger image
player_front_rect = player_front.get_rect(center = (364, 200)) #placing the rectangle around the player in the center of the beginnign screen

game_name = test_font.render("Pixel Runner", False, (0, 0, 0))
game_name_rect = game_name.get_rect(center = (364, 100))

#the window by itself will only last a second before python shuts it down, so we use a while loop to keep the screen on forever
while True: #the True will never be False which keeps the game continuing
    for event in pygame.event.get(): # checking all possible player input and see if one of them is happening
        if event.type == pygame.QUIT: #this allows the player to quit the game
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:# 
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20
                    
            if event.type == pygame.KEYDOWN: #whether a key is pressed
                if event.key == pygame.K_SPACE and player_rect.bottom >= 360: #whether a space is pressed
                    player_gravity = -20 # this makes the player go up to imitate jumping

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #if there is player input then the game restarts again
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000) # makes the game time restart everytime player fails
    if game_active: 
        screen.blit(ground_surface,(0,0)) # putting one surface onto another surface with coordinates that specify where the surface is on the original display
        #pygame.draw.rect(screen, "#c0e8ec", text_surface_rect, 0, 10)#colors the rect specified the color pink on the surface screen
        #screen.blit(text_surface, text_surface_rect)
        
        display_score()

        enemy_rect.x -= 5 #moves the snail's rectangle to the right
        if enemy_rect.right <= 0: enemy_rect. left = 728
        screen.blit(enemy_surface, enemy_rect)
        
        player_gravity += 1
        player_rect.y += player_gravity #this moves the y axis to imitate falling
        if player_rect.bottom >= 360: player_rect.bottom = 360 #this gives a ground for the player so that it doesn't keep falling
        screen.blit(player_surf, player_rect)

        #collision
        if enemy_rect.colliderect(player_rect):
            game_active = False
            enemy_rect.left = 800
    else: #if the enemy collides with the player, then game active is False and it goes directly to the else statement which makes the screen color fill with yellow
        screen.fill((94, 129, 162))  
        screen.blit(player_front, player_front_rect)

        first_text_font = pygame.font.Font(None, 50)
        first_text = first_text_font.render("Press the space bar to start.", False, (0, 0, 0))
        first_text_rect = first_text.get_rect(center = (364, 320))
        screen.blit(first_text, first_text_rect)
        screen.blit(game_name, game_name_rect)


    pygame.display.update() #this constantly keeps the display on
    clock.tick(60) #thewhile loop should not run faster than 60 frames/sec

    