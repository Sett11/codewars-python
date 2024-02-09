f=lambda:sorted(set(i**j+j**i for j in range(2,40) for i in range(2,40)))[:121]

print(f())