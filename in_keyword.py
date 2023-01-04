friends = {
    "Tenkorang",
    "Daniel",
    "Kwame",
    
}

country={
    "Ghana",
    "Dubai",
    "London",
    "USA"
}

next_country={
    "Ghana",
    "Amsterdam",
    "Cuba",
    "Usa",
    "Canada",
    "USA",
    "London",
    "Dubai"   
}

print("Daniel" in friends)
print(country in next_country)

user_country = input("Enter your country's name: ")
if user_country in next_country:
    print(f"Your country {user_country} exist")
else:
    print("Create your own world")
    
    
number = 7
user_input = input("Enter y if you want to play and n if you want to quit: ").lower()

if user_input =="y":
    user_number = int(input("Guess a number for $100: "))
    if user_number == number:
        print("Congratulations you just won $150")
    elif abs(number-user_number) ==1:
        print("You are very close")
    else:
        print("Sorry, next time guess well")
else:
    print("Bye Bye see you the next time")

