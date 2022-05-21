
import numbers

def number(*numbers,**student):
    multi=1
    for number in numbers:
        multi*=number
        print(multi)
    print(f"Hello{student}")
        