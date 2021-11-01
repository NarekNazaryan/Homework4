def numJewelsInStones(self, jewels: str, stones: str):
    c=0
    P=set(jewels)
    for k in stones:
        if k in P:
          c+=1
    return c