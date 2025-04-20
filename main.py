import os

def mkdirp(*dir):
    os.makedirs(os.path.join(*dir), exist_ok=True)

mkdirp("a", "b", "c")
