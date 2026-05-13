import random


def Checking_the_input_of_level():
     Remaining_attempts = 0
     stap = None
     while stap == None:
      your_choise_level = input("").lower()
      if your_choise_level == "easy":
          Remaining_attempts = 5
      else:
          Remaining_attempts = 3
      if your_choise_level == "easy" or your_choise_level== "hard" :
            return your_choise_level , Remaining_attempts
      print("enter only easy or hard ")
           
          
def Checking_the_input():
     stap = None
     while stap == None:
      your_choise_gass = input("").lower()
      if "z" >= your_choise_gass >= "a" and len(your_choise_gass)==1:
          return your_choise_gass
      elif len(your_choise_gass) > 1 :
          print("Enter input that contains only one character") 
      else:
          print("Enter only foreign characters")    

      
     
def Checking_count_the_word(word,leter):
    return word.count(leter)


def Checking_index_while_count_1(word,leter):
    return word.index(leter)
   
    

def Checking_index_while_count_mor_1(word, leter, counter1):
    counter_1 = -1
    indexes = []
    for i in range(counter1):
        ind = word.index(leter ,counter_1+1)
        indexes.append(ind)
        counter_1=ind
    return indexes    
        

    
def Return_list_of_word(choise):
    if choise == "easy":
        return  ["pizza",
    "coffee",
    "summer",
    "guitar",
    "yellow",
    ]
    

    return ["algorithm",
    "astronaut",
    "unbelievable",
    "knowledge",]


def filling_the_notes(status_word, the_word_for_game , gass_of_plyer ):
            count_the_word = Checking_count_the_word(the_word_for_game,gass_of_plyer)
            if count_the_word == 1:
                index_1=Checking_index_while_count_1(the_word_for_game,gass_of_plyer)
                status_word[index_1] = gass_of_plyer
                return status_word
            else:
                 index_more_1=Checking_index_while_count_mor_1(the_word_for_game,gass_of_plyer,count_the_word)
                 for item in index_more_1:
                     status_word[item] = gass_of_plyer
                 return status_word    
             

def the_menu():
    print("To START the game enter  1  ")
    print("To EXIT from the game enter any other key")


def get_status(status_word,Remaining_attempts,letters_he_guessed):
        print(f"The status word is :  {"".join(status_word)}") 
        print(f"The Remaining_attempts is : {Remaining_attempts} ")
        print(f"The letters_he_guessed is : {"".join(letters_he_guessed)} ")



def start_game():
    status_word = []
    Remaining_attempts = 0
    letters_he_guessed = []
    exit = 0
    count = 0

    while exit == 0:
        if count == 0:
            the_menu()
            your_choise = input("please enter yout choise ")
            if your_choise != "1":
                exit += 1
                continue
        
            print("choise the level the game : easy or hard")
            your_choise_level = Checking_the_input_of_level()
            Remaining_attempts = your_choise_level[1]
            list_the_curent_game = Return_list_of_word(your_choise_level[0])
            the_word_for_game = list(random.choice(list_the_curent_game))
            status_word = list(len(the_word_for_game)* "*")
            count += 1
        
        get_status(the_word_for_game,status_word,Remaining_attempts,letters_he_guessed)
        if Remaining_attempts == 0:
            print("You lost the game!!! The amount of guesses for the game has run out")
            exit += 1
            continue



        print("please enter your gass : only leter")
        gass_of_plyer = Checking_the_input()
        
        

        if gass_of_plyer in the_word_for_game:
            filling=filling_the_notes(status_word, the_word_for_game , gass_of_plyer)
            status_word = filling
           
            if status_word == the_word_for_game :
                print(f"Well done, you won the game :the word is {"".join(the_word_for_game)} ") 
                exit+=1
                continue
        else:
            if gass_of_plyer not in letters_he_guessed:
                letters_he_guessed.append(gass_of_plyer) 
                Remaining_attempts -= 1
                continue
            print("You have already selected this letter")
                   
                
start_game()






        

        
        




