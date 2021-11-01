 def numUnique(self,emails:List[str]):
     a=set()
     for email in emails:
         name=email[:email.index("@")]
         domain=email[email.index("@"):]
         name=name.replace(".","")
         if "+" in name:
             name=name[:name.index("+")]
         a.add(arajin.replace("."," ")+"@"+verjin )
     return len(a)
