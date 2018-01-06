lessThan20 =["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eightteen","NineTeen"]
tens = ["","Tens","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
hundereds = ["","Thousands","Million","Billion"]

def lessThan1000(num):
    if(num==0):
        return ""
    elif(num<20):
        return lessThan20[num]
    elif(num<100):
        return tens[num/10] + " " + lessThan1000(num%10)
    else:
        return lessThan20[num/100] + " Hundereds " + lessThan1000(num%100)

def integerToWords(inputNum):

    if(inputNum==0):
        return "Zero"

    count=0
    outstring=""
    while(inputNum>0):
        if(inputNum%1000 !=0):
            outstring = lessThan1000(inputNum%1000) + " " + hundereds[count] + outstring
        inputNum/=1000
        ++count
    return outstring


if __name__ == "__main__":
    print integerToWords(3453)
    print integerToWords(9854)
