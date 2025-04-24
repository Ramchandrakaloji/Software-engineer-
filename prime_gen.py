import math

class PrimeChecker:
    def is_prime(self, num):
        """
        Checks if a number is prime.
        """
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def generate_primes(self, limit):
        """
        Returns a list of all prime numbers up to 'limit'.
        """
        return [n for n in range(2, limit + 1) if self.is_prime(n)]

# Usage
checker = PrimeChecker()
prime_list = checker.generate_primes(50)
print("Prime numbers up to 50 are:", prime_list)
