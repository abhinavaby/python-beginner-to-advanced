# Can you change the self-parameter inside a class to something else
# (say "harry")? Try changing self to "slf" or "harry" and see the effects.

class Sample:
    def __init__(slf, name):
        slf.name = name

    def show(slf):
        print("Name:", slf.name)


obj = Sample("Abhinav")
obj.show()


# Answer: Yes, the name self can be replaced with any valid variable name such as slf or harry. Python treats it as the reference to the current object. However, using self is the standard convention and is strongly recommended.