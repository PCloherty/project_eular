#The sum of the squares of the first ten natural numbers is,
        #1²+2²+...+10²=385
#The square of the sum of the first ten natural numbers is,
        #(1+2+...+10)²=55²=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
        #3025-385=2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def main():
        #make an integer and list variable for both the sum of squares(sumSquares) and square of sums(squareSum)
        sumSquares=0
        sumSquaresList=[]
        squareSum=0
        squareSumList=[]

        #for each number up to 100 do 3 things
                #1 square the number
                #2 populate the list of sumSquaresList with the squared number
                #3 populate the list of squaredSumList with the normal number
        for i in range(1,101):
                sumSquares=i*i
                sumSquaresList.append(sumSquares)
                squaredSumList.append(i)

        #getting the answer for the sum of squares
        sumSquares=sum(sumSquaresList)
        
        #getting the answer for the square of sums
        squaredSum=sum(squaredSumList)
        squaredSum=squaredSum*squaredSum
        
        print('The sum of squares is:')
        print(sumSquares)

        print('The square of sums is:')
        print(squaredSum)

        print('The difference is:')
        if (sumSquares > squaredSum):
                print(sumSquares-squaredSum)
        else:
                print(squaredSum-sumSquares)


main()