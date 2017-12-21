# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    we_val = []
    tolweigh = 0
    we_val = list(sorted(zip(weights,values),key=lambda s: s[1]/s[0],reverse=True))
    
    i = 0
    while(tolweigh<capacity and i<len(we_val)):

        if tolweigh + we_val[i][0] < capacity:
            tolweigh = tolweigh + we_val[i][0]
            value = value + we_val[i][1]

        else:
            value = value + (capacity-tolweigh)*we_val[i][1]/we_val[i][0]
            break
        i=i+1
    return value
    


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
