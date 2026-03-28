#Modify global scope

global_variable = "I am a global variable"

def modify_global_variable():
    global global_variable  # Use the 'global' keyword to modify the global variable
    global_variable = "I have been modified"