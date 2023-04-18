def interlockable(a,b):
    a=bin(a)[2:][::-1];b=bin(b)[2:][::-1];i=0
    while i<min(len(a),len(b)):
        if(a[i]=='1' and b[i]=='1'):return False
        i+=1
    return True

print(interlockable(3,6))