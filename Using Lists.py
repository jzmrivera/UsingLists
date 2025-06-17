# Empty list to store the names
nameList = []

# For loop prompting user to enter 5 names and adds to list
for i in range(5):
    name = input("Please enter a name: ")
    nameList.append(name)
    
# Empty lists to keep track of odd and even name lengths
oddList = []
evenList = []

# For loop to cycle through the names and add them to the right list
for name in nameList:
    if len(name) % 2:
        oddList.append(name)
    else:
        evenList.append(name)
        
# Prompts user if they want to know odd or even length names
selection = input("Would you like to know the odd length names or the even length names? Please select odd or even: ")

# If user selects odd the list of odd names is displayed
if selection == "odd":
    print("The odd length names are: ", oddList)
# If user selects even the list of even names is displayed
elif selection == "even":
    print("The even length names are: ", evenList)
    
# Prompts user for their name
userName = input("What is your name? ")

# Checks if the users name is in the list
if userName in nameList:
    print("You have the same name as one of my friends!")
else:
    print("I don't see your name on the list")