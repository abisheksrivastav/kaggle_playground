def fib(n):
    if n == 0:
        return 0
        # create array f[0...n]
    f = [0] * (n + 1) # create array f[0...n]
    f[0] = 0        # f[0] = 0
    f[1] = 1

    for i in range(2, n + 1): # i = 2...n
        f[i] = f[i - 1] + f[i - 2]  # f[i] = f[i-1] + f[i-2]
    return f[n]

if __name__ == '__main__':
    print(fib(1000))
    print(fib(350000))