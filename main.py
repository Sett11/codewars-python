from re import search, sub

def roast_legacy(s):
    s = s.lower()
    print(s)
    comp = set(["slow!", "expensive!", "manual!", "down!", "hostage!", "security!"])
    points = {"cobol": 1000, "nonobject": 500, "monolithic": 500, "fax": 100, "modem": 100, "thickclient": 50, "tape": 50, "floppy": 50, "oldschoolit": 50}
    r1 = 'These guys are already DevOps and in the Cloud and the business is happy!'
    r2 = 'Burn baby burn disco inferno {} points earned in this roasting and {} complaints resolved!'
    c = p = 0
    for i in comp:
        while search(i, s):
            c += 1
            s = sub(i, '', s, count=1)
    for i in points:
        while search(i, s):
            p += points[i]
            s = sub(i, '', s, count=1)
    return r1 if c+p == 0 else r2.format(p, c)


print(roast_legacy('expensive!NONOBJECTexpensive!NONOBJECThostage!JAVASCRIPTexpensive!DEVOPS'))