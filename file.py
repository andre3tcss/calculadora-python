n1=int(input("Digite o primeiro número:"))
n2=int(input("Digite o segundo número:"))

a = n1+n2
s = n1-n2
m = n1*n2

print("Adição:", n1, "+", n2, "=", a)
print("Subtração:", n1, "-", n2, "=", s)
print("Multiplicação:", n1, "*", n2, "=", m)

if n2 != 0:
    d = n1/n2
    print("Divisão:", n1, "/", n2, "=", d)
else:
    print("Não se pode dividir um número por 0!")