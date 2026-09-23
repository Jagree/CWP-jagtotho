def greetings(name=None):
    if name and isinstance(name, str):
        print(f"Hello, {name}")
    elif name is None:
        print("Hello, noble stranger.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)