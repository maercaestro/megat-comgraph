import unittest
from src.computational_graph import Node


class TestComputationalGraph(unittest.TestCase):
    def test_node_initialization(self):
        """Test initializing a node."""
        a = Node("a", 5)
        self.assertEqual(a.name, "a")
        self.assertEqual(a.value, 5)

    def test_addition(self):
        """Test addition of two nodes."""
        a = Node("a", 3)
        b = Node("b", 7)
        c = a + b
        self.assertEqual(c.name, "(a + b)")
        self.assertEqual(c.compute(), 10)

    def test_subtraction(self):
        """Test subtraction of two nodes."""
        a = Node("a", 10)
        b = Node("b", 4)
        c = a - b
        self.assertEqual(c.name, "(a - b)")
        self.assertEqual(c.compute(), 6)

    def test_multiplication(self):
        """Test multiplication of two nodes."""
        a = Node("a", 2)
        b = Node("b", 5)
        c = a * b
        self.assertEqual(c.name, "(a * b)")
        self.assertEqual(c.compute(), 10)

    def test_division(self):
        """Test division of two nodes."""
        a = Node("a", 8)
        b = Node("b", 2)
        c = a / b
        self.assertEqual(c.name, "(a / b)")
        self.assertEqual(c.compute(), 4)

    def test_division_by_zero(self):
        """Test division by zero handling."""
        a = Node("a", 8)
        b = Node("b", 0)
        c = a / b
        self.assertEqual(c.name, "(a / b)")
        self.assertEqual(c.compute(), 0)  # Division by zero returns 0

    def test_chained_operations(self):
        """Test chained operations."""
        a = Node("a", 2)
        b = Node("b", 3)
        c = Node("c", 4)
        result = a + b * c  # a + (b * c)
        self.assertEqual(result.compute(), 14)

    def test_serialization(self):
        """Test serialization to JSON format."""
        a = Node("a", 3)
        b = Node("b", 5)
        c = a + b
        c.compute()
        serialized = c.to_dict()
        expected = {
            "name": "(a + b)",
            "value": 8,
            "parents": [
                {"parent1": "a", "parent2": "b", "operation": "add"}
            ],
        }
        self.assertEqual(serialized, expected)

    def test_deserialization(self):
        """Test deserialization from JSON format."""
        node_map = {"a": Node("a", 3), "b": Node("b", 5)}
        node_dict = {
            "name": "(a + b)",
            "value": None,
            "parents": [
                {"parent1": "a", "parent2": "b", "operation": "add"}
            ],
        }
        c = Node.from_dict(node_dict, node_map)
        self.assertEqual(c.compute(), 8)

if __name__ == "__main__":
    unittest.main()
