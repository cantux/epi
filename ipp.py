#!/usr/bin/env python

def test():
    pass

ops = ['+', '-', '/', '*']
def parenthesize_infix(txt):
    # if there are 3 or more literals with two signs that are not parenthesized 
    # A + B * C =>  A + ( B * C )
    # A + B * C * D => a + ( ( b * c ) * d )
    for ch in txt:
        if ch == ' ':continue            
        if ch in symbols: 
            pares_stack

# assume multiple digits and spaces between all the literals.
def postfix_eval(txt):
    # abc+* (2 3 5) = 16
    # abc*+ = 17
    lit_lst = txt.split()
    for ch in lit_lst:
        if ch in ops:
            op1 = op_stack.pop()
            op2 = op_stack.pop()
            result = apply_arithmetic(op1, op2, ch)
            op_stack.push(result)
        else:
            op_stack.push(int(token))

def apply_arithmetic(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b
    else:
        return a * b

if __name__ == "__main__":
    test()
