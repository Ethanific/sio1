
# Un premier programme
var1 = input('Quel est votre prénom ? ')
var2 = input('Quel est votre âge ? ')
n = int (var2)


print('Bonjour', var1 )
print('Voici votre âge en base 2 :')


# Division euclidienne de N par 2
q = n // 2     #quotient
r = n % 2      #reste
print(r)

while q != 0:
    r = q % 2      #reste
    print(r)
    q = q // 2     #quotient
    

