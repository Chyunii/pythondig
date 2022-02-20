def A():
    x=10
    def B():
        nonlocal x
        x=20
    B()
    print(x)
