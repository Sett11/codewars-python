def re_ordering(s):
    return ' '.join(sorted(s.split(' '),key=lambda e:e[0].isupper(),reverse=True))

print(re_ordering('jojo ddjajdiojdwo ana G nnibiial'))