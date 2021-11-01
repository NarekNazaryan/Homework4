def beautifulnum(n):
    n=list(n)
    count=0
    for i  in range(len(n)-2):
        if n[i]=="0" and n[i+1]=="1" and n[i+2]=="0":
            n[i+2]=="1"
            count+=1
    return count

print(beautifulnum("0101010"))

