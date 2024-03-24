n = int(input())
mreza = []
count = 0

def najdi_crko(polje, crka):
	indeksi = []
	for x in range(len(polje)):
		for y in range(len(polje)):
			if polje[x][y] == crka:
				indeksi.append((x, y))
	return indeksi

while n:
	vhod = input()
	if vhod == "":
		break
	mreza.append([i for i in vhod])
	n -= 1

besede = input().split(" ")
while besede:
	iskana_beseda = list(besede.pop())

	mreza_copy = mreza.copy()

	while iskana_beseda:
		iskana_crka = iskana_beseda.pop(0)

		crke = najdi_crko(mreza_copy.copy(), iskana_crka)
		for i in crke:
			mreza_copy[i[0]][i[1]] = "*"
			if iskana_beseda == []:
				count += 1
				break

			print(f"Iskana beseda: {iskana_beseda}")
			if not najdi_crko(mreza_copy, iskana_beseda[0]):
				iskana_beseda = ''
				break

			mreza_copy[i[0]][i[1]] = iskana_crka

print(count)