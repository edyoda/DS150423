numb = int(input('Enter no to be checked:  '))
copy_numb = numb
cp_num = numb
armstrong_no = 0

count = 0
while numb != 0 :
    count += 1
    numb //= 10

print(count)

while copy_numb != 0:
    mod = copy_numb % 10
    armstrong_no += mod ** count
    copy_numb = copy_numb//10

if armstrong_no == cp_num:
    print('The number is a Armstrong number')
else:
    print('The number is not a Armstrong number')