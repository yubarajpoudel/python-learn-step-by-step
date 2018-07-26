
**Control Statements **

Decision Making
> Decision making is widely used during the programming. This is used to perform a set of operation on the basis of condition either returns true or false.

Statements and descriptions

 1. if statement
 2. if .. else statement
 3. Nested if..else statement

Example ( if statement )

    myScore = 60
    if ( myScore > 50 ) : 
    	print ("Score is greater than 50")
    	print ("Good bye!")
> This will display the output 
> Score is greater than 50 Good bye!
 
 Example ( if .. else  statement )
 

    myScore = 40
    if ( myScore > 50 ) : 
    	print ("Score is greater than 50")
    else :
	    print("Score is less than 50")
	    

> This will display the output 
> Score is less than 50

Example ( Nested if..else statement )

    myScore = 45
    if ( myScore > 50 ) : 
    	print ("Score is greater than 50")
    elif( myScore < 50 and myScore > 40):
	    print(" Score is in between 50 and 40 ")
    else :
	    print("Score is less than 50")

> This will display the output
> Score is in between 50 and 40

**Loops**
> The for loop processes each item in a sequence, so it is used with Python’s sequence data types - strings, lists, and tuples.
Each item in turn is (re-)assigned to the loop variable, and the body of the loop is executed.

The general form of a for loop is:

    for LOOP_VARIABLE in SEQUENCE:
        STATEMENTS
for loop

Example

     
    workingDays = ['Monday','TuesDay','WednesDay','ThrusDay','Friday']
    for day in workingDays:
        print(day)

Output
>  
Monday
TuesDay
WednesDay
ThrusDay
Friday

**range() function in for loop**

> The range function is actually a very powerful function when it comes to creating sequences of integers. It can take one, two, or three parameters

One parameter

range(stop)
> stop: Number of integers to generate upto the specified number(not included).

example

    for n in range(3):
        print(n)

output

> 0 1 2

Two parameter

> range(start,stop)

example

 

    for n in range(5,10):
        print(n)

output

>   5 6 7 8 9

Three Parameter

 > range(start,stop,step)

example

 

    for n in range(0,10,2):
        print(n)

output

 

> 0 2 4 6 8

**While loop**

> In Python, while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. That means, while loop tells the computer to do something as long as the condition is met.


 

    while condition :
      statement(s)

example

 

    x=0
    while(x < =5):
      print(x)
      x+=1

output

 

> 0 1 2 3 4 5
> 
> Here we have our conditional of x < =5 and x was previously declared
> and set equal to 0. So, our first item printed out was 0, which makes
> sense. Next, we increment x and ran the loop again. Of course, once a
> becomes equal to 5, we will no longer run through the loop.

**Else clause on Python while statement**

> The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won't be executed.


 

    while  condition:
        statement(s)
    else:
        statement(s)

example

 

    x = 5
    while x < =10:
      print (x )
      x = x +1
    else:
      print("Inside Else")

output

 
   

>    5
>       6
>       7
>       8
>       9
>       10
>       Inside Else

example

 

    x = 11
    while x < =10:
      print (x )
      x = x +1
    else:
      print("Inside Else")

> output
>   Inside Else

example

    x = 5
    while x < =10:
      print (x )
      x = x +1
      if x==7:
        break;
    else:
      print("Inside Else")

output

>   5 6

**Python Infinite Loop**

>We can program an infinite loop using while statement. If the condition of while loop is always True, we get an infinite loop.

example

 
> Press Ctrl + c to exit from loop

    while True:
      print ("This is an infinite Loop")


**Python Break and Continue statement**

Python break statement

>It is sometimes desirable to skip some statements inside the loop or terminate the loop immediately without checking the test expression. In such cases we can use break statements in Python. The break statement allows you to exit a loop from any point within its body, bypassing its normal termination expression.

Examples

     
    n=1
    while True:
      print (n)
      n+=1
      if n==5:
        break
    print("After Break")

Output
 

> 1 2 3 4 After Break

Python continue statement

> Continue statement works like break but instead of forcing termination, it forces the next iteration of the loop to take place and skipping the rest of the code.

Example

     
    n=0
    while n < 5:
      n+=1
      if n==3:
        continue
      print (n)
    print("Loop Over")

Output
 

> 1 2 4 5 Loop Over


for more [Read the remaining all chapters in detail  click here (https://aitoml.com)](https://aitoml.com/)


