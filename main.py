def pyramid(s):
    N = (s - 2) // 4
    vertices = N + 1
    edges = 2 * N
    faces = N + 1
    return (vertices, edges, faces, N)

print(pyramid(42))