def while_loop_example():
    sum1 = 0
    count = 1
    while (count < 10):
        sum1 = sum1 + count
        count = count + 1
    print (count)#should be 10
    print (sum1)#should be 45
while_loop_example()

#second example
def for_loop_example():
    number=[765,23,56,89,14,78]
    for i in number:
        print(i)
for_loop_example()

#threee example
def for_loop_example():
    name=input("enter string: ")
    for i in range(0,len(name)):
        print(name[i])
for_loop_example()        