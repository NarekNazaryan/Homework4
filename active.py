  d = {}
   resuklt=[0]*m
    for i, j in logs:
        if i not in d:
                d[i] = [j]
         elif i in d and j not in d[i]:
                d[i].append(j)
    for m,n in d.items():
        result[len(n)-1] += 1
    return result