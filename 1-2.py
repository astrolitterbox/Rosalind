s = "TTACGGATAACTAGCAAATAAGCCCAGTTTGGACAGAGTATCTTTAAGCCGCTTGCCTCGCTTAACAGGGTATTTAGAAGGCGAAAGAATATGGCCAGAGGCGATTCAAAGCCCCTATCGCCTGCATTCTTCTGAATAGCCCTTCACGCGAACCTGCGGGCCGTGGATAACACGGCCACCCCGGGGATGGACGGTTTGAAACGATTTTCTCGAGTCCGTACGTGTCCAAACCTCTGCAGGCACGTAAGAGAAGCGTCCAGCCCTATCTTCGCTGCGATGAAAGTCAGGGTCTCGCTGGCCCAGGTGGTTCACTAGTTTTCTTCCTCTTGCGCAAGCCGACGGGATTCAAAGCTGGGGGCTTATACGGTGTCTCGTTAGGACAATTGTAAAGGGCCATCGTACGACTTGTTCGACTAGAAGCGCTCCACCCCATGAGCCTATTGACGTTGAATTGTAACGCTTTACTCCAATTCAGTATCCTGGATGCGCAATTTGCTGTGAGGTTGAATCGCCAGGCTGGTCTTAAACATCCCTTTGCCACACCTGGGAGTTGCATTCTAGTAGGGGTTAAGTCATCTACGGATGTCTCGCCCCTGTAGGTAGACCGTACTTGTCCGAGTTGTTAGGAAGCTCCCAACTCGTCCTGCCGGAGCAGCCAGACTCTCGAAGATGTTCGAAATGGAGTTGTTTTCGGTCATTGATCAGCTCTAGGTCTCACATATACTGCCGGAGAAGAGCCCTACGTCCCCCAACTGTGAGGCGGTAGGGATGTACGAAGATTTCCCTCCGCCTCGTACCAGTCGATCTACCGTCGAGATACGATTTTAACACTACTATCGTTTGCGCTATTCTCCGAAGGGCTCTTAAATATCTTCAACCTACTCACCTGGCTACTAATGTATTTAAGGGCGCACCTCTGTACGCGGAGCGAAGGAGGAGCCCAGGTGTGCTTGTTAGATATCCGCCAC"

c = ""

for letter in s:
	if letter == "T":
		c+= "U"
	else:
		c+= letter

print c			
