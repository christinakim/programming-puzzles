"""Write an algorithm to determine if all of the delimiters in an expression are matched and closed.{(abc)22}[14(xyz)2] should pass
[ { ] } should fail
{ (x) } [ should fail """

def delimeter(string):
    deli = {'}': '{', ']': '[', ')':'('}
    stack = []
    for i in string:
        if i == '{' or i==  '[' or i == '(':
            stack.append(i)
        elif len(stack) > 0 and deli.get(i) == stack[-1]:
            stack.pop()
    print stack
    if len(stack) == 0:
        return True
    else:
        return False

def main():
    str1 = '{(abc)22}[14(xyz)2]'
    str2 = '[ { ] }'
    str3 = '{ (x) } ['
    assert delimeter(str1) == True
    assert delimeter(str2) == False
    assert delimeter(str3) ==  False 


if __name__ == '__main__':
    main()
