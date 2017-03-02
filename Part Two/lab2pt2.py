def main():
    print(sum_primes(1))

def is_prime(x):
    if x < 2: #if negative or less than 2
        return False
    if x ==2 or x == 3 or x==5 or x == 7: #skips the obvious
        return True
    elif x%2==0 or x%3==0 or x%5==0 or x%7==0: #if its divisible of obvvious false
        return False
    else:
        for i in range(3, int(x ** 0.5) + 1, 2): #trial division
            if x % i == 0:
                return False

    return True


def get_primes(x):
    for i in range(x,2000000): #goes through 2mil
        if is_prime(i): #check if prime
            print(i)   #if its prime, print prime number


def sum_primes(x):
    sum = 0
    for i in range(x,2000000): #goes through 2mil
        if is_prime(i): #check if prime
           sum = sum + i #if prime add to sum
    return sum
main()