from statistics import mean

def are_contig_elemen_close_enough(arr, abs_error):
    return all(abs(arr[i]-arr[i+1])<=abs_error for i in range(len(arr)-1))

def simul_close_to2(arr, abs_error, count = 0):
    if are_contig_elemen_close_enough(arr,abs_error):
        return count
    k=mean(arr)
    return simul_close_to2([(i+k)/k for i in arr],abs_error,count+1)

print(simul_close_to2([12, 7, 23], pow(10, -5)))