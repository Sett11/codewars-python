def reverse_and_combine_text(t):
    a,i,r=[i[::-1] for i in t.split(' ')],0,[]
    while i<len(a)-1:
        r.append(a[i]+a[i+1])
        i+=2
    if len(a)&1:
        r.append(a[-1])
    return a[0][::-1] if len(a)==1 else reverse_and_combine_text(' '.join(r))

print(reverse_and_combine_text('abc def gh34 434ff 55_eri 123 343'))