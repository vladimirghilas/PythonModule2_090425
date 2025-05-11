a = int(input("enter your number "))

if a % 3 == 0 and a % 5 == 0:
    print("FooBar")
elif a % 3 == 0:
    print("Foo")
elif a % 5 == 0:
    print("Bar")
