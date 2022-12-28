def reverse_int(x):
    rev_num=0;
    while x!=0:
        print(x)
        rem =x%10
        rev_num=(rev_num*10)+rem
        x=x//10
    
    return rev_num

print(reverse_int(10))