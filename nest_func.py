import sympy as sp

def get_func_name(func_expr: str) -> str:
    func_name_end_pos: int = 0
    closing_brace_pos: int = 0

    for i in range(len(func_expr)):
        current = func_expr[i]
        if ((not (current.isalpha() or current == '_')) and func_name_end_pos == 0):
                if not (current == '('):
                    print("Expression not recognized as valid")
                    return
                else:
                    func_name_end_pos = i
        if (func_name_end_pos != 0 and current == ')'):
             closing_brace_pos = i
             
    if (func_name_end_pos == 0) or (closing_brace_pos == 0):
        print("Invalid expression")
        return
    
    return func_expr[0:func_name_end_pos]

def recursively_nest(func_expr: str, internal_var: str, n: int) -> str:
    func_name = get_func_name(func_expr)
    if func_name == None: return #get_func_name will itself print the "error" message, no need to add additional prints
    
    if n == 0:
        return func_expr

    result = ""

    #construct the left side
    for i in range(n):
        result += (func_name + "(")
    result += internal_var
    for i in range(n):
        result += ")"
    
    return result

t = recursively_nest("sin(x)", "x", 7)
print(t)