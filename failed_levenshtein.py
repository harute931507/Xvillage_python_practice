import lcs

a ="aslkndlkasoihlkn"
b ="asdhklneldbaiubsc"


c = lcs.lcs(a,b)
print(c)
print(len(c))

print(len(a))
print(len(b))

# # But the Levenshtein distance should be 12, not ( Max(a,b) - lcs )
# a	s	 	l	k	 	n	d	l	k	a	s	o	i	h	l	k	n
# a	s	d	h	k	l	n	e	l	 	d	b	a	i	u	b	s	c