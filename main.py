operator = input("Enter operation (+ - * / )")

firstop = float(input('enter original number'))
secondop = float(input('enter number'))

if operator == "+":
     answer= firstop + secondop
     print (answer)
elif operator == "-":
     answer = firstop - secondop
     print(answer)
elif operator == "*":
     answer = firstop * secondop
     print(answer)
elif operator == "/":
    answer = firstop / secondop
    print(answer)
else:
     print("Invalid/unprovided operation has been requested")