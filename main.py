import random
import hangman_art
import hangman_words
from replit import clear

stages=hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(hangman_art.logo)
guess = input('Guess a letter:').lower()

display=[]
for _ in range(len(chosen_word)):
  display+='_'
display=[guess if i==guess else '_' for i in chosen_word]
print(f"{' '.join(display)}")

lives=6

while '_' in display:
  try:
   guess = input('Guess next letter:').lower()
   clear()
   if guess in display:
       print(f'You\'ve alreagy guessed {guess}')
   print(f"{' '.join(display)}")
   for position in range(len(chosen_word)):
     letter = chosen_word[position]
     if letter == guess:
      display[position] = letter
      print(f"{' '.join(display)}")
        
  
   for i in range(len(display)):
     if '_' not in display: 
      print('you WIN!')
      break
   if guess not in chosen_word:
     print(f'You guessed {guess}, that\'s in the word, you lose a life.')
     lives-=1
     if lives==0:
      print('you lose!')
      break
   print(stages[lives])  
  

  except(NameError):
     print('wrong')
      
      
