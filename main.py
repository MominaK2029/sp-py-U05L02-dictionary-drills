# DICTIONARIES:
# QUESTION #1:
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# Your code goes here:

phonebook["Jake"] = 938273443
phonebook.pop("Jill")
print(phonebook)



# QUESTION #2: Create a dictionary called aboutMe that contains the following keys and values: 
# name (which contains the value of your name)
# age (which contains the value of your age)
# favFood (which contains a list as its value of your favourite foods)
# hairColor (which contains the value of your hair color)
# favSubject (which contains your favourite subject)
# favSweet (which contains your favourite sweet to eat)
# favHobbies (which contains a list as its value of your favourite hobbies)
# likeCoding (which contains a bool, True if you like coding and False if you don’t like coding)
# Then, print aboutMe

about_me = {
    "name" : "Momina Alam Khan",
    "age" : "15",
    "favFood" : "Chicken",
    "hairColor" : "Black",
    "favSubject" : "Math",
    "favSweet" : "Anything I bake",
    "favHobbies" : ["Reading", "Writing", "Acting"],
    "LikeCoding" : True,
}

print(about_me)





# QUESTION #3: Create a dictionary called myPet that contains information about a pet that you want to adopt! 
# These are the keys:
# 1. name (which contains the value of your pets name)
# 2. breed (which contains the value of your pets breed)
# 3. age (which contains the value of your pets age)
# 4. noise (which contains the value of what noise your pet makes ex: woof or meow)
# 5. favActivity (which contains the value of your pets favourite activity)
# 5. favFood (which contains the value of your pets favourite food)


myPet = {
    "name" : "Rj",
    "breed" : "Maincoone",
    "age" : "2",
    "noise" : "Meow",
    "favActivity" : "Sleeping",
    "favFood" : "Catnip Plant"
}


# Then do the following:
# A. Print the dictionary
# B. Print the value of breed using the breed key
# C. Remove favFood and its value then print the dictionary
# D. Add one new key-value pair then print the dictionary
# E. Print the length of your dictionary
# F. Change the value of one existing value then print the dictionary
print(myPet)
print(myPet["breed"])
myPet.pop("favFood")
myPet["enemies"] = "Other Cats"
print(len(myPet))
myPet["enemies"] = "My dad"
print(myPet)


# QUESTION #4: Create a dictionary called heights that 5 student names (keys) and their heights (values). 
# A. Print the dictionary
# B. Print the second value
# C. Remove the last key-value pair then print the dictionary
# D. Add one new key-value pair then print the dictionary
# E. Print the length of your dictionary
# F. Change the value of one existing value then print the dictionary
heights = {
    'Momina' : "5'3",
    "Leomar" : "5'9",
    "Tylar" : "5'4",
    "Aniya" : "5'5",
    "Adiel" : "5'5",
}
print(heights)
print(heights["Leomar"])
heights.pop("Adiel")
heights["Sam"] = "5'9"
print(len(heights))
heights["Leomar"] = ".1 nano-inch"
print(heights)



