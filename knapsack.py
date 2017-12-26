# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    
    package = {}
    max_w = max(w)
    sum_w = sum(w)
    package[0] = w
    pre_package = 0
    for i in range(1,W+1):
        temp = 0
        gold = 0
        for j in w:
            
            if (j<=i) and (j in package[i-j]):
                val = sum_w - sum(package[i-j]) + j
                if val>temp:
                    temp = val
                    pre_package = i-j
                    gold = j


        backup = []
        for j in package[pre_package]:
            backup.append(j)
        if (package[pre_package]!=None) and (gold!=0):
            backup.remove(gold)
            package[i] = backup

            
        else:
            package[i] = package[i-1]
            
           
    return sum_w-sum(package[W])
    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
