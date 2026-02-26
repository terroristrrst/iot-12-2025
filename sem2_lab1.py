def find_kth_largest(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("Некоректне значення k")

    last_max = float('inf')
    
    for _ in range(k):
        current_max = None
        
        for num in arr:
            if num < last_max:
                if current_max is None or num > current_max:
                    current_max = num
        
        last_max = current_max

    index = arr.index(last_max)
    return last_max, index