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
    print(" Any negative number is changed to zero")
elif input > 1 and input < 10:
    print("The number is {}",input)
else:
     print("The number entered is 10 or greater ")

#for

words =['cat', 'window', 'defenestrate']
for w in words[0]:
    if len(w) > 6:
         words.insert(0, w)
         print(w)

print(words)

for i in range(len(h)):
    print(i,h[i])

for i in range(0,100,3):
    print(i)
    
