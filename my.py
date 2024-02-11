squares_needed=lambda n,i=1:0 if n==0 else i if n<=1 else squares_needed(n//2,i+1)

print(squares_needed(235022852780276))