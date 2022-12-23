import pandas as pd
import random
import os
import time
import flagpy as fp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import wikipediaapi
import textwrap

# global variable of leaderboard dataframe
Leaderboard = pd.DataFrame(data=pd.read_csv("Leaderboard.csv"))
Leaderboard.set_index('Leaderboard', inplace=True)


# function used to get a substring of a string
def substring_after(st, de_lim):
    return st.partition(de_lim)[2]


# shows leaderboard
def show_leaderboard():
    os.system('clear')
    print(Leaderboard.head())
    input("Press enter to go back. ")
    os.system('clear')


# function that takes the score and the game, and calls update_leaderboard
def update_leaderboard_game(score, game):
    if game == 1:
        update_leaderboard(score, 'What is bigger?', 'Scores 1')
    elif game == 2:
        update_leaderboard(score, 'Capital City', 'Scores 2')
    elif game == 3:
        update_leaderboard(score, 'Guess the distance', 'Scores 3')
    elif game == 4:
        update_leaderboard(score, 'Guess the country', 'Scores 4')
    elif game == 5:
        update_leaderboard(score, 'Whose flag is it', 'Scores 5')


# updates given columns of the dataframe leaderboard with given score + asks for the player name
def update_leaderboard(score, c1, c2):
    count = 0
    temp_name = list(Leaderboard[c1])
    temp_score = list(Leaderboard[c2])
    if min(temp_score) < score:
        print("-" * 32)
        name = input("Input your name: ")
        for i in range(5):
            if temp_score[i] > score:
                count += 1
        temp_score.insert(count, score)
        temp_name.insert(count, name)
        temp_score.pop()
        temp_name.pop()
        Leaderboard[c1] = temp_name
        Leaderboard[c2] = temp_score
        Leaderboard.to_csv('Leaderboard.csv')
        print(Leaderboard.loc[:, [c1, c2]])
    input("Press Enter to continue.")
    os.system('clear')


# next 5 functions - games themselves
# first game
def game_mode_one():
    # opens data frame
    df = pd.DataFrame(pd.read_csv("area.csv"))
    # conditions for while loops

    statement = True
    #runs until fail
    while statement:
        score = 0
        os.system('clear')
        number1 = random.randint(0, 230)
        number2 = random.randint(0, 230)
        print("What is bigger? ")
        print("Your score -> ", score)
        # prints countries given they are not the same
        if number1 != number2:
            print(df.iloc[number1]["Entity"], " vs ", df.iloc[number2]["Entity"])
            # checks for invalid input
            try:
                country = int(input("Choose 1, for the country on the left, or 2 for the country on the right: "))
                print("-" * 64)
            except ValueError:
                print("Need an integer between 1 and 2!")
                print("Please wait 2 seconds.")
                input("Press Enter to continue...")
                break
            # checks for invalid input
            if country != 1 and country != 2:
                print("Need an integer between 1 and 2!")
                print("Please wait 2 seconds.")
                input("Press Enter to continue...")
                break
            #checks the answer and count points
            if (country == 1) and (
                    float(df.iloc[number1]["Land area (sq. km)"]) > float(df.iloc[number2]["Land area (sq. km)"])):
                print("Correct!")
                score += 1
                # prints data
                print(round((float(df.iloc[number1]["Land area (sq. km)"])), 2), " vs ",
                      round(float(df.iloc[number2]["Land area (sq. km)"]), 2))
                print("Your score -> ", score)
                print("Please wait 3 seconds.")
                input("Press Enter to continue...")
            # checks the answer and count points
            elif (country == 2) and (
                    float(df.iloc[number1]["Land area (sq. km)"]) < float(df.iloc[number2]["Land area (sq. km)"])):
                print("Correct!")
                score += 1
                # prints data
                print(round((float(df.iloc[number1]["Land area (sq. km)"])), 2), " vs ",
                      round(float(df.iloc[number2]["Land area (sq. km)"]), 2))
                print("Your score -> ", score)
                print("Please wait 3 seconds.")
                input("Press Enter to continue...")

                os.system('clear')
            # checks the answer and count points
            else:
                print("Incorrect")
                # ends the loop
                statement2 = False
                print(round((float(df.iloc[number1]["Land area (sq. km)"])), 2), " vs ",
                      round(float(df.iloc[number2]["Land area (sq. km)"]), 2))
                print("Your final score! -> ", score)

                print("Please wait 3 seconds.")
                input("Press Enter to continue...")
                # saving score in the database
                update_leaderboard_game(score, 1)
                os.system('clear')
        else:
            # in case the same country was picked for both
            number2 = random.randint(0, 230)


def game_mode_two():
    # opens data frame
    df = pd.read_csv("capitals.csv", sep=',')
    df = pd.DataFrame(df)
    # while loop conditions
    statement1 = True
    #runs until fail
    while statement1:
        os.system('clear')
        score = 0
        # choosing random countries
        number1, number2, number3, number4 = random.sample(range(0, 249), 4)
        number5 = random.randint(0, 3)
        print("Capital city!")
        print("Your score -> ", score)
        temp = ""
        temp2 = []
        # making sure proposed answers are printed at random
        if number5 == 0:
            print("What is the capital of:  ", df.iloc[number1]['country'])
            temp = number1
        if number5 == 1:
            print("What is the capital of:  ", df.iloc[number2]['country'])
            temp = number2
        if number5 == 2:
            print("What is the capital of:  ", df.iloc[number3]['country'])
            temp = number3
        if number5 == 3:
            print("What is the capital of:  ", df.iloc[number4]['country'])
            temp = number4
        #prints possible options
        print(df.iloc[number1]['capital'], " ", df.iloc[number2]['capital'], " ", df.iloc[number3]['capital'], " ",
              df.iloc[number4]['capital'], " ")

        # creating list of capitals
        temp2.append(df.iloc[number1]['capital'])
        temp2.append(df.iloc[number2]['capital'])
        temp2.append(df.iloc[number3]['capital'])
        temp2.append(df.iloc[number4]['capital'])

        # input check
        try:
            country = int(input("Choose between 1 and 4:  "))
            print("-" * 64)
        except ValueError:
            print("Need an integer between 1 and 4!")
            print("Please wait 2 seconds.")
            input("Press Enter to continue...")
            break
        # input check
        if country < 1 or country > 4:
            print("Need an integer between 1 and 4!")
            print("Please wait 2 seconds.")
            input("Press Enter to continue...")
            break
        # checks the answer
        if df.iloc[temp]['capital'] == temp2[country - 1]:
            print("Correct!")
            score += 1
            print("Your score -> ", score)
            print("Please wait 2 seconds.")
            input("Press Enter to continue...")
        #checks the answer
        else:
            print("Incorrect")
            print("The answer is: ", df.iloc[temp]['capital'])
            statement2 = False
            print("Your final score! -> ", score)
            # saving score in the database
            update_leaderboard_game(score, 2)
            print("Please wait 3 seconds.")
            input("Press Enter to continue...")


def game_mode_three():
    # data frames
    os.system('clear')

    df = pd.read_csv("distances.csv", sep=',')
    df = pd.DataFrame(df)
    df.set_index("XXX", inplace=True)

    df2 = pd.read_csv("country_codes.csv", sep=',')
    df2 = pd.DataFrame(df2)

    total = 0
    #5 trials game
    for n in range(5):
        # assigning random countries for the game
        number1 = random.randint(0, 242)
        number2 = random.randint(0, 242)
        code = df2.iat[number1, 1]
        country_name = df2.iat[number1, 0]
        code2 = df2.iat[number2, 1]
        country_name2 = df2.iat[number2, 0]
        #prints question
        print("How far is: ", country_name, " from, ", country_name2)
        print("This is your attempt number: ", n + 1, ", and your total is: ", total)
        #loop for getting available correct data frame entries or redoing, or same number picked
        while True:
            # checking if data bases match if not, redo
            if code in df.index and code2 in df.index:
                guess = int(input("Guess the distance in kilometers: "))
                factual = int(df.at[code, code2])
                if guess > factual:
                    # counting score
                    add = (factual / guess) * 100
                    total += add
                    print("Your guess was : ", guess, ",  and the factual distance is: ", factual)
                    print("Your points for this round : ", add, ",  and your total: ", total)
                    print()
                    input("Press Enter to continue...")
                    os.system('clear')
                else:
                    add = (guess / factual) * 100
                    total += add
                    print("Your guess was : ", guess, ",  and the factual distance is: ", factual)
                    print("Your points for this round : ", add, ",  and your total: ", total)
                    print()
                    input("Press Enter to continue...")
                    os.system('clear')
                #stop the loop to change the score
                break
            #used in case same number picked
            else:
                number1 = random.randint(0, 242)
                number2 = random.randint(0, 242)
                code = df2.iat[number1, 1]
                country_name = df2.iat[number1, 0]
                code2 = df2.iat[number2, 1]
                country_name2 = df2.iat[number2, 0]
    # saving score in the database
    update_leaderboard_game(total, 3)


def game_mode_four():
    os.system('clear')
    statement1 = True
    total = 0
    df2 = pd.read_csv("country_codes.csv", sep=',')
    df2 = pd.DataFrame(df2)
    # wikipedia library
    wiki_wiki = wikipediaapi.Wikipedia('en')
    #game until fail, trail game
    while statement1:
        #choosing web page
        number1 = random.randint(0, 242)
        country_name = df2.iat[number1, 0]
        page_py = wiki_wiki.page(country_name)
        #choosing difficulty
        print("What level of difficulty do you choose? ")
        print("1.Easy - 600 characters.")
        print("2.Medium - 350 characters.")
        print("3.Hard - 250 characters.")
        print("4.Extreme - 100 characters.")
        choice = int(input("Choose level of difficulty: "))
        # in case of error setting n
        n = 600
        # choosing level of difficulty
        try:
            if choice == 1:
                n = 500
            elif choice == 2:
                n = 350
            elif choice == 3:
                n = 250
            elif choice == 4:
                n = 100
            else:
                print("Need between and integer between 1 and 4")

            # creating string without country name and its length
            x = page_py.summary[0:n]
            x = substring_after(x, "is a country")
            x = x.replace(country_name, '"the country "')
            # if wikipedia returns empty
            if not x:
                os.system('clear')
                print("Error: Missing wikipedia website.")

            else:
                print('Page - Summary: ...is a country')
                print('\n'.join(textwrap.wrap(x, 64)))
            #the guess
            choice2 = input("Guess the country: ")
            # checks for answer
            if choice2.lower() == country_name.lower():
                total += 1
                input("Correct, press enter to continue!")
            else:
                print("Incorrect, it was, ", country_name)
                print("Your total is: ", total)
                statement1 = False
        except ValueError:
            print("Need between and integer between 1 and 4")
    # saving score in the database
    update_leaderboard_game(total, 4)


def game_mode_five():
    os.system('clear')
    df2 = pd.read_csv("country_codes.csv", sep=',')
    df2 = pd.DataFrame(df2)
    statement = True
    total = 0
    #until fail
    while statement:
        # choosing a random country
        number1 = random.randint(0, 242)
        country = df2.iat[number1, 0]
        # printing the flag with matplotlib - lack of legends, labels etc, just axis so can differentiate white flags on white backgrounds
        img = fp.get_flag_img(country)
        img.save("myImageFile.jpg")
        img = mpimg.imread('myImageFile.jpg')
        plt.imshow(img, interpolation='none')
        frame1 = plt.gca()
        frame1.axes.get_xaxis().set_visible(False)
        frame1.axes.get_yaxis().set_visible(False)
        #unblocking the window - let it close
        plt.show(block=False)
        #waiting for button to be clicked to close window
        plt.waitforbuttonpress(0)
        plt.close('all')
        time.sleep(2)
        # answer and check
        answer = input("What is the country: ").lower()
        if answer == country.lower():
            total += 1
            input("Correct, press enter to continue!")
        else:
            print("Incorrect, it was, ", country)
            print("Your total is: ", total)
            statement = False
    # saving score in the database
    update_leaderboard_game(total, 5)


# 5 prompts for the games, explanation and menu navigation
# they are all the same, differ in explanation and game access -  comments work the same for all of these 5 functions
def game_one_prompt():
    condition = True
    #run until condition, either play or exit to the main menu
    while condition:
        print('Welcome to the "What is bigger" game mode.')
        print('In that game mode, you are given two countries,')
        print('and you need to choose which one bigger, until fail!')

        print("-" * 64)
        print("Choose 1 to continue.")
        print("Or 2 to exit.")
        # input check
        try:
            choice = int(input("Choice: "))
            #game access
            if choice == 1:
                print("-" * 64)
                game_mode_one()
            #leaving to the menu
            elif choice == 2:
                condition = False
            #input error check
            else:
                print("Need to choose an integer between 1 and 2")
        except ValueError:
            print("Need to choose an integer between 1 and 2")


def game_two_prompt():
    condition = True
    while condition:
        print('Welcome to the "Capital city" game mode.')
        print('In that game mode, you are given a country, and 4 capital cities')
        print('and you need to match the capital city with the country, until fail!')
        print("-" * 64)
        print("Choose 1 to continue.")
        print("Or 2 to exit.")
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                print("-" * 64)
                game_mode_two()
            elif choice == 2:
                condition = False
        except ValueError:
            print("Need to choose an integer between 1 and 2")


def game_three_prompt():
    condition = True
    while condition:
        print('Welcome to the "Guess distance" game mode.')
        print('In that game mode, you are given two countries, and you need to guess the distance')
        print('between them in kilometers. You have 5 pairs to get the highest score out of 500!')
        print("-" * 64)
        print("Choose 1 to continue.")
        print("Or 2 to exit.")
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                print("-" * 64)
                game_mode_three()
            elif choice == 2:
                condition = False
        except ValueError:
            print("Need to choose an integer between 1 and 2")


def game_four_prompt():
    condition = True
    while condition:
        print('Welcome to the "Guess the country" game mode.')
        print('In that game mode, you are given some wikipedia info,')
        print('and you need to guess the country until fail!')
        print("-" * 64)
        print("Choose 1 to continue.")
        print("Or 2 to exit.")
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                print("-" * 64)
                game_mode_four()
            elif choice == 2:
                condition = False
        except ValueError:
            print("Need to choose an integer between 1 and 2")


def game_five_prompt():
    condition = True
    while condition:
        print('Welcome to the "Whose flag is it" game mode.')
        print('In that game mode, you are given a flag and you need to guess')
        print('whose it is, until fail! (Please click any button to close the flag window.)')
        print("-" * 64)
        print("Choose 1 to continue.")
        print("Or 2 to exit.")
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                print("-" * 64)
                game_mode_five()
            elif choice == 2:
                condition = False
        except ValueError:
            print("Need to choose an integer between 1 and 2")


# prints the game modes
def game_modes_chooser():
    os.system('clear')
    print("The five game modes are: ")
    print("1.What is bigger")
    print("2.Capital city")
    print("3.Guess distance")
    print("4.Guess the country")
    print("5.Whose flag is it")
    print("6.Leaderboard")
    print("7.Exit")


# main function
def main():
    print("Welcome to the Geographical Game - GeoGame!")
    print("In GeoGame, you can check out your geographical knowledge in five different game types,")
    print("and challenge your friends to compete with you.  ")
    print("-" * 32)
    print("Games based on data in the 3rd party data frames - might not include all countries all correct information")

    condition = True
    # while loop for the entire navigation - entire game, until closing the program
    while condition:
        try:
            game_modes_chooser()
            choice = int(input("Choose your game type/option: "))
            if choice == 1:
                print("-" * 64)
                os.system("clear")
                game_one_prompt()
            elif choice == 2:
                print("-" * 64)
                os.system("clear")
                game_two_prompt()
            elif choice == 3:
                print("-" * 64)
                os.system("clear")
                game_three_prompt()
            elif choice == 4:
                print("-" * 64)
                os.system("clear")
                game_four_prompt()
            elif choice == 5:
                print("-" * 64)
                os.system("clear")
                game_five_prompt()
            elif choice == 6:
                print("-" * 64)
                os.system("clear")
                show_leaderboard()
            elif choice == 7:
                condition = False
            else:
                print("Need to choose an integer between 1 and 7")

        except ValueError:
            print("Need to choose an integer between 1 and 7")


# main function
main()
