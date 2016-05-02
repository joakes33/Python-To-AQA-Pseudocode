
import random,sys, os,time,copy,math

listofwords=[]

gridlist=[]
Modword=""

Newword=""

Chances=""

Attempt=False

Attempt2=False

def loadFile():
    global Listofwords
    game=int(input("Do you wish to play a normal(1) or Hard(2) game?"))
    if game ==1: 
    
        textfile="words.txt"
    elif game == 2: 
    
        textfile="wordsEXT.txt"
    else:
        print(sys.exit)
        

    with open(textfile, 'r')as f:
     doc=f.read()
     Listofwords=doc.split()


def displayFirstGrid(): 
     global Listofwords 
     global gridlist

     while len(gridlist) < len(Listofwords) - 1:
         index = random.randint(0, len(Listofwords) - 1)
         if Listofwords[index] not in gridlist:
             gridlist.append(Listofwords[index])

     if len(gridlist) == 9:
         for i in range(0, 7, 3):
             print(gridlist[i], end=" ")
             print(gridlist[i + 1], end=" ")
             print(gridlist[i + 2], end=" ")
             print()
     else:
         for i in range(0, 13, 4):
             print(gridlist[i], end=" ")
             print(gridlist[i + 1], end=" ")
             print(gridlist[i + 2], end=" ")
             print(gridlist[i + 3], end=" ")
             print()
     

def changewords():
     global Listofwords
     global gridlist
     global Newword
     global Modword

     for word in Listofwords:
         if word not in gridlist:
             Newword = word

     index = random.randint(0, len(gridlist) - 1)
     Modword = gridlist[index]
     gridlist[index] = Newword
  

def ShowSecondGrid():
     global gridlist
     

    
   
     if len(gridlist) == 9:
         for i in range(0, 7, 3):
             print(gridlist[i], end=" ")
             print(gridlist[i + 1], end=" ")
             print(gridlist[i + 2], end=" ")
             print()
     else:
          for i in range(0, 13, 4):
              print(gridlist[i], end=" ")
              print(gridlist[i + 1], end=" ")
              print(gridlist[i + 2], end=" ")
              print(gridlist[i + 3], end=" ")
              print()

 
def WipeWindow():
 os.system('cls')


def GuessWordRemoved():
    global Modword
    guessed_word = False
    counter = 0

    
    while counter < 3 and not guessed_word:
        word_guessed = input("Please enter the word you think has been removed ")
        if word_guessed == Modword:
            print("Congratulations you got that right")
            guessed_word = True
        else:
            print("Sorry that was incorrect try again")
            counter += 1
             
    return guessed_word

def GuessWordAdded():
    global Newword
    guessed_word = False
    counter = 0
    
    while counter < 3 and not guessed_word:
        word_guessed = input("Please enter the word you think has been added ")
        if word_guessed == Newword:
            print("Congratulations you got that right")
            guessed_word = True
        else:
            print("Sorry that was incorrect try again")
            counter += 1
            
    return guessed_word

def check_guesses(guessed_added, guessed_removed):
    if guessed_added and guessed_removed:
        print("Congratulations you guessed both the word removed and the word added correctly")

end = False
while not end:
    loadFile()
    displayFirstGrid()

    if len(Listofwords)> 10:
        time.sleep(30)
    else:
        time.sleep(45)
    changewords()
    WipeWindow()
    ShowSecondGrid()
    guessed_removed = GuessWordRemoved()
    guessed_added = GuessWordAdded()
    check_guesses(guessed_removed, guessed_added)
