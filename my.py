def actually_really_good(f=' Nothing!',s="You know what's actually really good?"):
    return s+f if not f else s+' '+f[0].capitalize()+' and more '+f[0].lower()+'.' if len(f)==1 else s+' '+f[0].capitalize()+' and '+f[1].lower()+'.'

print(actually_really_good(['Peanut butter','beef']))