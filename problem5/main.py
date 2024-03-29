def mean_median(array_input):
    mean=1.0
    median=1

    n=len(array_input)
    tengah=int(n/2) #index array dimulai dari 0

    # cek apakah len array tidak 0
    if n!=0:
        mean = sum(array_input)/n
        if n%2!=0:median=array_input[tengah]       
        else: median=(array_input[tengah] + array_input[tengah-1])/2
    else: 
        return None
    return (mean, median)

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)