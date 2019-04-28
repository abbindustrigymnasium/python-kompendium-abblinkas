sömnbehov = ["14", "13", "12", "11.5", "11", "11", "10.5", "10", "10", "10", "9.5", "9", "9", "9", "9", "8.5", "8" ] #en lista med sömnbehov, listan är ordnad på så sätt att orningen är sömnbehov för ettåringar, sedan tvååringar, treåringar osv

print("Ange ditt namn: ")
namn = str(input()) #tar in input på användarens namn
print("Ange din ålder: ")
ålder = int(input()) #tar in input på användarens ålder

if ålder > 16 : #om man är 17 eller över så skriver den ut att användaren ska sova 8 timmar
    print("Hallå " + namn + "! Enligt Vårdguidens rekomendationer behöver individer i din ålder (" + str(ålder) + "år) sova minst 8 timmar per natt.")
else :
    print("Hallå " + namn + "! Enligt Vårdguidens rekomendationer behöver individer i din ålder (" + str(ålder) + "år) sova minst " + sömnbehov[ålder-1] + " timmar per natt.") #eftersom åldrarna är i storleksordning i listan så skrivar man ut ålder -1, (-1 är för att listan börjar på 0)