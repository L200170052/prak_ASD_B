#No10

def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    d=(b**2)-(4*a*c)
    if d<0:
        return "determinan negatif"
    return  "determinan positif"
print(selesaikanABC(5,6,7))
