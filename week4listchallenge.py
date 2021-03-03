# Black-Owned Restaurant Finder: Lists exercises

####################################################################################################
# Think about different cuisines (as many as you want) and store them in a list. Using what you
# learned in the previous exercises, write code that asks the user what cuisine they are interested
# in. If the cuisine they entered is not in the list, print the string "Please choose one of these
# cuisines: [LIST OF CUISINES HERE]".

# YOUR CODE HERE
cuisines = ['Chinese', 'American', 'Japanese', 'Vietnamese', 'Korean', 'Filipino', 'Italian', 'Mexican', 'Thai']
cuisine_choice = input("What kind of cuisine are you interested in? ")
if cuisine_choice not in cuisines:
    print("Please choose one of these cuisines:", cuisines)
    cuisine_choice = input("What kind of cuisine are you interested in? ")
else:
    print("You selected", cuisine_choice, "food.")


####################################################################################################
# Find the name of at least three black-owned restaurants nearby and store their names in a list.
# Then, print out the name of each restaurant, one line at a time.

# TIP: Use Google Maps to find nearby black-owned restaurants
# https://www.google.com/maps/search/black+owned+restaurants
# -YOUR CODE HERE
bor = ["Brown Sugar Kitchen", 'Little Skillet', "Tastebuds"]
counter = 1
for x in bor:
    print(str(counter) + ". " + x)
    counter += 1


####################################################################################################
# Take your list of restaurants from the previous challenge and print them out in a numbered list.
# Example:
# 1. <RESTAURANT 1>
# 2. <RESTAURANT 2>
# 3. <RESTAURANT 3>

# YOUR CODE HERE

####################################################################################################
# Find out how far away each restaurant is (in miles) and store those distances in another list.
# Then, print out the name of each restaurant AND how far away it is in a numbered list. Example:
# 1. <RESTAURANT 1> is 2.4 miles away
# 2. <RESTAURANT 2> is 6.8 miles away
# 3. <RESTAURANT 3> is 10.2 miles away

# YOUR CODE HERE
distances = [2.4, 6.8, 10.2]
for i in range(len(bor)):
    #print(str(i+1) + ". " + bor[i] + " is " + str(distances[i]) + " miles away.")
    print(f"{str(i+1)}. {bor[i]} is {str(distances[i])} miles away.")