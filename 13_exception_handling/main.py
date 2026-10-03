
while True:
    try:
        number = int(input("Enter a number: "))
        print(1 / number)
        break
    except ZeroDivisionError:
        print("You can't divide by ZERO")
    except ValueError:
        print("Enter only numbers.")
    except Exception:
        print("Something went wrong!")
    finally:
        print("Do some cleanup here...")
