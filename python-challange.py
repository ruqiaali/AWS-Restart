def is_prime(n):
     if n <= 1:
         return False
     elif n == 2:
         return True
     elif n % 2 == 0:
         return False
     else: 
         for i in range(3, int(n**0.5)+1, 2):
             if n % i == 0:
                 return False
         return True


# Create a list of prime numbers
primes = [n for n in range(1, 251) if is_prime(n)]

# Display the prime numbers
for prime in primes:
    print(prime)

# Save the prime numbers to a file
with open('results.txt', 'w') as file:
     for prime in primes:
         file.write(str(prime) + '\n')