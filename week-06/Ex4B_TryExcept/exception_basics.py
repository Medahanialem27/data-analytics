try:
    age = int("hello")
except ValueError:
    print("ValueError: I couldn't convert that text to a number.")
else:
    print(age)
finally:
    print("Let's try another one...")

    try:
        m = banana
    except NameError:
        print("NameError: this name has not been defined.")
    else:
        print(m)
    finally:
        print("Let's try another one...")

        try:
            result ="age" + 5
        except TypeError:
            print("TypeError: text and a number cannot be added this way")
        else:
            print(result)
        finally:
            print("Let's try another one...")

            try:
                compile("if True print('hello')", "<string", "exec")
            except SyntaxError:
                print("SyntaxError: the code has invalid syntax.")
            else:
                print("The code has valid syntax.")
            finally:
                print("Let's try another one...")