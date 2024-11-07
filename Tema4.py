import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print("Bine ai venit la Spanzuratoarea")
print("Cuvantul de ghicit: ", " ".join(progres))

while "_" in progres and incercari_ramase > 0:
    litera = input("Introduceti o litera: ")

    if len(litera) != 1 or not litera.isalpha():
        print("Te rog sa introduci o singura litera.")
        continue

    if litera in litere_incercate:
        print("Ai incercat deja aceasta litera!")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print("Corect! progresul tau: ", " ".join(progres))
    else:
        incercari_ramase -= 1
        print(f"Litera '{litera}' nu este in cuvant. Incercari ramase: {incercari_ramase}")

if "_" not in progres:
    print("Felicitari! Ai ghicit cuvantul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvantul era:", cuvant_de_ghicit)
