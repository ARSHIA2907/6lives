import pygame
import math



pygame.init()


win = pygame.display.set_mode((450,400))
#bg image1
bgimg = pygame.image.load("5.jpg")
bgimg = pygame.transform.scale(bgimg, (450, 400)).convert_alpha()

pygame.display.set_caption("hangy")

        
                  


RADIUS = 11
GAP = 7
letters = []
startx = round((450 - (RADIUS * 2 + GAP) * 13) / 2)
starty = 320

A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y,chr(A + i),True])


# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 20)
WORD_FONT = pygame.font.SysFont('comicsans', 30)


a = []
for i in range(7):
    b = pygame.image.load("hangman" + str(i) + ".png")
    a.append(b)

    #game variables

hangman_status = 0
    #The word to be guessed from random_word import RandomWords
from random_word import RandomWords
r = RandomWords()



  

# Return a single random word
t= r.get_random_word()
word=t.upper()
    
    #the guesses list of letters
guessed=[]

FPS = 100
clock = pygame.time.Clock()
run = True


def draw():
    win.fill((255, 255, 255))
    win.blit(bgimg, (0, 0))

    #word guessing part
    display_word = ""
    
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, (0,0,0))
    win.blit(text, (210, 250))
    
    
    #1
    for letter in letters:
        x, y ,ltr,visible = letter
        if visible:
          pygame.draw.circle(win, (0, 0, 0), (x, y), RADIUS,3)
          text = LETTER_FONT.render(ltr, 1, (0,0,0))
          win.blit(text, (x - text.get_width()/2, y -text.get_height()/2))


        

        
        

    win.blit(a[hangman_status], (57, 75))
    pygame.display.update()

#define function meassage 
def display_message(message):
    pygame.time.delay(1000)
    win.fill((0,180,0))

    text = WORD_FONT.render(message, 1, (255,255,255))
    win.blit(text, (450/2 - text.get_width()/2, 400/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
#function for game over
def display_messages(messages):
    pygame.time.delay(1000)
    win.fill((190,0,0))

    text = WORD_FONT.render(messages, 1, (255,255,255))
    win.blit(text, (450/2 - text.get_width()/2, 400/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)      
#function to display no of chances left after each entry
def display_chance(m):
    pygame.time.delay(500)
    win.fill((140,100,190))

    text = WORD_FONT.render(m, 1, (255,255,255))
    win.blit(text, (450/2 - text.get_width()/2, 400/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)      


while run:
  
    clock.tick(FPS)
    
    draw()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters: 
              x, y, ltr,visible = letter
              if visible:
                dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                if dis < RADIUS:
                  letter[3]=False
                  guessed.append(ltr)
                  if ltr not in word:
                    hangman_status += 1
                  won = True
                  for letter in word:
                     if letter not in guessed:
                          won = False
                          break
        
                  if won:
                    display_message("You WON!")
                    break
                  if hangman_status == 0:
                    display_chance("6  chances left")
                    break
                  if won:
                    display_message("You WON!")
                    break  

                  if hangman_status == 1:
                    display_chance("5 more chances left")
                    break
                  if won:
                    display_message("You WON!")  
                  if hangman_status == 2:
                    display_chance("4 more chances left")
                    break 
                  if won:
                    display_message("You WON!")  
                  if hangman_status == 3:
                    display_chance("3 more chances left")
                    break
                  if won:
                    display_message("You WON!")  
                  if hangman_status == 4:
                    display_chance("2 more chances left")
                    break
                  if won:
                    display_message("You WON!") 
                  if hangman_status == 5:
                    display_chance("last chance") 
                    break
                  if won:
                    display_message("You WON!")
                    break        


                
      
    won = True
    for letter in word:
      if letter not in guessed:
        won = False
        break
        
    if won:
      display_message("You WON!")

      break
    
    
    if hangman_status == 6:
      

      display_messages("Game Over! the correct word is" +  word)
      
      break
    
    

            

              
pygame.quit()
