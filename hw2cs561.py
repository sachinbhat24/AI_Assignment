with open('input.txt') as f:
    words = [word.strip() for word in f]	

grp_count = int(words[0])
pot_count = int(words[1])

pot_lists = [words[i+2].split(",") for i in range(pot_count)]
countries = []

dict_pot = {}
for i,row in enumerate(pot_lists):
	for j,col in enumerate(row) :
		countries.append(col)
		dict_pot[col] = 'pot_%s' % str(i+1)

country_lists = {}

for i in range(pot_count+2,pot_count+8):
	val = ""
	val = words[i].replace(":", ",")
	val = val.split(",")

	key = ""
	key = val.pop(0)
	for item in val :
		if item != "None" :
			country_lists[item] = key

def issafe(c,countries,groups,g):
	pot = dict_pot[countries[c]]
	team = country_lists[countries[c]]

	count = 0 

	for i,cty in enumerate(countries):
		if cty == countries[c] :
			pass 
		else :
			if dict_pot[cty] == pot and g == groups[i] :
				return False

			if country_lists[cty] != "UEFA" :
				if country_lists[cty] == team and g == groups[i] :
					return False

			elif country_lists[cty] == "UEFA" :
				if country_lists[cty] == team and g == groups[i] :
					count += 1

				if count == 2:
					return False

	return True

def assign_groups_util(countries,grp_count,groups,c):

	if c == len(countries) :
		return True
     
	for i in range(1,grp_count+1):

		if issafe(c,countries,groups,i):

			groups[c] = i 

			if assign_groups_util(countries,grp_count,groups,c+1) == True :
				return True

			groups[c] = 0

	return False
	
groups = []

for i in range(len(countries)):
	groups.append(0)

result = assign_groups_util(countries,grp_count,groups,0)

if result == False :
	fh = open("output.txt","w")
	fh.write("No")
	fh.close()
else:
	fh = open("output.txt","w")
	fh.write("Yes" + '\n')
	
	for i in range(1,grp_count+1):
		flag = 0
		l1 = []
		for j,elem in enumerate(groups):
			if elem == i :
				flag = 1
				l1.append(countries[j])
				l1.append(",")
		if flag == 1 :
			l1.pop()
		if flag == 0 :
			l1.append("None")
		if i != grp_count :
			l1.append("\n")
		fh.writelines(l1)

	fh.close()