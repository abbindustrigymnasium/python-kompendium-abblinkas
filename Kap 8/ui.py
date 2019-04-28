def line(boolean = False): #funktionen line som behöver ha in ett argument, om inget argument skickas med så har funktionen standarvärdet False
    if boolean == True: #om argumentet är True
        print("****************************") #skirvs en rad av asterixer ut
    else: #annars (om det är false)
        print("----------------------------") #skrivs en rad av bindestreck ut

def header(string): #funktionen header böver ha in ett argument 
    string = string.center(26) #string blir lika med string fast centrerad, eftersom center() är en inbyggd funktion som centrerar strings
    print("| "+ string) #skriver ut en string med två tecken sen den centrerade strängen
         
def echo(string): #funktionen echo böver ha in ett argument 
    print("| " + string) #skriver ut sitt stringen den får in som argument

def prompt(string): #funktionen prompt böver ha in ett argument
    return input("| " + string) #returner en input med stringen som funktionen fick in som argument som meddelande, samt att der returnas så att man kan använda svaret senare i koden