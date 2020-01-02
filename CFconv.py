convertfrom = input("Please type in the degree, then follow with C or F: ")

def convert_ctof(degf):
    print((degf * 9/5) + 32,"F°")

def convert_ftoc(degc):
    print((degc - 32) * 5/9,"C°")

if "C" in convertfrom:
    convert_ctof(float(convertfrom[:-1]))
if "F" in convertfrom:
    convert_ftoc(float(convertfrom[:-1]))
    