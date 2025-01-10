# MEGAT Computational Graph

## Introduction

![alt text](https://github.com/maercaestro/megat-comgraph/blob/a3917f82f7ebfbbc0b2878cbade19af3bd14f5b7/example/gambar-comgraph.png))


This project implements a **computational graph** that breaks down complex calculations into discrete, traceable components called nodes. Each node represents a simple arithmetic operation or a leaf value, allowing for modular computation. This implementation showcases the power of computational graphs for feature impact analysis and other numerical computations.

The computational graph supports:
- Addition
- Subtraction
- Multiplication
- Division

It also includes methods for serialization and deserialization to JSON, making it suitable for saving and loading computational states.

---

## Features

- **Traceable Computations**: Nodes and their operations are explicitly represented, making the computation process easy to follow.
- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Serialization**: Save the graph structure and node values to JSON for storage or debugging.
- **Deserialization**: Reconstruct the computational graph from a JSON dictionary.
- **Dynamic Computation**: Automatically calculates the value of nodes based on their parents.

---

## How It Works

### Node Class
Each node in the graph represents a variable or an operation. Nodes can be combined using basic arithmetic operators (`+`, `-`, `*`, `/`) to form a directed acyclic graph (DAG).

#### Key Methods:
1. **`__init__`**: Initializes the node with a name and optional value.
2. **`__add__`, `__sub__`, `__mul__`, `__truediv__`**: Overloaded operators for building the graph.
3. **`compute`**: Recursively calculates the value of the node based on its parents.
4. **`to_dict`**: Serializes the node into a JSON-compatible dictionary.
5. **`from_dict`**: Reconstructs a node from a serialized dictionary.

---

## Example Use Case

### Creating and Using Nodes
```python
# Create leaf nodes
a = Node("a", 5)
b = Node("b", 3)

# Build a computational graph
c = a + b  # c = a + b
d = c * a  # d = (a + b) * a

# Compute values
print(f"Value of c: {c.compute()}")  # Output: 8
print(f"Value of d: {d.compute()}")  # Output: 40

# Serialize the graph
serialized = d.to_dict()
print(serialized)

# Deserialize the graph
node_map = {"a": a, "b": b}
d_reconstructed = Node.from_dict(serialized, node_map)
print(f"Recomputed value of d: {d_reconstructed.compute()}")  # Output: 40
```

---

## Installation

### Prerequisites
- Python 3.7+

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/maercaestro/megat-comgraph.git
   cd megat-comgraph
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

---

## Advantages

- **Explicit Relationships**: Visualize and debug the relationships between variables and their computations.
- **Reusability**: Intermediate computations are cached, reducing redundant calculations.
- **Scalability**: Supports complex computations involving multiple layers of operations.

---

## Future Work

- Extend to support non-linear operations (e.g., power, logarithm).
- Implement graph visualization for better interpretability.
- Add support for multi-threaded computations for performance optimization.

---

## License
This project is licensed under the MIT License.

---

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

---

## Contact
For questions or suggestions, contact [maercaestro@gmail.com].

