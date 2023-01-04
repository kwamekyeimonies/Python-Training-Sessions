full_name = "Tenkorang Daniel"
greeting = "Hello"

# F String
f_greeting = f"Good Morning, {full_name}"
print(f_greeting)

full_name= "Fiadzo Matilda"
f_greeting=f"Good Moring, {full_name}"
#The F string does not update itself when added to declared variable
print(f"Hello, {full_name}")

name ="Kwame"
user_greeting= "Hello, {}"
with_name = user_greeting.format(name)
print(with_name)
season_time="Jubilatijon"
test_name = "Dexoangle"
long_phrase = "Hello {},Toduay is {}";
formatted_string = long_phrase.format(test_name,season_time)
print(formatted_string)