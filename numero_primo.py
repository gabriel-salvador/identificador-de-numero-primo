n = int(input("Digite um número inteiro maior do que zero (n>0): "))

n_primo = True
divisor = 2
while divisor < n and n_primo:
    if n % divisor == 0:
        n_primo = False
    divisor += 1

if n_primo and n != 1:  # 1 não é primo
    print(n, "é primo.")
else:
    print(n, "não é primo. Seus divisores são:")
    for i in range(1, n):
        if n % i == 0:
            print(i, end=" ")
        continue
