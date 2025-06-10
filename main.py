def decrypt(a, k):
    d = []
    def f(e, n):
        if n > k:
            return
        if isinstance(e, str):
            if n == k:
                d.insert(0, e)
                return
        else:
            for i in e:
                f(i, n+1)
    f(a, -1)
    return ''.join(d)

print(decrypt(["a", "b", ["c"], ["world", "hello"]], 0))
print(decrypt([ [  ["b"] , ["a"] ], ["world", "hello"]], 1))
print(decrypt([ ["hello", [ [], [], "hiya", ["hiii", [[["lol"]]] ] ],"hi", [ [["he", "world"] ], [ ["hi", "!" ] ] ] ] , [ ["hi", "!","lol!",["lol"] ] ]], 2))