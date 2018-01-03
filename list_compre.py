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
