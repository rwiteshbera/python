def Division(a: int, b: int):
    try:
        c = a / b
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except TypeError:
        print("Use integer value only")
    else:
        print("c = " + str(c))


Division(12,4) # 3.0
Division(13,0) # Cannot divide by zero

