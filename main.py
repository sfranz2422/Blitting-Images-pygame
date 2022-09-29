import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Blitting Images!")


#create images...returns a surface object with the image drawn on it.  we can get the rect of the surface and use the rect to position the image. 
dragon_left_image = pygame.image.load("dragon_left.png")

# get the rect
dragon_left_rect = dragon_left_image.get_rect()

#position the image
dragon_left_rect.topleft = (0,0)

#load the right dragon
dragon_right_image = pygame.image.load("dragon_right.png")

# get the rect
dragon_right_rect = dragon_right_image.get_rect()

#position
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


#The main game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #blit a surface object at the given coordinates to our display.
  display_surface.blit(dragon_left_image, dragon_left_rect)

  display_surface.blit(dragon_right_image, dragon_right_rect)
  pygame.draw.line(display_surface, (255,255,255),(0,75), (WINDOW_WIDTH, 75),4)
  
  pygame.display.update()
  
pygame.quit()