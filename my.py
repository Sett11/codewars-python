def is_dd(n):
    for i in str(n):
        if(str(n).count(i)==int(i)):
            return True
    return False

print(is_dd(664444309))