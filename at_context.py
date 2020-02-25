#AT content
#Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.

#read in data
data = open("data.csv")

#function to get at content
def what_at_content(dna):
	l = len(dna)
	a = dna.upper().count('A')
	t = dna.upper().count('T')
	return ((a+t)/l)

#name columns in data, store them in variables
for d in data:
		col = d.rstrip("\n").split(",")
		s = col[0]
		seq = col[1]
		name = col[2]
		exp = col[3]
		
		#specifies what we want
		if what_at_content(seq) < 0.5 and int(exp) > 200:
			print(name)