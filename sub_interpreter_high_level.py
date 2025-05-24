import _xxsubinterpreters as sub_interpreters
sub_int_1 = sub_interpreters.create()
code = """
def some_method(n):
    x = 0
    for i in range(n):
        x += i * i
    print(f"Result: {x}")

some_method(10**7)
"""

sub_interpreters.run_string(sub_int_1, code)
