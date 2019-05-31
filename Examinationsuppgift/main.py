import web, ui, random #importerar filen web och ui samt biblioteket random

integer = 1
correctAnswerNum = 0
correctAnswers = 0
count = 0
numbers = list(range(25)) #array med nummer från 0-24
random.shuffle(numbers) #shufflar nummrerna i arrayen
apiEasy = web.get("https://opentdb.com/api.php?amount=25&category=18&difficulty=easy&type=multiple")["results"] #api med lätta frågor
apiHard = web.get("https://opentdb.com/api.php?amount=25&category=18&difficulty=medium&type=multiple")["results"] #api med svåra frågor
qna = [] #skapar en tom array som vi sedan ska lägga in frågor och svar och rätta svaret

def getApi(api): #funktion som lägger in värden i qna arrayen, det läggs in ett dictionary för varje plats i arrayen med fråga och svar och rätt svar
    for i in api:
        qna.append({"fråga" : i["question"], "correct" : i["correct_answer"], "incorrect" : i["incorrect_answers"]})

def getNum(): #funktion för att hämta ett index som är blir random och som bara returnas en gång
    global index #gör en global variabel av index för att vi använder den i och utanför funktionen
    index = numbers[0] #index blir första värdet
    del numbers[0] #tar bort första värdet i listan
    return index #returnar index

def getAlternatives(index): #funktion för att blanda alternativen i random ordning
    global alt #gör en global variabel av alt för att vi använder den i och utanför funktionen
    alt = [] #tom array 
    alt.append(qna[index]["correct"]) #lägger till rätta svaret i arrayen
    for i in qna[index]["incorrect"]: 
        alt.append(i) #lägger till felaktiga svaren i arrayen
    random.shuffle(alt) #shufflar värdena i arrayen
    return alt #returnerar arrayen

def isValidNumber(x, num): #funktion för att kolla om det man skickar in är ett nummer mellan vissa värden
    if (x != 0):
        try:
            float(x) #om det inte går att göra till en float är det en string, då returnas false
            if (int(x)!= 0): #nummret får inte vara 0
                if(int(x) < num): #nummret får inte vara högre än parametern num                
                    return True
            return False
        except ValueError:
            return False
    else:
        return False
def outputText(header, echo):
    ui.header(header)
    ui.echo(echo)
    ui.line()

def whatDifficulty(): #funktion för att välja svårighetsgrad
    ui.header("Difficulty")
    ui.echo("1: Easy")
    ui.echo("2: Hard")
    difficulty = ui.prompt("Answer >")
    if difficulty == "1": 
        getApi(apiEasy) #om man svarar 1 så används apin med lättare frågor
    elif difficulty == "2":
        getApi(apiHard) #om man svarar 2 så används apin med svårare frågor
    else:
        ui.echo("Invalid input, try again")
        ui.line()
        whatDifficulty() #om något annat än 1 eller 2 anges så körsfunnktionen om

def numbOfQuestions():
    global questions #gör en global variabel av questions för att vi använder den i och utanför funktionen
    ui.echo("Number of questions, 1 - 25")
    questions = ui.prompt("Answer >")
    if isValidNumber(questions, 26): #om nummret ligger mellan 1-25 returneras true från isValidNummer
        return questions  #returnerar antalet frågor som ska finnas
    else:
        ui.echo("Invalid input, try again")
        ui.line()
        numbOfQuestions() #om ett ogiltigt svar anges körs funktionen om

def replace(str): #funktion för att byta ut vissa kombinationer av tecken till vad de egentligen betyder
    str = str.replace("&lt;", "<")
    str = str.replace("&gt;", ">")
    str = str.replace("&quot;", '"')
    str = str.replace("&#039;", "'")
    #vi uppdaterar str för varje rad med de riktiga teckena
    return str #sedan returnerar vi string

ui.line()
ui.header("Frågesport")
ui.line()
whatDifficulty()
ui.line()
ui.header("Questions")
numbOfQuestions()
ui.line()
while True: #frågesporten körs tills det breakas, det breakas när antalet frågor har nåtts
    if count != int(questions): #om antalet frågor programmet har frågat inte är lika med så många frågor som ska ställas
        count += 1 #antalet gånger programmet har ställt en fråga, lägger till 1 när en ny fråga ställs
        getNum() #hämtar ett index
        ui.echo(replace(qna[index]["fråga"])) #frågar frågan
        ui.echo("Alternatives:")
        getAlternatives(index) #hämtar listan med alternativ
        for i in alt:
            if i == qna[index]["correct"]: #om alternativet är rätt svar
                correctAnswerNum = integer #sparar det rätta värdets plats
            ui.echo(replace(str(integer) + ": " + i)) #skriver ut alternativen
            integer += 1
        svar = ui.prompt("Answer >")
        if isValidNumber(svar, 5): #om svaret är mellan 1 och 4
            if alt[int(svar)-1] == alt[correctAnswerNum -1]: #om svaret är korrekt
                correctAnswers += 1 #lägger till ett poäng i minne 
                outputText("Your score: " + str(correctAnswers), "Correct! Your answer was " + str(correctAnswerNum)) #anropar funktionen outputText som skriver ut rätt eller fel samt poäng
                integer = 1
            else:
                outputText("Your score: " + str(correctAnswers), "Wrong! Correct answer was " + str(correctAnswerNum)) #anropar funktionen outputText som skriver ut rätt eller fel samt poäng
                integer = 1
        else:
            outputText("Your score: " + str(correctAnswers), "Correct! Your answer was " + str(correctAnswerNum)) #anropar funktionen outputText som skriver ut rätt eller fel samt poäng
            integer = 1
    else: #om programmet frågat lika många frågor som användaren har valt
        ui.line()
        ui.header("Your final score: " + str(correctAnswers) + "/" + questions) #skriver ut en slutgiltig poäng
        ui.header("Thank you for playing!")
        ui.line()
        break #avslutar while loopen