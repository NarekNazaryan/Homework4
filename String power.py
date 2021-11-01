def powerofstring(a,k):
    if k < 0:
        c = a[:len(a) // (abs(k))]
        if a.count(c) == abs(k):
            return(c)
        else:
            return ("undefined")
    elif k > 0:
        return(a * k)
a="abc"
k=-1
print(powerofstring(a,k))
