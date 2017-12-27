bikes = ['trek','redline','giant']

first_bike = bikes[0]

last_bike = bikes[-1]

for bike in bikes:
    print (bike)

bikes.append('aravind')
bikes.append('kumar')


print "The following is range based for loop where the first one is the start and the second is end range"
squares = []
for i in range(1,11):
    squares.append(i**2)

for num in squares :
    print(num)


print "The following is using list comprehesion the first part is the body followed by the for loop"
squarescompre = [x**2 for x in range(1,11)]

for num in squarescompre:
    print num

print "The following is list splicing where the first num is the start and the last one is the end range"
first_half = squarescompre[:6]
second_half = squarescompre[6:]

print "First"
for num in first_half:
    print num

print "Second"
for num in second_half:
    print num
