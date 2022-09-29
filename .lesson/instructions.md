# Blitting Images

Often we want to put other stuff on the screen not only geometric shapes. 

1.  See if you can setup Pygame on your own.  Try to import and initialize it. Set the window height and window width.  Set a caption. Setup the game loop.  Access the event and make sure i can quit the game. End the game after quitting.
```py

import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Blitting Images!")

#The main game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()

```

2.  Now we need to add images.
3.  [icon archive](iconarchive.com). Search for dragon. Make sure commercial usage is allowed if you are using your game.  64x64 px for this demo.  Make sure image is in same directory.
4.  Load image as surface object.  This loads the image in memory but does not display it. 
```py


import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Blitting Images!")


#create images...returns a surface object with the image drawn on it.  we can get the rect of the surface and use the rect to position the image. 
dragon_left_image = pygame.image.load("dragon_left.png")


#The main game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()

```

5.  Now we have to access the position coordinates.  We get the rect of the image surface.  it will have the same width and height of the image.
```py



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



#The main game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()

```
6.  Now we can position the dragon.
```py



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

#The main game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()

```
7.  Add the dragon right image.
```py




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

pygame.quit()

```

8.  Run the game.  Nothing shows
9.  Update display in game loop
```py




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

  pygame.display.update()
  
pygame.quit()

```
10. Run the game  Nothing shows.  We are not copying the image to the display this is called blitting
11. We defined the surface and we gave it a position.  now we have to copy. 
```py
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
  
  pygame.display.update()
  
pygame.quit()

```
12.  It works!
13.  As a review lets draw a white line under the dragons.

Hint:  put this below your right dragon blit and above pygame.display.update()
```py
pygame.draw.line(display_surface, (255,255,255),(0,75), (WINDOW_WIDTH, 75),4)

```

FINAL CODE FOR THIS LESSON

```py
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

```
