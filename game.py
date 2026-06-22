#word game
import random
word_bank=['instagram','python','java','kotlin','javascript','hangman','programming','developer','function','variable']
word=random.choice(word_bank)
guessed_word=['_']*len(word)
attempts=6
print("Welcome to word game!")
while attempts>0: 
    print('\n current word:'+' '.join(guessed_word))
    guess=input("guess the letter:").lower()

    if guess in word:
         for i in range(len(word)):
              if word[i]==guess:
                  guessed_word[i]=guess
         print("correct guess😃!")
    else:
        attempts-=1
        print("wrong guess 😟! attempts left:"+str(attempts))
    if '_' not in guessed_word:
        print('\n Congratulations🎉🎉!! you guessed the word😃:'+ word)
        break
if attempts==0 and '_' in guessed_word:
    print('\n You have 0 attempts💔! The word was:'+ word) 
