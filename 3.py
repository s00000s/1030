print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

# if operation == "add":
#     result = first_number + second_number
#     print(f"Result: {result}")
# elif operation == "subtract":
#     result = first_number - second_number
#     print(f"Result: {result}")
# elif operation == "multiply":
#     result = first_number * second_number
#     print(f"Result: {result}")
# elif operation == "divide":
#     result = first_number / second_number
#     print(f"Result: {result}")
# else:
#     print("Sorry, I do not understand your request.")
if operation == "add":
    def add ():
        result = first_number + second_number
        print(f"equales {result}")
        return result
    add()
elif operation == "subtract":
    def subtract ():
        result = first_number - second_number
        print(f"results {result}")
        return result
    subtract()
elif operation == "multiple":
    def multiple ():
        result = first_number* second_number
        print(f"resultes {result}")
        return result
    multiple()
elif operation == "divide":
    def divide ():
        result = first_number / second_number
        print(f"result {result}")
        return result
    divide ()
else:
    print("Sorry, I do not understand your request. ")