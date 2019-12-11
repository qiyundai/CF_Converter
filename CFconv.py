def checksystem(letter):
    if letter == "C":
        degreec = input("Please type in the degree in C°: ")
        convert_ctof(int(degreec))

    elif letter == "F":
        degreef = input("Please type in the degree in F°: ")
        convert_ftoc(int(degreef))

    else:
        print("Error; please type uppercase C or F.")

def convert_ctof(degf):
    print((degf * 9/5) + 32)

def convert_ftoc(degc):
    print((degc - 32) * 5/9)

system = input("Converting from Fahrenheit or Celsius? Please type C for Celsius or F for Fahrenheit. ")

checksystem(system)