def line(boolean = False):
    if boolean == True:
        print("****************************")
    else:
        print("----------------------------")

def header(string):
    string = string.center(26)
    print("| "+ string + "  ")
         
def echo(string):
    print("| " + string)

def prompt(string):
    return input("| " + string)