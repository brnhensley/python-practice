# if else statements and try catch

print("This movie has tons of naked butts, what is your age?")
age = input()
try:
    userAge = int(age)
    if userAge >= 17:
        print("Come on in and check out these butts!")
    else:
        print("Go back to kindergarden creep!")
except ValueError:
    print("That's not a number, genius.")
