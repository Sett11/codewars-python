def word_game(grid,words,moves):
    a,curr,ind=list(map(list,grid.splitlines())),[],[]
    for i,j in moves:
        if a[i][j]!=' ':
            t=(i,j)
            if t not in ind:
                ind.append(t)
                curr.append(a[i][j])
                a[i][j]=a[i][j].upper()
                if len(curr)==4:
                    v=''.join(curr) in words
                    for k,p in ind:
                        a[k][p]=' ' if v else a[k][p].lower()
                    curr,ind=[],[]
            else:
                ind.remove(t)
                a[i][j]=a[i][j].lower()
                curr.remove(a[i][j])
    return '\n'.join([''.join(i) for i in a])

print(word_game( 'gdzuhn\nthcqyj\nantaaw\nkwzcab\nbcwwvg\nvsfjop',
['cpca', 'bjya', 'gzuz', 'ksjv', 'wgfq', 'thvh', 'wnbo', 'tncw', 'daaw'],
[(3, 3), (0, 5), (4, 1), (5, 4), (0, 3), (0, 2), (3, 2), (4, 5), (2, 4), (2, 3), (0, 1), (3, 1), (2, 4), (0, 2), (1, 1), (5, 5), (4, 0), (1, 5), (1, 4), (2, 0), (2, 0), (4, 0), (5, 0), (2, 4), (0, 2), (1, 0), (1, 1), (0, 4), (5, 0), (0, 4), (5, 2), (4, 1), (2, 5), (4, 1), (4, 0), (5, 3), (2, 0)]))