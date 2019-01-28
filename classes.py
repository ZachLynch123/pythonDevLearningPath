

class myClass():
    def method(self):
        print("method1")

    def method2(self, someString):
        print("myClass method2" + someString)

class myClass2(myClass):
    def method(self):
        myClass.method(self)
        print("method1 anotherClass")

    def method2(self, someString):
        print("anotherClass method2" )

def main():
    c = myClass()
    c2 = myClass2()
    c.method()
    c.method2(" called back!")
    c2.method()
    c2.method2(" Another callback")


if __name__ == "__main__":
    main()