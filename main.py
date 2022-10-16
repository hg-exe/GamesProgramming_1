# First Exercise
print("Harry")
print(29)

dog_name = "penny"
dog_age = 8
print(dog_name)
print(dog_age)

# Second Exercise
total_price = 0
amongus = 12
elden_ring = 60
project_grove = 20
US_tax = 1.14

total_price += (amongus + elden_ring + project_grove)
print(("Your total price is: $" + str(total_price * US_tax)))

# Third Exercise
name = "Shrek"
print("Your name is {}".format(name))

age = 12
height = 1.6867

print("Your name is {}, your age is {} and you are {:.2f} tall".format(name, age, height))

# fourth Exercise
number = int(input("Give me a number: "))
print(str(number)*4)
print(str(number * 4))

# Fifth Activity
number = float(input("Give me another number: "))
if number < 100:
    print("That’s a small number")
elif number <= 1000:
    print("That’s not a big number yet")
else:
    print("That’s what I call a big number!” ")

if number % 2 == 0:
    print("It's also an even number")
else:
    print("It's also an odd number")

