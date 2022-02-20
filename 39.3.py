class Counter:

    def __init__(self, stop):
        self.stop=stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError

