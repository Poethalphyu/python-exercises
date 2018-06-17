class Parent(object):
    def override(self):
        print("PARENT implict()")
        def implict(self):
            print("PARENT implict()")
            def altered(self):
                print("PARENT implict()")
                class Child(Parent):
                    def override(self):
                        print("CHILD override()")
                        def altered(self)
                                print("CHILD overrride()")
                                def aletered(self):
                                    print("CHILD,BEFORE PARENT altered()")
                                    super(Child,self).altered()
                                    print("CHILD,AFTER PARENT altered()")
                                    dad=Parent()
                                    son=Child()
                                    dad.implict()
                                    son.implict()
                                    dad.override()
                                    son.override()
                                    dad.altered()
                                    son.altered()


