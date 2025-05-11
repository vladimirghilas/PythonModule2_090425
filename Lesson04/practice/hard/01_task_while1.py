n = int(input("enter your number > 0 "))
i = 2
fibonacci_num0 = 0
fibonacci_num1 = 1
fibonacci_num = 0
while i < n :
    fibonacci_num = fibonacci_num0 + fibonacci_num1
    fibonacci_num0 = fibonacci_num1
    fibonacci_num1 = fibonacci_num
    i += 1
print(fibonacci_num)