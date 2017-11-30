#numeric functions
print(min([1, 5, 32, 4, 7, -1, -432, 4])) #takes an iterable list and returns min
print(max([4, 43, 2, 7, -4, 5, -432423, 5])) #same as min
print(abs(5)) #works for pos or neg nums
print(abs(-5))
print(sum([5,3,2,7,7,8,8,7,6,5,5,4,3,3,54])) #returns sum of iterable list

num = 543424.43234523
#2nd round argument works as 10^-x for the most accurate place
print(round(num)) #default rounds to nearest 1
print(round(num, 2)) #2nd arg if >0 tells how many decimal places
print(round(num, -1)) #rounds to tens place
print(round(num, -10)) #rounds to 10^10s place

