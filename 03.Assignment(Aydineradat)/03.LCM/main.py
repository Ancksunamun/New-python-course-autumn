def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b , a%b)

print("Welcom to GCD calculation program")

n1 = int(input("Plz enter your first number: "))
n2 = int(input("plz enter your second number: "))

print(n1 * n2 / gcd(n1,n2))
