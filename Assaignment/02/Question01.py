def find_peak(N: int) -> int:
    x = N // 2
    while True:
        current = query(x)
        left = query(x - 1) if x - 1 >= 0 else float('-inf')
        right = query(x + 1) if x + 1 <= N else float('-inf')

        if current >= left and current >= right:
            return x
        elif right > current:
            x += 1
        else:
            x -= 1

def query(x):
    return -1 * (x - 7)**2 + 49


N = 11
print(find_peak(N))  
