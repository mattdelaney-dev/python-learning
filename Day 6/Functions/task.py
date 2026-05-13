End = 0
sum = 0

while End == 0:
    Numbers = float(input("Number: "))
    if Numbers == 112:
        End += 1
    else:
        sum += Numbers
print(f"Sum: {sum}")