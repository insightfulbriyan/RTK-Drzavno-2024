vhod = input().split(" ")
n_baloni = int(vhod[0])
n_streli = int(vhod[1])


baloni = []
while n_baloni:
	vhod = input()
	if vhod == "":
		break
	vhod = vhod.split(" ")
	baloni.append((int(vhod[0]), int(vhod[1])))
	n_baloni -= 1

while n_streli:
	vhod = input().split(" ")
	if vhod[0] == "":
		break
	vr = int(vhod[0])
	smer = vhod[1]
	while True:
		try:
			baloni.pop(list(zip(*baloni))[0 if smer == "v" else 1].index(vr)) #no pun intended
		except:
			break

	print(len(baloni))

	n_streli -= 1