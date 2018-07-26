
**Variable and data types **
Python basically has five data types

 1. Numbers
 2. List
 3. Tuple
 4. String
 5. Dictionary

**Numbers**
	
| Type 		|Format 	  | Description|
|:----------|:-----------:|:-------------:|
| int | a = 10 | Signed Integer |
| long | a = 345L | Long integers, they can also be represented in octal and hexadecimal |
|float | a = 45.67 | Floating point real values |
| complex | a = 3.14J|Contains integer in the range 0 to 255.|


**String**

> Create string variables by enclosing characters in quotes. Python uses
> single quotes ' double quotes " and triple quotes """ to denote
> literal strings. Only the triple quoted strings """ also will
> automatically continue across the end of line statement.

    firstName = 'Yubaraj'
    lastName = "poudel"
    message = """this is the literal string """

**List**

Lists are a very useful variable type in Python. A list can contain a series of values. List variables are declared by using brackets [ ] following the variable name.

    A = [ ] # This is a blank list variable
    B = [1, 23, 45, 67] # this list creates an initial list of 4 numbers.
    C = [2, 4, 'john'] # lists can contain different variable types.

**Tuple**

Tuples are a group of values like a list and are manipulated in similar ways. But, tuples are fixed in size once they are assigned. In Python the fixed size is considered immutable as compared to a list that is dynamic and mutable. Tuples are defined by parenthesis ().

    myGroup = ('Rhino', 'Grasshopper', 'Flamingo', 'Bongo')

**Dictionary**

Dictionaries in Python are lists of Key:Value pairs. This is a very powerful datatype to hold a lot of related information that can be associated through keys. The main operation of a dictionary is to extract a value based on the key name. Unlike lists, where index numbers are used, dictionaries allow the use of a key to access its members. Dictionaries can also be used to sort, iterate and compare data.

    student = {'name': 'hari', 'surname': 'pandey'}
    studnet['name'] = 'shyam'  # set the value
    print (student['name']) # print the value.
    student['roll'] = 34 # Add a new key 'roll' with the associated value
    print (student.keys()) # print out a list of keys in the dictionary
    print ('roll' in room_num) # test to see if 'roll' is in the dictionary.  This returns true.


**Operators in python**

Python language supports the following types of operators.

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

**Python Arithmetic Operators**

| Operator | Description | Example |
|:---------:|:-----------:|:-------------:|
|+ Addition|Adds values on either side of the operator.|	a + b = 30
|- Subtraction |Subtracts right hand operand from left hand operand.|	a – b = -10
|* Multiplication |	Multiplies values on either side of the operator|	a * b = 200
|/ Division |	Divides left hand operand by right hand operand |	b / a = 2
|% Modulus |	Divides left hand operand by right hand operand and returns remainder |	b % a = 0
|**  Exponent |	Performs exponential (power) calculation on operators	| a**b =10 to the power 20
|//	Floor Division|The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) |	9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0


**Python Comparison Operators**

> These operators compare the values on either sides of them and decide
> the relation among them. They are also called Relational operators.

| Operator |	Description	| Example |
|:---------:|:-------------:|:----------:|
| == | If the values of two operands are equal, then the condition becomes true.|	(a == b) is not true.|
|!=	|If values of two operands are not equal, then condition becomes true.|	(a != b) is true.|
|<>	|If values of two operands are not equal, then condition becomes true.|	(a <> b) is true. This is similar to != operator.|
|>	|If the value of left operand is greater than the value of right operand, then condition becomes true.|	(a > b) is not true.|
|<	|If the value of left operand is less than the value of right operand, then condition becomes true.|	(a < b) is true. |
|>=	|If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.|	(a >= b) is not true.|
|<=	|If the value of left operand is less than or equal to the value of right operand, then condition becomes true.|	(a <= b) is true.|

**Python Assignment Operators**
| Operators | Description | Examples |
|:---------:|:------------:|:----------:|
|   =  |  Assigns values from right side operands to left side operand |	c = a + b assigns value of a + b into c |
|+= Add AND |	It adds right operand to the left operand and assign the result to left operand |	c += a is equivalent to c = c + a |
| -= Subtract AND |	It subtracts right operand from the left operand and assign the result to left operand |	c -= a is equivalent to c = c - a |
| *= Multiply AND |	It multiplies right operand with the left operand and assign the result to left operand |	c *= a is equivalent to c = c * a |
| /= Divide AND |	It divides left operand with the right operand and assign the result to left operand | 	c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a
| %= Modulus AND |	It takes modulus using two operands and assign the result to left operand	c %= a is equivalent to c = c % a |
| **= Exponent AND |	Performs exponential (power) calculation on operators and assign value to the left operand | 	c **= a is equivalent to c = c ** a |
| //= Floor Division |	It performs floor division on operators and assign value to the left operand | c //= a is equivalent to c = c // a |

**Python Bitwise Operators**

Bitwise operator works on bits and performs bit by bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows −

    a = 0011 1100
    
    b = 0000 1101
    
    -----------------
    
    a&b = 0000 1100
    
    a|b = 0011 1101
    
    a^b = 0011 0001
    
    ~a  = 1100 0011

There are following Bitwise operators supported by Python language

| Operator |	Description |	Example |
|:----------:|:---------------:|:---------------:|
|& Binary AND |	Operator copies a bit to the result if it exists in both operands	(a & b) (means 0000 1100)|
| Binary OR |	It copies a bit if it exists in either operand. |	(a \| b) = 61 (means 0011 1101) |
| ^ Binary XOR |	It copies the bit if it is set in one operand but not both. |	(a ^ b) = 49 (means 0011 0001)
|~ Binary Ones Complement|	It is unary and has the effect of 'flipping' bits.	| (~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
|<< Binary Left Shift |	The left operands value is moved left by the number of bits specified by the right operand. |	a << 2 = 240 (means 1111 0000)
| \>> Binary Right Shift	| The left operands value is moved right by the number of bits specified by the right operand. |	a >> 2 = 15 (means 0000 1111)

**Python Logical Operators**

| Operator |	Description |	Example |
|:---------:|:--------------:|:-----------:|
| in |	Evaluates to true if it finds a variable in the specified sequence and false otherwise. |	x in y, here in results in a 1 if x is a member of sequence y.|
| not in |	Evaluates to true if it does not finds a variable in the specified sequence and false otherwise. |	x not in y, here not in results in a 1 if x is not a member of sequence y.| 

**Python Identity Operators**

> Identity operators compare the memory locations of two objects. 

| Operator |	Description	| Example |
|:------------:|:----------------:|:---------------:|
| is | Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. |	x is y, here is results in 1 if id(x) equals id(y). |
|is not | Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. |x is not y, here is not results in 1 if id(x) is not equal to id(y).|

**Comments in Python**
> Single-line comments are created simply by beginning a line with the hash (#) character, and they are automatically terminated by the end of line.

    #This is the single line comment

> Comments that span multiple lines – used to explain things in more detail – are created by adding a delimiter (“””) on each end of the comment.

 

    “””” This would be a multiline comment
    in Python that spans several lines
    …
    “”” 

for more [Read the remaining all chapters in detail  click here (https://aitoml.com)](https://aitoml.com/)


