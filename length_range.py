#Length range
#Print out the gene names for all genes between 90 and 110 bases long.


#read in data
data = open("data.csv")

#name columns in data, store them in variables
for a in data:
		col = a.rstrip("\n").split(",")
		s = col[0]
		seq = col[1]
		name = col[2]
		exp = col[3]
#selects for correct length		
		if len(seq) >= 90 and len(seq)<=110:
			print(name)