# 2^32
# "56757657657657665456465465" * "57657657657656757657657567" = 

# str1 = "230948239844789432"
# str2 = "2482398754392"
# Not: int(str1) * int(str2)


#     16
# *   12
#-------
#     32
#    16
#-------
#    192

def largeProduct(str1, str2):
    product = []
    i = 0
    str2 = str2[::-1]
    str1 = str1[::-1]
    total = 0 
    for i in range(len(str2)):
        carryover = 0
        for j in range(len(str1)):
            total = int(str1[j]) * int(str2[i]) + carryover
            carryover = total/10
            prod = str(total) + ("0" * j) + ("0" * i) 
            # prod[0]= "32"
            # prod[1] = "160"
            print int(prod)
            total = total + int(prod)
            product.append(prod)
            
    return total, product

def main():
    str1 = "16"
    str2 = "12"
    print largeProduct(str1, str2)
    
if __name__ == '__main__':
    main()
            
