def valid_number(n):
    try:
        return (float(n) or int(float(n))==0) and len(n.split('.')[1])==2
    except:
        return False

print(valid_number("34443.33"))
print(valid_number("0.00"))
print(valid_number("34443.33a"))