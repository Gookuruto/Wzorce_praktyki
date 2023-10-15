class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class MyClass(Singleton):

    def __init__(self):
        self.x = 100
        self.y = 200

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


x = MyClass()
y = MyClass()

print(x)
print(y)
x.x = 300
print(x)
print(y)
print(x == y)
print(x is y)
