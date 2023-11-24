def printinfo(name, age = 35):
    print("name: ", name)
    print ("age ", age)
    return;
printinfo(age=50, name="miki" );
printinfo( name="miki" );

print("------------------------------")

def printme(*var_1):
    for elem in var_1:
        print(elem)
print("___")
printme()
print("____")
printme("hi","halo","hai juga")