import math
def main():
    N = int(input().strip())
    is_prime = [True] * (N + 1)
    is_prime[0] = False
    is_prime[1] = True    
    for i in range(2, int(math.isqrt(N)) + 1):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False
    primes = []
    if N >= 1:
        primes.append('1')
    for num in range(2, N+1):
        if is_prime[num]:
            primes.append(str(num))  
    print(', '.join(primes))
if __name__ == '__main__':
    main()
