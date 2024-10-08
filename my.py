from re import sub,search

def solve(s):
    if len(s)&1:
        return -1
    if search(r'\(\)',s):
        return solve(sub(r'\(\)','',s))
    r=sub(r'(\(\()|(\)\))','',s)
    return (len(s)-len(r))//2+len(r)
    

print(solve("(((())"))