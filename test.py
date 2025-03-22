def verifica(n,div):
    if n == div:
        return True
    if n%div == 0:
        return False
    return verifica(n,div +1)
def primo_rec(n):
    if n <= 1:
        return False
    return verifica(n,2)

def primo_ite(n):
    if n <= 1:
        return False
        
    for div in range(2,n):
        if n%div == 0:
            return False
    return True



p = [n for n in range(2,100) if all(n%div for div in range(2,n))]
print(p)
# print(list_primi)
# primi = [n for n in range(0,10) if n%2 == 0]# for i in range(2,10) if n%i != 0]
# print(primi)
