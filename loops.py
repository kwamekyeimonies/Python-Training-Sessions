#while loop
# majic_numbers={4,2,6,2,5,23,53}
# guess_num= 77

# user_input = input("would you like to play the game ? (Y/n)").lower()

# while user_input !="n":
#     user_guess = int(input("Guess a random number: "))
#     if (user_guess in majic_numbers) or (user_guess == guess_num):
#         print("You guessed correctly, Congratulations")
#         break
#     elif (abs(user_guess-guess_num)==1):
#         print("You are very close, keep on trying")
#     else:
#         print("Go and ask your grandmFather...!!!!")
        
        
#For Loop

friends =[
    "Dexoangle",
    "Kyeimonies",
    "Great_Man",
    "Danny",
    "Lil_Prophet",
    "Jexebel"
]

for friend in friends:
    print(f"Welcome {friend}")
    
numbers =[1,3,54,6,84,45,64,43,64,4,63,2,6,34]
doubled = [num *2 for num in numbers]

print(doubled)

my_friends = [
    "Sammy",
    "Samuel",
    "Soap",
    "Salmon",
    "Moon",
    "Mango",
    "Love"
]

start_s=["Kofi","Emmanuel"]

for x in my_friends:
    if x.startswith("S"):
        start_s.append(x)
        
print(start_s)