def hello(counter: int, name="World", ending="!"):
    for i in range(counter):
        print(f'Hello {name}{ending}')

hello(5)
hello(3,name="Béla")
hello(2,ending=".")
hello(1,ending="?",name="Pista")
hello(4,"Józsi",":")

