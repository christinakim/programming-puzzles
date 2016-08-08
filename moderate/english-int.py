"""
given int, return the english phrase 
intput: 1234
output: one thousand two hundred thirty four

need to chunk 
"""
def int2eng(n):
    num = { 1: 'one', 2: 'two', 3: 'three', 4:'four', 5:'five', 6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',19:'nineteen', 14:,'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',20:'twenty',30:'thirty',40:'forty',  50:'fifty' 60:'sixty',70: 'seventy' 80:'eighty',90: 'ninety'}
    eng = ''
    i = 0
    string = str(n)
    for i in range(len(string):
        string[len-1]


    return eng

def main():
    n = 1234
    print int2eng(n)
if __name__ == '__main__':
    main()