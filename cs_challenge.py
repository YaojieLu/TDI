
# mean
def mean(N):
	return dp_mean(N)

def dp_mean(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2.5
    else:
        res = dp_mean(n-1)+1+1/n*(n/2)+(n-2)/n*2*((n-1)*n*(2*n-1)/6-1-(n*(n-1)/2-1))/2/((n-1)*(n-2)/2)
        return res
print(mean(20))

