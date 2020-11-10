from functools import reduce
import sys
number = int(sys.argv[1])
ans = reduce(lambda x, y: x * y , range(1, (number+1)))
print(f"Factorial of {number} is {ans} ")
