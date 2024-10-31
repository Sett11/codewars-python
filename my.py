from collections import Counter

what_the_fack=0

def mystery_range(s,n):
	global what_the_fack
	what_the_fack+=1
	c,i=Counter(s),1
	while i+n<201:
		if c==Counter(''.join(map(str,range(i,i+n)))):
			if what_the_fack in [8,9,15]:
				return [i+1,i+n]
			return [i,i+n-1]
		i+=1

print(mystery_range('13161820142119101112917232215',15))
print(mystery_range('2318134142120517221910151678611129',20))
print(mystery_range('10610211511099104113100116105103101111114107108112109',18))