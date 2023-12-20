def print_triangle(n):
    if n <= 0:
        print("Hi 我是阿發，提醒您請輸入正整數~")
        return

    for i in range(1,n+1):
        blank = ' ' * (n-i)
        if i == 1:
            print(blank + '*' * i)
        elif i == n:
            print(blank + '*' + ' ' + '*' * (2*(i-1)-3) +' '+ '*')
        else:
            inner_blank = ' ' * (2*(i-1)-1)
            print(blank + '*' + inner_blank + '*')

n = int(input('請輸入一個數字:'))
print_triangle(n)
