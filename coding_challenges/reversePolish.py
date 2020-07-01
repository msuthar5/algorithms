"""
Evaluate Reverse Polish Notation

leetcode.com/problems/evaluate-reverse-polish-notation/

["2", "1", "+", "3", "*"] --> ((2 + 1) * 3) = 9

["4", "13", "5", "/", "+"] --> (4 + (13 / 5)) = 6

["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"] --> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
"""

import math

def evaluateExpression(operator, arg1, arg2):
        if operator == "+":
            return arg1 + arg2
        if operator == "-":
            return arg1 - arg2
        if operator == "*":
            return arg1 * arg2
        if operator == "/":
            return int(float(arg1) / float(arg2))
        
def evalRPN(tokens):

    operators = {"+", "-", "*", "/"}
    stack = list()
    
    for tok in tokens:
        stack.append(tok)
        
    def evalExpr():
        if not stack:
            return
        
        tok = stack.pop()
        if tok in operators:
            right = evalExpr()
            left = evalExpr()
            
            return evaluateExpression(tok, left, right)
        
        return int(tok)
        
    return evalExpr()

print('["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]' + " --> "  + str(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])))