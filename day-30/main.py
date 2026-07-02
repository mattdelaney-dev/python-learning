import os

#FileNotFound
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "a_file.txt")
# try:
#     file = open(file_path)
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open(file_path , "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"That key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

height = float(input("Hieght: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("The Height is too much..")

bmi = weight / (height ** 2)
print(bmi)