def draw_a_cross(n):
    if n<3:
        return 'Not possible to draw cross for grids less than 3x3!'
    if n%2==0:
        return 'Centered cross not possible!'
    return '\n'.join([''.join(['x' if k==h or k+h==len(x)-1 else b for k,b in enumerate(x)]) for h,x in enumerate([[' ' for i in range(n)] for j in range(n)])])

print(draw_a_cross(2))