def find_employees_role(s):
    x='Does not work here!'
    try:
        a,b=s.split()
        r=[i['role'] for i in employees if i['first_name']==a and i['last_name']==b]
        return r[0] if r else x
    except:
        return x