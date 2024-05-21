"""
Test code
"""


def say_many_hello(nb_of_hello: int = 1):
    """
    print as many hello world as you want

    :param nb_of_hello: int
    :return:
    """
    for _ in range(nb_of_hello):
        print("Bonjour Monde")


if __name__ == "__main__":

    say_many_hello(3)