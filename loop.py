#Check even odd

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#While Loop
even_numbers = []
starting = 0
user_input = int(input("Limit:"))
while starting < user_input:
    if is_even(starting):
       even_numbers.append(starting)
    starting = starting + 1
print(f"Even numbers: {even_numbers}")
print("Finished")
print("\n")

#For Loop

grocery = ["Rice", "Potato", "Tomato", "Water", "Ginger"]
for item in grocery:
    print(item)
print("\n")

#Continue 

grocery = ["Rice", "Potato", "Tomato", "Water", "Ginger"]
for item in grocery:
    if item == "Potato":
        continue
    print(item)
print("Finished")
print("\n")

#Break

grocery = ["Rice", "Potato", "Tomato", "Water", "Ginger"]
for item in grocery:
    if item == "Potato":
        break
    print(item)
print("FInished")
print("\n")


