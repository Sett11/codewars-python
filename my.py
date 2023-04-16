CHANGE={'penny': 0.01, 'nickel': 0.05, 'dime': 0.1, 'quarter': 0.25, 'dollar': 1.0}

def change_count(c):
    c='$'+str(round(sum(list(map(lambda e:CHANGE[e], c.split()))),2))
    return c+'0' if(len(c[slice(c.find('.')+1,len(c))])==1) else c

print(change_count('quarter quarter'))