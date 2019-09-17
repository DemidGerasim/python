MAC = "AAAA:BBBB:CCCC"
MAC = MAC.replace(':','')
for i in MAC:
	if i == 'A':
		MAC = bin(int(i.replace('A','10')))
	if i == 'B':
		MAC +=  bin(int(i.replace('B', '11')))
	if i == 'C':
		MAC +=  bin(int(i.replace('C', '12')))	
print (MAC)