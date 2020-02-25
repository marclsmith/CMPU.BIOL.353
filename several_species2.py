#Several species

#Print out the gene names for all genes belonging to 
#Drosophila melanogaster or Drosophila simulans.

#read in data
data = open("data.csv")

#name columns in data, store them in variables
for a in data:
		col = a.rstrip("\n").split(",")
		s = col[0]
		seq = col[1]
		name = col[2]
		exp = col[3]
		
#only print the ones we want
		if s == "Drosophila melanogaster" or s == "Drosophila simulans":
				print(name)