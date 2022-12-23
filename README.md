# GeoGame
GeoGame - SGH (my first python/programming project)

#General explanation

The python project I have created is called GeoGame. It is an interactive game that has 5 different games based on geographical knowledge, and a leaderboard so it is possible to compare scores and compete with friends. 

The game has inner navigation that allows to go between the main menu, leaderboard, game explanations and games itself. 

There is one python file called GeoGame.py, that includes the main function, and many other functions, including one for each game, for games explanation, showing and updating leaderboard. Some functions are one time used just for clearer code for instance: game_mode_one, other are reaused,like update_leaderboard.

Other than that, there are 4 third sourced data bases that are used to check the geographical knowledge of the player, however, those might include mistakes or missing values, the latter taken care of by choosing different data. The data bases include different data like countries codes, capitals, sizes or distances between each other. The aim was to be able to work with pandas and use dataframes in various ways. There is also a fifth "Leaderboard" dataframe, created internally, to keep track of the scores.  

#How to run
To run the game, you need to create a folder with all the necessary databases and the GeoGame python file, then run the file. 
You will also need libraries installed: pandas, random, os, time, flagpy, matplotlib, wikipediaapi, textwrap


#More information
The program tries to provide entertaining and challenging geographical games, further explained in the program itself. Some are based on certain amounts of trials, other are available until failure. There is errors and invalid input checking, and other used libraries, like matplotlib, textwrap, random, time, wikipediaapi or flaggy. Game also uses inbuilt macOS command using os library, meaning os.system('clear'), for better and cleaner output. 


#more explanations on games and database
1- Game one is based on the "area.csv" database that has the area size of countries in km; then, you are presented with two countries, and decide which one is bigger to gain points
2- Game two is based on the "capitals.csv" database that has the data of the country with respective capital. Then, at random, you are given a country and four possible answers to choose from. 
3- Game three is based on the "distances.csv" database that has a matrix of all the countries with distances between them in km. You are supposed to guess that distance and then 

Then, database "country_codes.csv" is used to facilitate accessing dataframes and translating the codes into actual country names.

The database "Leaderboard.csv" is used to keep track of scores and winners, including top 5 scores and able to update.

Furthermore, games 4 and 5, are not based on data frame informations, but on the access to the internet, via wikipedia api, and the source text of the website, and flagpy, that downloads flags. 

The program also includes tries, exceptions, and loops to work against unintended input and do not crash, but provide error and repeat input.
