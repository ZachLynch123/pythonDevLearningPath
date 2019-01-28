

class myClass():
    def method(self):
        print("method1")

    def method2(self, someString):
        print("myClass method2" + someString)


def main():
    c = myClass()
    c.method()
    c.method2(" called back!")


if __name__ == "__main__":
    main()