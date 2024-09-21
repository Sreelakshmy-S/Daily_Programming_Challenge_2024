# Daily Programming Challenge 2024 : Day 12
# Valid Parentheses with Multiple Types
'''
You are given a string s consisting of different types of parentheses: (), {}, and []. 
Your task is to determine whether the given string is valid.
'''
def check_valid(str: str) -> bool:
    match_dict = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in str:
        if char in match_dict.values():
            stack.append(char)
        elif char in match_dict.keys():
            if stack == [] or stack.pop() != match_dict[char]:
                return False
        else:
            return False
    return True

str = input().strip('""')
if (check_valid(str)):
    x = 'true'
else:
    x = 'false'
print(x)

# As we reach the string, if its an open parenthesis present in match_dict we push it into the stack. When we read a closing parenthesis, we check if the corresponding open parenthesis is present st the top of the stack. If yes, we pop it from the stack and continue reading the string, else we return False as the string is not valid.