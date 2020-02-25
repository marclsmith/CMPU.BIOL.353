#Complex condition
#Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.

#read in data
data = open("data.csv")

#name columns in data, store them in variables
for a in data:
		col = a.rstrip("\n").split(",")
		s = col[0]
		seq = col[1]
		name = col[2]
		exp = col[3]

#get first index of name and make sure it isn't DM species
		if (name[0] == 'k' or name[0] == 'h') and s != "Drosophila melanogaster":
			print(name)
		