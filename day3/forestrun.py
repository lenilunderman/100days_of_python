print('''
*******************************************************************************
____/______/______/______/______/______/______/______/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/___
*******************************************************************************
''')
print("### Welcome to the Jungle ###\n")
print("Your mission is to get out of the forest and get back to civilization safe.")

choice1 = input("You woke up in the middle of the forest, the path is dark, and you have only two options ahead of you. \nWould you like to go 'left' or 'right'? ").lower()

if choice1 == 'left':
    # Continue in the game...
    choice2 = input(
        "\nYou decided to go left and saw a bright light at the end of the forest. \nWould you like to 'wait' or 'walk' towards the light? ").lower()
    # Choice to is wait... game continue.
    if choice2 == 'wait':
        choice3 = input("You decided to wait, and a wizard came to your rescue. He tells you to pick up one tool that may save your life. \nPlease choose one tool that you would like to have:\n'gun', 'magic wand', or 'key'? ")
        if choice3 == "gun":
            print(
                "The gun had only one bullet, and you end up dying from angry cannibals. Game over!")
        elif choice3 == "magic wand":
            print("Congratulation! You used the magic wand and teleported yourself to civilization! You won the game.")
        elif choice3 == "key":
            print("The key has no magic power, it is just a key. You got lost in the forest and died from a snake bite. Game over!")
        else:
            print("You didn't choose any option correctly and got lost. Game over!")
    else:
        print("You walked towards the light too quickly and end up burning yourself. Game over!")
else:
    print("Wrong choice. You got lost with your options and lost your way. Game over!")
