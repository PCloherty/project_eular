# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def main():
    a=0
    b=1
    c=0
    max=4000000
    collection=[]
    even=[]

    while c < max:
        c=a+b
        if(c < max):
            print(f'{a} + {b} = {c}')
            a=b
            b=c
            collection.append(c)
        else:
            break

    print('The terms of the Fibonacci sequance are:')    
    print(collection)

    for num in collection:
        if (num % 2 == 0):
            even.append(num)
    
    print('The terms of an even Fibonacci sequance are:')    
    print(even)

    print(sum(even))

main()