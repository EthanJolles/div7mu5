# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


# zhiwehu's solution
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
#
# print(','.join(l))


# my solution
div7mul5 = [x for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]

# my test case
print(div7mul5)
for i in div7mul5:
    if i % 7 != 0 or i % 5 == 0:
        print('False')

print('True')


