from re import split

def hand(s):
    if len(s)>30:
        x=''.join(i[0].upper() for i in s.split('-') if i not in ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"])
        return s,x
    return s,s.upper().replace('-',' ')

def generate_bc(url,sep):
    #print(url,sep)
    a,r,c=url.lstrip('http://').lstrip('www.').lstrip('https://').split('/')[1:],'<a href="/">HOME</a>'+sep,'/'
    if not a or (len(a)==1 and (not a[0] or 'index.' in a[0])):
        return '<span class="active">HOME</span>'
    if a and 'index.' in a[-1]:
        a.pop()
    n=len(a)
    for i in range(n):
        if i!=n-1:
            x,y=hand(split(r'\&|\?|\=|\#',a[i])[0].split('.')[0])
            c+=x+'/'
            r+=f'<a href="{c}">{y}</a>'+sep
        else:
            a[i]=split(r'\&|\?|\=|\#',a[i])[0].split('.')[0]
            if len(a[i])>30:
                x=''.join(i[0].upper() for i in a[i].split('-') if i not in ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"])
            else:
                x=' '.join(a[i].split('-')).upper()
            r+=f'<span class="active">'+x+'</span>'
    return r

print(generate_bc("https://twitter.de/most-viewed/profiles/images/profiles/funny.htm?order=desc&filter=adult", " >>> "))
print(generate_bc('agcpartners.co.uk/with-by-the-immunity-in-or-in-pippi-eurasian-cauterization?favourite=code',  '/'))
print(generate_bc('www.agcpartners.co.uk/',  '*'))
print(generate_bc('https://agcpartners.co.uk/files/transmutation-meningitis-bioengineering-in-immunity?favourite=code','.'))
print(generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > "))
print(generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / "))
print(generate_bc("www.microsoft.com/important/confidential/docs/index.htm#top", " * "))
print(generate_bc("www.microsoft.com/docs/index.htm", " * "))
print(generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > "))
print(generate_bc("www.microsoft.com/important/confidential/docs/index.htm#top", " * "))
print(generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + "))