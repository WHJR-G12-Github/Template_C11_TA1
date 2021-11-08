import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()

groundx=0
speed=0
# Create a class named 'Bird'

# Move the following code inside the 'Bird' class and do the following changes
# Include 'self' as the parameter inside the function
# 'bird' inside the function has to be referred to as 'self.bird'
bird=pygame.Rect(100,250,30,30)
def movedown():
    global speed
    gravity=0.2
    speed=speed+gravity
    bird.y=bird.y+speed

def moveup():
    global speed
    speed=speed-10
# Move till the previous line

# Inside the 'Bird' class, define a function to display the bird image over 'bird' rectangle

while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-550:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  # Call the 'movedown()' function using the object 'bird1' 
  
  # Call the 'display()' function using the object 'bird1'
  
  # The following line is commented as it is included inside the 'display()' function defined inside the 'Bird' class
  # screen.blit(images["bird"],bird)
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        
    
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            # Call the 'moveup()' function using the object 'bird1' 
            
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
