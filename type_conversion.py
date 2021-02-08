def implicitConversion():

    """In Implicit type conversion, Python interpreter is responsible to perform type conversion.
     We need not to do it manually."""

    x = 10
    print("Type of x before conversion is :", type(x))
    y = 10.6
    x = x + y
    print("Type of x after conversion is :", type(x))

    p = 10
    print("Type of p before conversion is :", type(p))
    q = 10.6
    p = q - p
    print("Type of p after conversion is :", type(p))

    bool_val = True
    print("Type of bool_val before conversion is: ", type(bool_val))
    bool_val = bool_val + y
    print("Type of bool_val after conversion is: ", type(bool_val))

    complex_num = 10j
    w = 5
    print("Type of w before conversion is: ", type(w))
    w = complex_num + w
    print("Type of w after conversion is: ", type(w))




def explicitConversion():

    """ In Explicit type conversion, we can apply a cast externally to a data type.
    User can perform type casting manually as per the requirements."""

    a = 10
    print("Type of a before conversion is: ", type(a))
    a = hex(a)
    print("Type of a after conversion is: ", type(a))

    b = (1,2,3,4)
    print("Type of b before conversion is: ", type(b))
    b = list(b)
    print("Type of b after conversion is: ", type(b))

    s = 10
    print("Type of s before conversion is: ", type(s))
    s = str(s)
    print("Type of s after conversion is: ", type(s))

    l = [1,2,3,4,5]
    print("Type of l before conversion is: ", type(l))
    l = enumerate(l)
    print("Type of l after conversion is: ", type(l))
    print("Data type in l are: ")
    for x in l:
        print(x,type(x))

    t = {0:'a',1:'b',2:'c',3:'d'}
    print("Type of t before conversion is: ", type(t))
    t = list(t)
    print("Type of t after conversion is: ", type(t))


if __name__ == '__main__':
    print("-----------------Implicit Conversion-------------")
    implicitConversion()
    print("\n-----------------Explicit Conversion----------------------")
    explicitConversion()

