import pandas as pd
import numpy as np
#%%
vocab= pd.read_excel('/Users/christinepham/Desktop/GRE WORDS.xlsx')

#%%
#Create a program that will store vocabulary words.

#Program should be able to:

"""

1. Display vocab words and definitions.
2. Serve a random word in quiz mode.
3. Add new words to the database.

"""






#Code will ask user which of the above things they want to do.

def menu():
    global vocab
    while True:
        print(f"You haz {len(vocab)} wurdz in yur table.\n")
        user_input = input(
            "What would you like to do? \n"
            "a - Add word and definition to database\n"
            "s - Quiz mode; server random word\n"
            "p - Print all words in database\n"
            "q - Quit"
        )
        if user_input == 'a':
            vocab = add_word()
            continue
        elif user_input == 's':
            quiz_mode()
        elif user_input == 'p':
            print_words()
        elif user_input == 'q':
            print( " Sowwy, i haz a bolshoi tired, and am hangry, kthxbai! ")
            break


def quiz_mode():

    x = np.random.randint(0, len(vocab), 1)
    word = vocab.iloc[x]["Word"].values[0]
    definition = vocab.iloc[x]["Definition"].values[0]
    synonym = vocab.iloc[x]["Synonym"].values[0]
    print(f" What does {word.upper()} mean? ")
    user_input_2 = input("Ready for definition?, Davai.... ")
    if user_input_2 == 'yes':
        print(definition + "\n")
    elif user_input_2 != 'yes':
        print("Hooman, why you do dis and torture me? ")
"""    
    Word            harangue
    Definition      long pompous speech
    Synonym         diatribe, rant   
    Name: 6, dtype: object
"""

def add_word():
    global vocab
    word = input(" Davai word, den can i haz a cheezburger? ")
    definition = input(" Hooman, what does dis wurd mean? ")
    add_synonym = input("Hooman, do you want to add cinnamon...oh i mean synonym")
    if add_synonym == 'yes':
        synonym= input(f" What udder words mean da same thing as dis {word}?" )
    else:
        print('Davai, more learning and words and bring da coocoorooza! ')


    indexes = ["Word", "Definition", "Synonym"]
    words = [word, definition, synonym]


    new_word = pd.DataFrame(
        index=indexes,
        data=words)

    new_word = new_word.transpose()
    vocab = pd.concat([vocab, new_word], axis=0, ignore_index=True)
    return vocab


    #This function will run after the user has selected 'a' from the menu.

menu()



