# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    else:
        temp = {}
        n = len(a)
        for i in a:
            temp[i]=0
        for i in a:
            temp[i]=temp[i]+1
        value = max(temp.values())
        if value>n/2:
            return 1
        else:
            return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
