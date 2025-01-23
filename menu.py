
import pygame
import button
import gameplay

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Postal Worker Simulator")

#game variables
game = False
house = False
package = False
house1 = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
play_img = pygame.image.load("button_images/start_button.png").convert_alpha()
quit_img = pygame.image.load("button_images/quit_button.png").convert_alpha()
back_img = pygame.image.load('button_images/back_button.png').convert_alpha()
background = pygame.image.load('button_images/background.jpg').convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
title = pygame.image.load('button_images/title.png').convert_alpha()
title = pygame.transform.scale(title, (title.get_width()*0.2, title.get_height()*0.2))

house_img = pygame.image.load('button_images/house_button.png').convert_alpha()
display_img = pygame.image.load('button_images/display.png').convert_alpha()
display_img = pygame.transform.scale(display_img, (display_img.get_width()*0.2, display_img.get_height()*0.2))
question_img = pygame.image.load('button_images/question_button.png').convert_alpha()
package_img = pygame.image.load('button_images/package_button.png').convert_alpha()
back_arrow_img = pygame.image.load('button_images/back_arrow.png').convert_alpha()

house1_img = pygame.image.load('button_images/house1.png').convert_alpha()
house2_img = pygame.image.load('button_images/house2.png').convert_alpha()
house3_img = pygame.image.load('button_images/house3.png').convert_alpha()
house4_img = pygame.image.load('button_images/house4.png').convert_alpha()
house5_img = pygame.image.load('button_images/house5.png').convert_alpha()
house6_img = pygame.image.load('button_images/house6.png').convert_alpha()


neighbour_img = pygame.image.load('button_images/neighbour1.png').convert_alpha


#create button instances
play_button = button.Button(226, 300, play_img, 0.1)
quit_button = button.Button(226, 450, quit_img, 0.1)
back_button = button.Button(700, 600, back_img, 0.1)

house_button = button.Button(0, 0, house_img, 0.05)
question_button = button.Button(0, 0, question_img, 0.1)
package_button = button.Button(0, 100, package_img, 0.05)
back_arrow = button.Button(500, 500, back_arrow_img, 0.5)

house1_button = button.Button(200,150, house1_img,0.8)
house2_button = button.Button(400,150, house2_img,0.8)
house3_button = button.Button(600,150, house3_img,0.8)
house4_button = button.Button(200,350, house4_img,0.8)
house5_button = button.Button(400,350, house5_img,0.8)
house6_button = button.Button(600,350, house6_img,0.8)

#neighbour = button.Button(50,50,neighbour_img,1)







def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  #screen.fill((52, 78, 91))
  screen.blit(background, (0, 0))
  if not game:
    if menu_state == "main":
      screen.blit(title,(200,100))
      if play_button.draw(screen):
        game = True
      if quit_button.draw(screen):
        run = False

  if game:
    bg_game = pygame.image.load('button_images/street_view.jpg').convert_alpha()
    bg_game = pygame.transform.scale(bg_game, (1000, 800))
    screen.blit(bg_game, (0, 0))
    if house_button.draw(screen):
      house = True
    if back_button.draw(screen):
      game = False
    if package_button.draw(screen):
      package = True

    if house:
      if house1_button.draw(screen):
        house1 = True
      if house2_button.draw(screen):
        pass
      if house3_button.draw(screen):
        pass
      if house4_button.draw(screen):
        pass
      if house5_button.draw(screen):
        pass
      if house6_button.draw(screen):
        pass
      if back_arrow.draw(screen):
        house = False

    if package:
      screen.blit(display_img, (100, 100))
      draw_text("1 Rose Avenue", font, "black", 300, 300)
      if back_arrow.draw(screen):
        package = False

    if house1:
      default_house_img = pygame.image.load('button_images/default_house.jpg').convert_alpha()
      default_house_img = pygame.transform.scale(default_house_img, (1000, 800))
      screen.blit(default_house_img,(0,0))





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

