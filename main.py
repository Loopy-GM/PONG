import pygame
pygame.init()

screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Pong")

#variable hold paddle position
#these go above game loop
p1x = 20
p1y = 200
p2x = 760
p2y = 200
p1Score = 0
p2Score = 0
#ball variables
bx = 400
by = 275
bVx = 5
bVy = 5
doExit = False#run game loop

clock = pygame.time.Clock()#how fast screen updates

while not doExit:
  #event queue stuff
  clock.tick(60)#set the FPS

  for event in pygame.event.get():#checks for user action
    if event.type == pygame.QUIT:#if close is clicked
      doExit = True#exit game loop

  #game logic here
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    p1y-=5
  if keys[pygame.K_s]:
    p1y+=5
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    p2y-=5
  if keys[pygame.K_DOWN]:
    p2y+=5

  #ball movement
  bx += bVx
  by += bVy
   
  #ball padle reflection left/right
  if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
    bVx *= -1
  if bx > p2x - 20 and by + 20 > p2y and by < p2y + 100:
    bVx *= -1

  #reflect off walls and change score
  if bx < 0:
    bVx *= -1
    p2Score += 1
  if bx + 20 > 800:
    bVx *= -1
    p1Score += 1

  #ground collision
  if by <= 0 or by + 20 >= 550:
        bVy *= -1
  
  #render section here
  screen.fill((0,0,0))#wipe screen black

  #draws line down middle
  pygame.draw.line(screen, (255, 255, 255), [400, 0], [400, 600], 10)

  #draw a rectangle
  pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 1)
  pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100), 1)

  #draw a circle
  pygame.draw.circle(screen, (255, 255, 255), (bx, by), 5)

  #display scores
  font = pygame.font.Font(None, 74)
  text = font.render(str(p1Score), 1, (255, 255, 255))
  screen.blit(text, (250,10))
  text = font.render(str(p2Score), 1, (255, 255, 255))
  screen.blit(text, (525,10))

  #update screen
  pygame.display.flip()

  
#END GAME LOOP

pygame.quit()
