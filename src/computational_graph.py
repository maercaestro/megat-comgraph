import json
# Computational Graph class written by Abu Huzaifah Bidin
# with help from ChatGPT for debugging and testing
# -------------------------------
# Node Class Definition - where we create the nodes of the computational graph
# -------------------------------

class Node:
    # ----------------------------------------
    # Initialization Method
    # ----------------------------------------
    def __init__(self, name, value=None):
        """
        Initialize a node in the computational graph.
        :param name: Name of the node (string).
        :param value: Initial value of the node (float or int).
        """
        self.name = name
        self.value = value  # Value of the node
        self.parents = []   # List of parent nodes and operations

    # ----------------------------------------
    # Overloaded Arithmetic Operators - where we add  the basic arithmetic operations
    # ----------------------------------------
    
    def __add__(self, other):
        """
        Overload the + operator for addition.
        """
        result = Node(f"({self.name} + {other.name})")
        result.parents.append((self, other, "add"))
        return result

    def __sub__(self, other):
        """
        Overload the - operator for subtraction.
        """
        result = Node(f"({self.name} - {other.name})")
        result.parents.append((self, other, "subtract"))
        return result

    def __mul__(self, other):
        """
        Overload the * operator for multiplication.
        """
        result = Node(f"({self.name} * {other.name})")
        result.parents.append((self, other, "multiply"))
        return result

    def __truediv__(self, other):
        """
        Overload the / operator for division.
        """
        result = Node(f"({self.name} / {other.name})")
        result.parents.append((self, other, "divide"))
        return result

    # ----------------------------------------
    # Computational Methods - where we define the compute method
    # ----------------------------------------
    
    def compute(self):
        """
        Compute the value of the node based on its parents and operations.
        :return: Computed value of the node.
        """
        if self.value is not None:  # Leaf node
            return self.value

        value = 0
        for parent1, parent2, operation in self.parents:
            if operation == "add":
                value = parent1.compute() + parent2.compute()
            elif operation == "subtract":
                value = parent1.compute() - parent2.compute()
            elif operation == "multiply":
                value = parent1.compute() * parent2.compute()
            elif operation == "divide":
                divisor = parent2.compute()
                value = parent1.compute() / divisor if divisor != 0 else 0
        self.value = value  # Cache computed value
        return value

    # ----------------------------------------
    # Serialization Methods - where we save the node into json dictionary and load it back
    # ----------------------------------------
    
    def to_dict(self):
        """
        Convert the node to a dictionary for serialization.
        """
        return {
            "name": self.name,
            "value": self.value,
            "parents": [
                {"parent1": parent1.name, "parent2": parent2.name, "operation": operation}
                for parent1, parent2, operation in self.parents
            ],
        }

    @staticmethod
    def from_dict(node_dict, node_map):
        """
        Recreate a node from a dictionary during deserialization.
        :param node_dict: The dictionary representing the node.
        :param node_map: A mapping of node names to Node objects.
        """
        name = node_dict["name"]
        value = node_dict["value"]
        node = Node(name, value)

        for parent_info in node_dict["parents"]:
            parent1 = node_map[parent_info["parent1"]]
            parent2 = node_map[parent_info["parent2"]]
            operation = parent_info["operation"]
            if operation == "add":
                node = parent1 + parent2
            elif operation == "subtract":
                node = parent1 - parent2
            elif operation == "multiply":
                node = parent1 * parent2
            elif operation == "divide":
                node = parent1 / parent2
        return node
