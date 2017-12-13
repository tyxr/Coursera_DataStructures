# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    wrong = False
    opening_brackets_stack = []
    brackets_num = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            brackets_num.append(i)
        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) != 0:
                
                b = Bracket(opening_brackets_stack[-1],i)
                ans = b.Match(next)
                if ans==False:
                    wrong=True
                    print(i+1)
                    break
                else:
                    opening_brackets_stack.pop()
                    brackets_num.pop()
            else:
                wrong=True
                print(i+1)
                break

    # Printing answer, write your code here
    if len(opening_brackets_stack)==0 and wrong==False:
        print("Success")
    elif len(opening_brackets_stack)!=0 and wrong==False:
        print(brackets_num[-1]+1)
