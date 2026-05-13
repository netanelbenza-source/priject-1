import random

def Checking_the_input_of_level():
     stap=None
     while stap == None:
      your_choise_level = input("").lower()
      if your_choise_level == "easy" or your_choise_level== "hard" :
          return your_choise_level
           
          
 


def Checking_the_input():
    pass



def Checking_caunt_the_word():
    pass


def Checking_index_woile_count_mor_1():
    pass




def Checking_index_woile_count_mor_2():
    pass




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











def statr_game():
    status_word = ""
    Remaining_attempts = 0
    letters_he_guessed = []
    exit = 0
    caunt=0
    
    while exit == 0:
            
        if caunt==0:

            print("to start the game enter 1 ")
            print("to EXIT from the game enter any other key")

            your_choise = input("please enter yout choise")
            if your_choise != "1":
                exit += 1
                continue
        
    

            print("choise the level the game : easy or hard")
            your_choise_level = Checking_the_input_of_level()
            if your_choise_level=="easy":
                Remaining_attempts=5
            else:
                Remaining_attempts=3

            list_the_curent_game = Return_list_of_word(your_choise_level)

            the_word_for_game=random.choice(list_the_curent_game)
            caunt += 1
        
        else:
            print(f"the status word is {status_word} the Remaining_attempts is {Remaining_attempts} the letters_he_guessed {letters_he_guessed}")





        

        
        




