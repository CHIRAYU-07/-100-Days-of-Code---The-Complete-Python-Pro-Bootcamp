#1. A greeting is created for the program.
print("Welcome to the Band Name Generator \n")
print("Hello " + input("What is your name "))
#2. The user is asked for the city that they grew up in.
city=input("Enter the city you grew up into : \n")
#3. The user is asked for the name of a pet.
pet=input("Enter the name your pet : \n")
#4. Combination of the name of their city and pet is shown generating their band name.
print("Here is suggestion for your band name ~ " + city +' '+ pet )
print("The length of your 'Band Name' is = " + str(len(city+pet)))
#5. See the example at:
#   https://replit.com/@chirayu7/Band-Name-Generator#main.py
