def omit_hashtag(s,h):
    return s.replace(h,'',1)

print(omit_hashtag("Sunny day! #lta #vvv", "#lta"))