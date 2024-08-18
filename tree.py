from collections import deque

class Tree[F]:
    def __init__(self, node: F, children=None):
        children = children or []
        assert isinstance(children, list)
        for child in children:
            assert isinstance(child, Tree)
        self.node = node
        self.children = children

    
    # TODO: add emojies when printing trees
    def __str__(self) -> str:
        return self.__string(order=1)

    def __string(self, *, order=1):
        if self.isEmpty(): 
            return f'Leaf({self.node})'
        res = f'Tree({self.node}, [\n'
        for child in self.children:
            child: Tree 
            res += (order*'\t') + child.__string(order=order+1) + '\n'
        return res + ((order-1)*'\t') + '])'



    @classmethod
    def empty(cls, node: F):
        return cls(node, [])
    
    def isEmpty(self):
        return self.children == []

    def insert(self, tree):
        self.children.append(tree)
    
    def get(self):
        return self.node 
    
    def __iter__(self) -> None:
        self.deck = deque([self])
        return self 
    
    def __next__(self):
        if len(self.deck) == 0: raise StopIteration
        tree = self.deck.popleft()
        for child in tree.children:
            self.deck.append(child)
        return tree.node
    
    @property
    def pud(self):
        yield self.node
        for child in self.children:
            child: Tree 
            for node in child.pud:
                yield node
    
    @property
    def pdu(self):
        for child in self.children:
            child: Tree 
            for node in child.pdu:
                yield node
        yield self.node
    
    @property
    def des(self):
        for child in self.children:
            yield child


