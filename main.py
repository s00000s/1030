import calculator

print("oprations are add subtract multiply divide")
first_input =input("enter a number ")
second_input = input("eneter in a seconcd number ")

first_number = float(first_input)
second_number =  float(second_input)

opration = input("enter in an opration ````````````````````````````")

if opration == "add":
    calculator.add(first_number,second_number)
elif opration =="subtract":
    calculator.subtract(first_number,second_number)
elif opration =="multiply":
    calculator.multiply(first_number,second_number)
elif opration =="divide":
    calculator.divide(first_number,second_number)
else:
    print("please enter in a proper oppration ")