from math import sqrt


def main():
    prime1 = p = int(input("Enter the first prime for the encryption: "))
    while isPrime(p) == False:
        print("The number you entered is not prime")
        p = int(input("Enter the first prime for the encryption: "))
    prime2 = q = int(input("Enter the second prime for the encryption: "))
    while isPrime(q) == False:
        print("The number you entered is not prime")
        q = int(input("Enter the second prime for the encryption: "))
    message = m = input("Enter the message you want to encrypt: ")
    semiPrime = n = p*q
    t = totient(p,q)
    c = encrypt(n,m,t)
    print(f"The encrypted message is {c}")


def isPrime(p):
    count = 0
    for i in range(2,int(sqrt(p))+1):
        if p%i == 0:
            count = count + 1
            print(i)
        else:
            continue
    if count == 0:
        return True
    else:
        return False

def totient(p,q):
    return (p-1)*(q-1)

def choosenPrime(t):
    choosen = []
    for i in range(2,t):
        if isPrime(i) == True and t%i != 0:
            choosen.append(i)
        else:
            continue
    return choosen[0]
def encrypt(n,m,t):
    if m.isdigit():
        c = m**choosenPrime(t) % n
        return c

# main()

print(choosenPrime(72))