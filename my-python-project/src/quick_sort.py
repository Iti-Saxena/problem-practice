def quick_sort(arr):
    # divide and conquer
    i=-1
    j=0
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    # create left array
    for each in arr:
        if each<pivot:
            j+=1
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            j+=1
    
    return quick_sort(arr[:i+1]) + [pivot] + quick_sort(arr[j:])

