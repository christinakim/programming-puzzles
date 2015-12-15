def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    if num==0: return "Zero"
    
    result = ""
    p = [""," Thousand"," Million"," Billion"]
    nums = [["","One","Two","Three","Four",
             "Five","Six","Seven","Eight","Nine"], 
            ["Ten","Eleven","Twelve","Thirteen","Fourteen",
             "Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"], 
            ["Twenty","Thirty","Forty","Fifty",
            "Sixty","Seventy","Eighty","Ninety"]
            ]
   
    i = 0
    
    while (num>0):
        part = ""
        res = num%1000

        if res != 0:
            
            tmp = res%100
            if tmp != 0:
                if tmp >= 20:
                    part += nums[2][tmp/10-2]
                    if tmp%10 > 0:
                        part += " " + nums[0][tmp%10]
                elif tmp >= 10:
                    part += nums[1][tmp%10] 
                else: 
                    part += nums[0][tmp%10] 
    
                if res/100 != 0:
                    part = nums[0][res/100] + " " + "Hundred " + part
            else: 
                part = nums[0][res/100] + " " + "Hundred"
            
            if result == "":
                result = part + p[i] + result
            else:
                result = part + p[i] + " " + result
                
        i += 1 
        num = num/1000
        
    return result

def main():
    n = 123
    assert numberToWords(n) == "One Hundred Twenty Three"
    print "test passed yo"

if __name__ == '__main__':
    main()
