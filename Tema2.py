stire = "Potopul a provocat alunecări de teren, iar vânturile de peste 120 de km/h au rupt acoperișurile caselor, făcând și mai dificilă munca tehnicienilor care încearcă să pună în funcțiune rețeaua electrică a Cubei. În ultimele luni, penele de curent au devenit atât de severe, încât oamenii au rămas fără alimentele pe care le depozitaseră la rece, un dezastru într-o țară cu inflație și prețuri în creștere."
stire_1 = (stire[0:201:])
stire_2 = (stire[201::-1])
stire_1 = (stire_1.upper())
stire_1 = stire_1.strip()
stire_2 = stire_2.translate(str.maketrans("", "", ".,!"))
stire = stire_1 + stire_2
print(stire)