def mult_egypt(n,p):
        resultat=0
        while n!=0:
            if n%2==1: 
                resultat+=p
            n>>=1 
            p=p+p
        return resultat

var = mult_egypt(5,3)
print(var)

