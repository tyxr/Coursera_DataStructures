# Uses python3
import sys

def binary_search(a, x):
    left,right = 0,len(a)
    if x<a[0] or x>a[-1]:
        return -1
    else:
        mid = round(right/2) - 1
        while(True):
            if x>a[mid]:
                if right-mid==1:
                    return -1
                else:
                    mid = mid + round((right-mid)/2)
            elif x<a[mid]:
                if mid==0:
                    return -1
                else:
                    mid=mid - round((mid-left)/2)
            elif x==a[mid]:
                return mid
            
        

        
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
