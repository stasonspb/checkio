class Friends:
    def __init__(self, connections):
        self.connections = list(connections)
        print connections

    def add(self, connection):
        self.connection = connection
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        return False
    def remove(self, connection):
        self.connection = connection
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

    def names(self):
        name = set()
        for i in self.connections:
            name = name.union(i)
        return name

    def connected(self, name):
        self.name = name
        test = set()
        conn = [i for i in self.connections if name in i]
        if conn:
            for i in conn:
                test = test.union(i)
            test.remove(name)
        else:
            return test
        return test
            
            



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
