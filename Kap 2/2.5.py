import math #importerar biblioteket math

print("Hur många vill äta 2 vanliga korvar?")
korvar2 = int(input())
print("Hur många vill äta 3 vanliga korvar?")
korvar3 = int(input())
print("Hur många vill äta 2 veganska korvar?")
vkorvar2 = int(input())
print("Hur många vill äta 3 veganska korvar?")
vkorvar3 = int(input())
#frågar hur många som vill äta vad och sparar det i variabler

antalvanligafrpk = (korvar2 * 2 + korvar3 * 3)/8
antalveganskafrpk = (vkorvar2 * 2 + vkorvar3 * 3)/4
antaldrickor = korvar2 + korvar3 + vkorvar2 + vkorvar3
kostnad = antaldrickor * 13.95 + antalvanligafrpk * 20.95 + antalveganskafrpk * 34.95 
#räknar ut hur många paket vanliga respektive veganskaförpackningar man behöver köpa samt antal drickor och den totala kostnaden

print("Vanliga korvpaket : " + str(math.ceil(antalvanligafrpk)))
print("Veganska korvpaket : " + str(math.ceil(antalveganskafrpk)))
print("Dryck: " + str(antaldrickor) + "st")
print(str(kostnad) + " SEK")
#skriver ut ett meddelande där den uträknade informationen finns med