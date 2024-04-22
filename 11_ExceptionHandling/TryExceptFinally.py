def Display(a, b : int):
    try:
        print(a + b)
    except TypeError:
        print("Use integer value")
    finally:
        print("This will be executed always")

Display(12,15)