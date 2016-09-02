"""Given a list of digits, compute the possible strings of characters they could create using T9 rules.
"""

def t_nine(digits, strings =[]):
    keyboard = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'prqs', 8: 'tuv', 9: 'wxyz'}

    if len(digits) == 1:
        for i in keyboard.get(digits):
            strings.append(i)
        return strings

    else:   
        for i in digits:
            digits.pop()
            letters = keyboard.get(i)
            for letter in letters:
                for i in 

def main():
    print t_nine(234)

if __name__ == '__main__':
    main()