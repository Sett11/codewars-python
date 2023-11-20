def palindrome_chain_length(n,c=0):
    s=str(n)
    return c if s==s[::-1] else palindrome_chain_length(int(s)+int(s[::-1]),c+1)

print(palindrome_chain_length(87))