def greeting():
    print("Hello, user")
    
greeting()

friends=["Daniel","Kwame"]

def add_friends():
    friends_name = input("Enter your name: ")
    friendz= friends + [friends_name]
    # print(friendz)
    
add_friends() 

def quantum_entergy(work,force,distance):
    return work * force * distance

energy = quantum_entergy(45,8.9,34)
print(energy)


#Lambda Functions
#Does not have a name but used to return values, never used to perform actions

# add_lambda = lambda x,y:x+y
# (print(lambda x,y:x*y)(7,8))

def tripple(x):
    return x*3

my_sequence = [3,5,2,5]
tripplex = [tripple(x) for x in my_sequence]
# tripplex=map(tripple,my_sequence)
print(tripplex)
