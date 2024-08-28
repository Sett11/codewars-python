from re import sub

def simple_assembler(a):
	env,i={},0
	a=[i.split() for i in a]
	while i<len(a):
		t=a[i]
		if t[0]=='mov':
			env[t[1]]=int(t[2]) if sub(r'-','',t[2]).isdigit() else env[t[2]]
			i+=1
			continue
		elif t[0]=='inc':
			env[t[1]]+=1
			i+=1
			continue
		elif t[0]=='dec':
			env[t[1]]-=1
			i+=1
			continue
		elif t[0]=='jnz':
			if t[1] in env and env[t[1]]:
				i+=int(t[2])
				continue
			elif t[1] not in env and int(t[1]):
				i+=int(t[2])
			else:
				i+=1
	return env

print(simple_assembler('''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''.splitlines()))
print(simple_assembler('''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''.splitlines()))