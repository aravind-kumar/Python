nums = [num for num in range(1,1000) if num%7==0]
print (nums) 

nums1 = [num for num in range(0,1000,7)]
nums1 = nums1[0:]
print (nums1)

numswith3 = [num for num in range(1,1000) if '3' in str(num)]
print (numswith3)

text="My name is aravind kumar"
print (len(text.split())-1)

vowels=['a','e','i','o','u']

withoutvowels = [char for char in text if char not in vowels]
print "".join(withoutvowels)

lessThan3 = [word for word in text.split() if len(word)<4]
print lessThan3

wordLen = {word: len(word) for word in text.split()}
print wordLen

numsDivisible =[num for i in range(2,9) if num%i==0 for num in range(2,1000)]
print numsDivisible;
