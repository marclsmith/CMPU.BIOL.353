#High low medium
#For each gene, print out a message giving the gene name and saying whether 
#its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).



#read in data
data = open("data.csv")


#function to get at content
def what_at_content(dna):
	l = len(dna)
	a = dna.upper().count('A')
	t = dna.upper().count('T')
	avg = (a+t)/l
	#specifiy what we want to say
	if avg > 0.65:
		return "high"
	elif avg < 0.45:
		return "low"
	else:
		return "medium"


#name columns in data, store them in variables
for a in data:
		col = a.rstrip("\n").split(",")
		s = col[0]
		seq = col[1]
		name = col[2]
		exp = col[3]
		
		#print with concatenations
		print(name + " has a " + what_at_content(seq) + " AT content.")