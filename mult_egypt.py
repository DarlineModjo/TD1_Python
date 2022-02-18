def mult_egypt(n,p):
        resultat=0
        while n!=0:
            if n%2==1: 
                resultat+=p
            n>>=1 
            p<<=1
        return resultat

var = mult_egypt(11,3)
print(var)

