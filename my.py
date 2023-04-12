def get_status(a):
    return {'status':"busy"if a else "available"}

print(get_status(0))