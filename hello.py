h = "Hello World"
print(len(h))
g="victor\nmuchina"
print(g + " the second letter is" + g[1])

a=0
b=1

#while
while a < 1000:
    print(a)
    a,b= b, a+b

#if else    
input = int(input("Please enter an integer\n"))
if input < 1:
    print(0+" Any negative number is changed to zero")
elif input > 1 and input < 10:
    print("The number is {}",input)
else:
     print("The number entered is 10 or greater ")

#for

words =['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
         words.insert(1, w)

print(w)
