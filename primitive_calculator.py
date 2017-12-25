# Uses python3
import sys

def optimal_sequence(n):
    values = [0]*(n+1)
    sequence = []
    n_steps = {1:0}
    for i in range(2,n+1):
        a = None
        b = None
        if i%3==0:
            a = n_steps[i//3]
        if i%2==0:
            b = n_steps[i//2]
        c = n_steps[i-1]
        steps = [a,b,c]
        steps_values = [i//3,i//2,i-1]
        temp = []
        for j in steps:
            if j!=None:
                temp.append(j)
        i_pre = steps_values[steps.index(min(temp))]
        n_steps[i] = n_steps[i_pre] + 1
        values[i] = i_pre

    sequence.append(n)
    for i in range(n_steps[n]):
        sequence.append(values[n])
        n = values[n]
                             
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
