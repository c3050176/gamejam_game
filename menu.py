import pygame
import sys

import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
play_img = pygame.image.load("button_images/play_img.png").convert_alpha()
#options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("button_images/quit_img.png").convert_alpha()
back_img = pygame.image.load('button_images/back_img.png').convert_alpha()
'''
video_img = pygame.image.load('button_images/button_video.png').convert_alpha()
audio_img = pygame.image.load('button_images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('button_images/button_keys.png').convert_alpha()
'''

#create button instances
play_button = button.Button(226, 300, play_img, 0.5)
#options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(226, 450, quit_img, 0.5)
back_button = button.Button(500, 450, back_img, 0.5)
'''
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
'''

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))


  '''
  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250
  '''

  if not game:
    if menu_state == "main":
      draw_text("best game ever", font, TEXT_COL, 100, 100)
      if play_button.draw(screen):
        game = True
      if quit_button.draw(screen):
        run = False
  if game:
    draw_text("insert game playing", font, TEXT_COL, 100,100)
    if back_button.draw(screen):
      game = False
  menu_state = "main"


  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()