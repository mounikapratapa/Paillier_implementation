from miller_rabin_test import is_prime
import random
def generate_prime_candidate(size):
    p = random.getrandbits(size)
    p |= (1 << size - 1) | 1
    return p
def generate_prime_numbers(size):
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(size)
    return p
def gcd(a, b):
    while b:
        return gcd(b, a%b)
    return a
def lcm(a,b):
    return (a * b) // gcd(a,b)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def L(x, n):
    return ((x-1) // n)
def keys(size):
    p = generate_prime_numbers(size)
    q = generate_prime_numbers(size)
    n =  p * q
    g =  random.getrandbits(size)
    if (gcd(g, n**2) == 1):
        g = g
    Lambda =  lcm(p-1, q-1)
    x = pow(g, Lambda, n**2)
    mu = modinv(L(x,n), n)
    return (n,g,Lambda,mu)
def enc(n,g,pt):
    r =  random.getrandbits(1024)
    c1 = pow(g, pt, n**2)
    c2 = pow(r, n, n**2)
    ct = (c1 * c2) % n**2
    return ct
def dec(n, Lambda, mu, ct):
    x = pow(ct, Lambda, n**2)
    pt = (L(x, n) * mu) % n
    return pt
def main():
    n,g,Lambda,mu = keys(1024)
    disp = input("Do you want to test for homomorphism?(y/n):")
    if(disp == 'y'):
        print("Good choice,let us have some fun!")
        p1 = input("Enter the first integer:")
        p2 = input("Enter the second integer:")
        c1 = enc(n,g,int(p1))
        c2 = enc(n,g,int(p2))
        c3 = c1 * c2
        print("Your first cipher text is:",c1)
        print("Your second cipher text is:",c2)
        print("cipher product is:", c3)
        print("Decrypting")
        message = dec(n, Lambda, mu, c3)
        print(message)
        d = input("Is this the same as plain m1 + m2?(y/n):")
        if(d == 'y'):
            print("Eureka!")
        else:
            print("Paillier Failed!")
    else:    
        pt = input("Enter the integer you want to encrypt:")
        print("Encrypting...")
        ct = enc(n,g,int(pt))
        print("Your cipher text is:",ct)
        print("Decrypting...")
        message = dec(n,Lambda,mu, ct)
        print("Here is the secret in plain text:", message)
    
main()


    


    
    
