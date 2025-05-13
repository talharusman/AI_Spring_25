def query(x):
    return -1 * (x - 7)**2 + 49 

def find_peak(N: int) -> int:
    low = 0
    high = N
    
    while low < high:
        mid = (low + high)
        if query(mid) < query(mid + 1):
            low = mid + 1
        else:
            high = mid
    return low  

N = 15
peak_index = find_peak(N)
print(f"Peak found at index {peak_index} with elevation {query(peak_index)}")
