meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []
portii = []

while studenti and comenzi:
    studentul = studenti.pop(0)
    comanda = comenzi.pop(0)
    tavi.pop()
    istoric_comenzi.append((studentul, comanda))
    portii.append(comanda)
    print(f'Studentul {studentul} a comandat {comanda}.')

print(istoric_comenzi)
print(f"""
S-au consumat {portii.count('papanasi')} papanasi.
S-au consumat {portii.count('ceafa')} cefe.
S-au consumat {portii.count('guias')} de guias.
""")

contor_comenzi = {
    'papanasi': portii.count('papanasi'),
    'ceafa': portii.count('ceafa'),
    'guias': portii.count('guias'),
}

print(f"S-au comandat {contor_comenzi['guias']} guias, {contor_comenzi['ceafa']} ceafa, {contor_comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi disponibile.")
print(f"Mai este ceafa: {'ceafa' in meniu}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu}.")
print(f"Mai sunt guias: {'guias' in meniu}.")

total_incasari = 0
for produs, pret in preturi:
    total_incasari += contor_comenzi[produs] * pret

produse_sub_7_lei = [item for item in preturi if item[1] <= 7]

print(f"Cantina a încasat: {total_incasari} lei.")
print(f"Produse care costă cel mult 7 lei: {produse_sub_7_lei}")