def draw_spider(a,b,c,d):
    p,t,n={1:"^ ^",2:"/\ /\\",3:"/╲ ╱\\",4:"╱╲ ╱╲"},{1:"( )", 2:"(( ))", 3:"((( )))"},2**b//2
    return '{0}{2}{4}{3}{1}'.format(*p[a].split(),*t[b].split(),d*n+c+d*n)

print(draw_spider(3, 3, "w", "0"))