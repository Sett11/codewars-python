def populate_dict(k,d):
    return dict([[i,d] for i in k])

print(populate_dict(["draft", "completed"], 0))