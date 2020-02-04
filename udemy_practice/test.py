class Test:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "is speaking.")


def main():
    name = Test("Kitae")
    name.speak()
    print('This is a string {}'.format('Inserted!!'))
    print('The {} {} {}'.format('fox', 'brown', 'quick'))
    print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
    print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
    result = 100/77
    print("The result was {}".format(result))

    # Float formatting follows "{value:width.precision f}"
    print("The result was {r:10.3f}".format(r=result))
    print("The result was {r:1.5f}".format(r=result))
    print("The result was {r:1.2f}".format(r=result))

    # f literal methods.
    first_name = 'Kitae'
    print(f'Hello, his name is {first_name}')


if __name__ == '__main__':
    main()
