# --calculate --
def calculate(text_input):
        if "+" in text_input:
            separate = text_input.split("+")
            add = int(separate[0]) + int(separate[1])
            return add
        elif "-" in text_input:
            separate = text_input.split("-")
            sub = int(separate[0]) - int(separate[1])
            return sub
        elif "*" in text_input:
            separate = text_input.split("*")
            mult = int(separate[0]) * int(separate[1])
            return mult
        elif "/" in text_input:
            separate = text_input.split("/")
            if separate[1] == "0":
                return "-Cannot divide by 0-"
            else:
                div = int(separate[0]) / int(separate[1])
                return div
        elif "~" in text_input:
            separate = text_input.split("~")
            if separate[1] == "0":
                return "-Cannot divide by 0-"
            else:
                full = int(separate[0]) // int(separate[1])
                rest = int(separate[0]) % int(separate[1])
                return full, rest

# -- numbers of calculations and output--
def how_many_calculations(number_of_input):
    num_int = int(number_of_input)
    how_many = range(0, num_int)
    for num in how_many:
        user_input = input("What do you want to calculate? ")
        result = calculate(user_input)
        if "-Cannot divide by 0-" == result:  # --divide by 0--
            print(f"{result}")
        elif "~" in user_input:
            print(f"The result is {result[0]}")
            print(f"The rest is {result[1]}")
        else:
            print(f"The answer is {result}")


print("Welcome to the Python calculator!")
query_calculations = input("How many calculations would you like to perform?: ")
number_of_calculation = how_many_calculations(query_calculations)

# test
