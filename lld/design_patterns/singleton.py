# Singleton pattern belongs to creational patterns.

# Singleton:
# - Singleton pattern lets you ensure that a class has only one instance, while providing a global access point to this instance.
# - Use the singleton pattern when:
# -- a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program.
# -- you need stricter control over global variables.


class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:

            # super class explanation:
            # - syntax: class super(type, object_or_type=None)
            # - Return a proxy object that delegates method calls to a parent or sibling class of 'type'. This is useful for accessing inherited methods that have been overridden in a class.
            # - The 'object_or_type' determines the method resolution order (MRO) to be searched. The search starts from the class right after the 'type'.
            # - For example, if __mro__ of 'object_or_type' is D -> B -> C -> A -> object and the value of 'type' is B, then super() searches C -> A -> object.

            cls._instance = super(Singleton, cls).__new__(
                cls
            )  # In Python, __new__() method is implicitly a static method.

            print("Singleton instance is created")
        else:
            print("Singleton instance is already created")

        return cls._instance

    def __init__(self):
        if not Singleton._initialized:
            # one time initialization of the instance
            self.attribute_1 = "attribute_1"
            self.attribute_2 = "attribute_2"

            Singleton._initialized = True

            print("Singleton instance is initialized")
        else:
            print("Singleton instance is already initialized")

    # using __str__() method to test singleton design pattern.
    def __str__(self):
        return f"""
        instance id --> {id(self)}
        instance hash --> {hash(self)}
        instance attributes --> attribute_1: {self.attribute_1}, self.attribute_2: {self.attribute_2}
        """

    # if needed, we can have an additional classmethod to get the singleton instance.
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            print("Singleton instance is created + initialized")
        else:
            print("Singleton instance is already created + initialized")

        return cls._instance


print(Singleton.get_instance())
print(Singleton())  # Instance creation (__new__) + Instance initialization (__init__)
print(Singleton.get_instance())

# a = Singleton.get_instance()
# b = Singleton()
# c = Singleton.get_instance()
# print(a == b == c) # True
