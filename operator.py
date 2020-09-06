#Arithmethic operator
num1 = 32
num2 = 4

addition = num1 + num2  
subtraction = num1 - num2
mul = num1 * 2
div = num1 / 3          #vag fol with float value
div_int = num1 // 3     #vag fol with integer value
remainder = num1 % 3    #vag ses

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplecation: {mul}")
print(f"Division: {div}")
print(f"Division int: {div_int}")
print(f" Remainder: {remainder}")

#String concatenated

person_name = 'Mono'
food = "Pizza"
value = 24

concatenated = person_name + " " + food
print(concatenated)

concatenated_with_value = person_name + str(value)
print(concatenated_with_value)

print(f"Length of string: {len(concatenated)}")

