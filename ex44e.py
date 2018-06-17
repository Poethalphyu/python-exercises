class Other(object):
    def override(self):
        print("OTHER override()")
        def implict(self):
            print("Other implict()")
            def altered(self):
                print("OTHER implict()")
                def altered(self):
                    print("OTHER altered()")
    class Child(object):
        def __init__(self)
        self.other=Other()
        def implict(self):
            self.other.implict()
            def override(self):
                print("CHILD override()")
                def altered(self):
                    print("CHILD,BEFORE OTHER altered()")
                    self.other.altered()
                    print("CHILD ,AFTER OTHER altered()")
                    son=Child()
                    son.implict()
                    son.overrride()
                    son.altered()
