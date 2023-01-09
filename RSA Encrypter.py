import math
import numpy as np

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

def linear_congruence(a, b, m):
    if b == 0:
        return 0

    if a < 0:
        a = -a
        b = -b

    b %= m
    while a > m:
        a -= m

    return (m * linear_congruence(m, -b, a) + b) // a

def valid_number(x, y, z):
    if math.gcd(x, (y - 1) * (z - 1)) == 1 and 1 < x < (y - 1) * (z - 1):
        return True
    else:
        return False    


while True:
    print('''1. Setup RSA
2. Encrypt a message
3. Decrypt a message
4. Quit''')
    answer = input("Enter your choice: ")
 
    if answer == '1':
        print("Choose 2 distinct prime numbers (p and q)")
        while True:
            p = int(input("p: "))
            q = int(input("q: "))
            if p == q:
                print("Please choose 2 different prime numbers and try again.")
            elif is_prime(p) and is_prime(q):
                break
            elif np.logical_not(is_prime(p)) and np.logical_not(is_prime(q)):
                print("Chosen values for both p and q are both not prime numbers, please try again.")
            elif np.logical_not(is_prime(q)):
                print("Chosen value for q is not a prime number, please try again")
            else:
                print("Chosen value for q is not a prime number, please try again.")
        print(f"Select an integer e such that the gcd(e, {(p - 1) * (q - 1)}) is 1 and 1 < e < {(p - 1) * (q - 1)}")
        e = int(input("e: "))
        if np.logical_not(valid_number(e, p, q)):
            print("Chosen value for e does not satisfy the conditions required, please try again.")
        else:
            d = linear_congruence(e, 1, (p - 1) * (q - 1))
            n = p * q
            print(f"Your public key is ({e}, {n})")
            print(f"Your private key is ({d}, {n})")
    elif answer == '2':
        print("What is the public key? (e, n)")
        e = int(input("e: "))
        n = int(input("n: "))
        print(f"Construct a plaintext message M, an integer such that 0 <= M < {n}")
        m = int(input("M: "))
        if np.logical_not(0 <= m < n):
            print("Chosen value for M does not satisfy the condition required, please try again.")
        else:
            c = linear_congruence(1, m ** e, n)
            print(f"Your encrypted ciphertext is {c}")
    elif answer == '3':
        print("What is your private key? (d, n):")
        d = int(input("d: "))
        n = int(input("n: "))
        print("What is the message (C) that you'd like to decrypt?")
        c = int(input("C: "))
        r = linear_congruence(1, c ** d, n)
        print(f"The decrypted message is {r}")
    elif answer == '4':
        break
    else:
        print("Invalid choice, please try again.")





            
         
    
                

