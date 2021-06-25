#
# Since the operators that are defined take an operand on each side,
# we can count on the fact that the length of the numbers array will be
# equal to the length of the operators array + 1. Also, the left-hand operand
# will share an index with the operator, and the right-hand operand will be
# one greater than that: e.g. if we pass the string "2+4", we will have an
# operator array ['+'] and a number array ['2', '4'].
#                 (0)                      (0)  (1)
# 
# We can caluculate the result by exhausting--in order of BEDMAS--the
# array of operators by applying the operator to it's left and right
# operands. We then remove the operator from the list, and replace the
# two operands with their resulting value in the number list. When there 
# are no operators left, the single number left in the numbers list is
# our final answer.
#
# ex: "10+4*2-11"
#   operators : ['+', '*', '-'] -> ['+', '-']  -> ['-']    -> []
#   numbers   : [10, 4, 2, 11]  -> [10, 8, 11] -> [18, 11] -> [7] = 7
#

#
# get expression from user input
#
expression = input()

#
# get an ordered list of all operation occurances
#
operations = []
for char in expression:
    if char in ['*', '/', '+', '-']:
        operations.append(char)

#
# get an ordered list of all numbers
#
# replace any operation characters with a space
for op in ['*', '/', '+', '-']:
    expression = expression.replace(op, ' ') 
# split into array of strings where spaces are
number_strings = expression.split(' ') 
numbers = []
# parse strings into numbers
for num in number_strings: 
    numbers.append(float(num))


# convenient function to get next operation with current precedence level
def next_index(operation_pair):
    for index in range(len(operations)):
        if operations[index] in operation_pair:
            return index
    return -1

#
# Logic for applying the operations sequentially
#
for operation_pair in [['*', '/'], ['+', '-']]: # do for ('*' and '/'), then for ('+' and '-')

    # get the index, within the operations list, of the first operator in the current operator pair
    operation_index = next_index(operation_pair)
    
    # while there are still operators in the operations list from the operation pair
    while operation_index >= 0: 
        operator      = operations[operation_index]
        left_operand  = numbers[operation_index]
        right_operand = numbers[operation_index + 1]

        if operator == '*':
            operation_result = left_operand * right_operand
        elif operator == '/':
            operation_result = left_operand / right_operand
        elif operator == '+':
            operation_result = left_operand + right_operand
        elif operator == '-':
            operation_result = left_operand - right_operand


        numbers[operation_index] = operation_result # assign result to index of left operand
        numbers.pop(operation_index + 1) # remove right operand from  numbers array

        operations.pop(operation_index) # remove operator from operations array

        operation_index = next_index(operation_pair) # get index of next operator

final_result = numbers[0]
print(final_result)
