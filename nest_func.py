
def get_func_name(func_expr: str) -> list:
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
    
    var_name = ""
    potential_var_name = func_expr[(func_name_end_pos + 1):closing_brace_pos]
    if potential_var_name.isalpha():
        var_name = potential_var_name
    return [func_expr[0:func_name_end_pos], var_name]

def recursively_nest(func_expr: str, n: int) -> str:
    func_name, var_name = get_func_name(func_expr)
    if func_name == None: return #get_func_name will itself print the "error" message, no need to add additional prints
    
    if n == 0:
        return func_expr

    result = ""

    #construct the left side
    for i in range(n):
        result += (func_name + "(")
    result += var_name
    for i in range(n):
        result += ")"
    
    return result
