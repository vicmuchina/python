from tokenize import String
from unittest import result


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
    print(0 ," Any negative number is changed to zero")
elif input > 1 and input < 10:
    print("The number is ",input)
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

c=0

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        c = c + 1 
         # loop fell through without finding a factor
        print(c,". ",n, 'is a prime number')

def fib(n):
    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a,b = 0,1
    result = []

    while a < n :

        result.append(a)
        a,b = b,a + b
        
    return result

fib = fib(1000000)
print(fib)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = prompt
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')

            print(reminder)
 

ask_def=ask_ok("yeah")
print(ask_def)