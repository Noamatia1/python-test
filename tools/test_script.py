

from numbers.simp import add, subtract
from numbers.comp import sum_of_digits, ispal
import os


current_directory = os.path.abspath(os.path.dirname(__file__))
simp_module_path = os.path.join(current_directory, 'tools', 'numbers', 'simp.py')
comp_module_path = os.path.join(current_directory, 'tools', 'numbers', 'comp.py')
# Create missing directories if they don't exist
os.makedirs(os.path.join(current_directory, 'tools', 'numbers'), exist_ok=True)
# tried fixing an error. (fixed)


simp_module_called = False

def check_simp_module_called():
    if not simp_module_called:
        raise Exception("Functions in simp module must be called before functions in comp module.")

result_add = add(5, 3)
result_subtract = subtract(8, 2)

print(f"Addition result: {result_add}")
print(f"Subtraction result: {result_subtract}")

simp_module_called = True  


check_simp_module_called()  
result_sum_of_digits = sum_of_digits(234)
result_is_palindrome = ispal(121)

print(f"Sum of digits result: {result_sum_of_digits}")
print(f"Is palindrome result: {result_is_palindrome}")
