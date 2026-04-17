## default parameter
def greet(name="Guest"): # here we provides deafault value to name 
    print(f"Hello {name}, Welcome to my home")

greet()


# without passing default parameter
def greet(name):  
    print(f"Hello {name}, Welcome to my home")

greet()
"""
It shows error:

PS C:\Users\hp\OneDrive\Desktop\Agentic AI> python -u "c:\Users\hp\OneDrive\Desktop\Agentic AI\functions\default_parameter.py"
Traceback (most recent call last):
  File "c:\Users\hp\OneDrive\Desktop\Agentic AI\functions\default_parameter.py", line 12, in <module>
    greet()
TypeError: greet() missing 1 required positional argument: 'name'
PS C:\Users\hp\OneDrive\Desktop\Agentic AI> 
"""