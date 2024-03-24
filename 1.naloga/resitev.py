#program podatke prejme iz standardnega vhoda (navaja števila dokler neka vrstica ni prazna)

from cmath import nan
import itertools 

def permutacije_stevila(stevilo):
	if isinstance(stevilo, int):
		return [stevilo]
	stevilo_moznosti = []
	cnt = stevilo.count("*")
	vse_permutacije = itertools.product('69', repeat=cnt)
	for permute in vse_permutacije:
		permute = list(permute)
		stevilo_cpy = stevilo
		while "*" in stevilo_cpy:
			stevilo_cpy = stevilo_cpy.replace("*", permute.pop(0), 1)
		stevilo_moznosti.append(int(''.join(stevilo_cpy)))

	return stevilo_moznosti


nums = []
stevila = []

while True:
	vhod = input()
	if vhod == "":
		break
	if "*" not in vhod:
		nums.append(int(vhod))
		continue
	nums.append(vhod)

i = 1
stevila.append(permutacije_stevila(nums[0])[0])
while i < len(nums):
	prejsnja = stevila[-1] 
	trenutna_moznosti = permutacije_stevila(nums[i])

	while len(trenutna_moznosti):
		if trenutna_moznosti[0] > prejsnja:
			stevila.append(trenutna_moznosti[0])
			break
		trenutna_moznosti.pop(0)

	if len(trenutna_moznosti) == 0:
		print("To ni mogoče")
		break

	i += 1

print(stevila)

'''
Podatke preberemo iz standardnega vhoda, vsako število v svojo vrstico.
S funkcijo permutacije_stevila generiramo vsa možna števila, ki bi lahko bila napisana na seznamu.
Izmed njih vedno vzamemo najmanjšo tako število, da je še vedno večje od števila, ki je na seznamu napisano pred njem.
Če takega števila ni na seznamu program javi da tak seznam ne obstaja, to lahko zagotavljamo, ker vedno izbiramo najmanjše možno število.

Program je od parametna n linearno odvisen, saj primerjamo le prejšnje število [O(n) = n], od paremta m pa je v najslabšem primeru odvisen od m^2 ker bi takrat vsa števila bila samo zvezdice,
generacija vstavkov pa ima O(x) = x^2 (kartezični produkt) [O(m) = m^2].
'''