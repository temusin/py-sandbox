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

    # list
    my_list = [1,2,3]
    another_list = ['four','five']
    total = my_list + another_list
    total.append('six')

    # pop() removes the value of the last index
    total.pop()
    popped_value = total.pop()
    print(total)
    print(popped_value)

    new_list = ['b','d','z','t','e']
    num_list = [3,1,9,2]
    new_tuple = (1,2,3,2)
    print(num_list)
    num_list.reverse()
    print(num_list)
    num_list.sort()
    print(num_list)
    print(num_list.pop())
    print(len(num_list))
    print(len(new_tuple))
    print(new_tuple.count(2))
    print(new_tuple.index(2))

    myset = [1,1,1,1,2,2,2,3,3,3]
    myset = set(myset)

    print(1<2)

if __name__ == '__main__':
    main()
