def hello_world():
    "prints hello world"
    print("Hello World")
    return


def puss(name="Sonja"):
    "prints puss + name"
    print("puss" + name)
    return


def main():
    hello_world()
    puss


if __name__ == "__main__":
    main()

