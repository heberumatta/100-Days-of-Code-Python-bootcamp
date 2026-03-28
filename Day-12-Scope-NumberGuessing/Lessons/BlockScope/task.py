#There is no Block Scope in Python. You can access variables defined in a block scope outside of it.
if True:
    block_scope_variable = "I am inside a block scope"

print(block_scope_variable)  # This will print "I am inside a block scope"

#But if you define a variable inside a function, it will be local to that function and cannot be accessed outside of it.

def my_function():
    if True:
        function_scope_variable = "I am inside a block scope"

#print(function_scope_variable)  # This will raise a NameError because function_scope_variable is not defined outside of the function.

