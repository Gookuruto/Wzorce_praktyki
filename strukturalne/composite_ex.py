class LeafElement:
    """Class representing objects at the bottom or Leaf of the hierarchy tree."""

    def __init__(self, *args):
        """'Takes the first positional argument and assigns to member variable "position"."""
        self.position = args[0]

    def showDetails(self, tab_number):
        """Prints the position of the child element."""
        # print("\t", end="")
        print(self.position)


class CompositeElement:
    """Class representing objects at any level of the hierarchy
    tree except for the bottom or leaf level. Maintains the child
     objects by adding and removing them from the tree structure."""

    def __init__(self, *args):
        """Takes the first positional argument and assigns to member
        variable "position". Initializes a list of children elements."""
        self.position = args[0]
        self.children = []

    def add(self, child):
        """Adds supplied child elemnt to the list of children."""
        self.children.append(child)

    def remove(self, child):
        """Remove child from children list."""
        self.children.remove(child)

    def showDetails(self, tab_number=1):
        """print details of the component first.
        Then iterates over each children and print thier details."""
        print(self.position)
        for child in self.children:
            print("\t" * tab_number, end="")
            child.showDetails(tab_number + 1)


if __name__ == "__main__":
    topLevelMenu = CompositeElement("GeneralManager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")
    subMenuItem11 = CompositeElement("Developer11")
    junior = LeafElement("Juniorek")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")
    # manager 1
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    # manager 2
    subMenuItem2.add(subMenuItem21)
    subMenuItem2.add(subMenuItem22)
    # developer 11
    subMenuItem11.add(junior)
    # general manager
    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)

    topLevelMenu.showDetails()
