sömnbehov = ["14", "13", "12", "11.5", "11", "11", "10.5", "10", "10", "10", "9.5", "9", "9", "9", "9", "8.5", "8" ]
print("Ange ditt namn: ")
namn = str(input())
print("Ange din ålder: ")
ålder = int(input())
if ålder > 16 :
    print("Hallå " + namn + "! Enligt Vårdguidens rekomendationer behöver individer i din ålder (" + str(ålder) + "år) sova minst 8 timmar per natt.")
else :
    print("Hallå " + namn + "! Enligt Vårdguidens rekomendationer behöver individer i din ålder (" + str(ålder) + "år) sova minst " + sömnbehov[ålder-1] + " timmar per natt.")
