try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter a valid age in numbers")
    age = int(input("How old are you?"))

if age >= 18:
    print(f"You can drive at age {age}.")
