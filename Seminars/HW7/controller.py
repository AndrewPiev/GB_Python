from view import get_mode, get_value_rational, get_value_comlex, return_result, get_operation
from logger import general_log
from calc import init, sum, sub, mult, div

def do_it():
    nums_mode = get_mode()
    if nums_mode == 1:
       num1, num2 = get_value_rational()
    else:
        a, b, c, d = get_value_comlex()
        num1, num2 = complex (a,b), complex (b,c)
    init(num1, num2)
    operand = get_operation()
    if operand ==1:
        result = sum()
    elif operand == 2:
        result = sub()
    elif operand == 3:
        result = mult()
    elif operand == 4:
        result = div()
    print (return_result(result))
    general_log (num1, num2, nums_mode, operand, result)
