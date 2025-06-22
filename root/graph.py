# FILE: graph.py

import heapq
from typing import List, Iterator, TypeVar, Generic, Optional
from station import Station

T = TypeVar('T')


class Node(Generic[T]):
    """A graph node with support for disjoint set operations (Union-Find)."""
    
    def __init__(self, data: T):
        self.data = data
        self.parent = self  # Initially, each node is its own parent
        self.rank = 0
    
    def get_data(self) -> T:
        return self.data
    
    def find(self) -> 'Node[T]':
        """
        TODO: Implement the find operation for Union-Find.
        Find the representative of the set to which this node belongs.
        For now, don't use path compression.
        
        Returns:
            The representative node of the set
        """
        # TODO: Implement find operation
        pass
    
    def union(self, other: 'Node[T]') -> None:
        """
        TODO: Implement the union operation for Union-Find.
        Merges the two sets to which this node and the other node belong.
        Use union by rank for efficiency.
        
        Args:
            other: The other node to union with
        """
        # TODO: Implement union operation
        pass
    
    def __str__(self) -> str:
        if isinstance(self.data, Station):
            if self == self.find():
                return self.data.get_name()
            else:
                return f"{self.data.get_name()} ({self.find()})"
        return str(self.data)


class Edge(Generic[T]):
    """A weighted undirected edge in a graph."""
    
    def __init__(self, node1: Node[T], node2: Node[T], weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    
    def get_node1(self) -> Node[T]:
        return self.node1
    
    def get_node2(self) -> Node[T]:
        return self.node2
    
    def get_weight(self) -> int:
        return self.weight
    
    def __lt__(self, other: 'Edge[T]') -> bool:
        """For use with heapq (min-heap)."""
        return self.weight < other.weight
    
    def __str__(self) -> str:
        return f"Edge({self.node1.get_data()}, {self.node2.get_data()}, {self.weight})"


class KruskalIterator(Generic[T]):
    """Iterator that provides edges according to Kruskal's Algorithm."""
    
    def __init__(self, edges: List[Edge[T]], mod_count: int):
        """
        TODO: Initialize the iterator for Kruskal's algorithm.
        
        Args:
            edges: List of all edges in the graph
            mod_count: Modification count for concurrent modification detection
        """
        self.edge_queue = []  # Use as min-heap
        self.next_edge: Optional[Edge[T]] = None
        self.expected_mod_count = mod_count
        
        # TODO: Initialize the priority queue with all edges
        # TODO: Compute the first edge that should be returned
        pass
    
    def _compute_next_edge(self) -> None:
        """
        TODO: Compute the next edge to be returned by the iterator.
        This should implement the core logic of Kruskal's algorithm:
        1. Get the next smallest edge from the priority queue
        2. Check if the edge connects two different components (using Union-Find)
        3. If yes, union the components and set this as the next edge
        4. If no, continue to the next edge
        5. If no more valid edges, set next_edge to None
        """
        # TODO: Implement Kruskal's algorithm logic
        pass
    
    def __iter__(self) -> Iterator[Edge[T]]:
        return self
    
    def __next__(self) -> Edge[T]:
        """
        TODO: Return the next edge in the MST.
        Should raise StopIteration when no more edges are available.
        Should raise RuntimeError if the graph was modified after iterator creation.
        """
        # TODO: Check for concurrent modification
        # TODO: Check if there's a next edge available
        # TODO: Return current edge and compute the next one
        pass


class Graph(Generic[T]):
    """A graph with nodes and weighted edges."""
    
    def __init__(self):
        self.nodes: List[Node[T]] = []
        self.edges: List[Edge[T]] = []
        self.mod_count = 0
    
    def add_node(self, data: T) -> None:
        """Add a new node with the specified data to the graph."""
        self.mod_count += 1
        self.nodes.append(Node(data))
    
    def add_edge(self, node1: Node[T], node2: Node[T], weight: int) -> None:
        """Add an edge between two nodes with the specified weight."""
        self.mod_count += 1
        self.edges.append(Edge(node1, node2, weight))
    
    def get_nodes(self) -> List[Node[T]]:
        """Get all nodes in the graph."""
        return self.nodes
    
    def get_edges(self) -> List[Edge[T]]:
        """Get all edges in the graph."""
        return self.edges
    
    def get_kruskal_iterator(self) -> KruskalIterator[T]:
        """
        Get an iterator that provides edges according to Kruskal's Algorithm.
        The iterator provides edges of increasing weight that would join distinct
        subtrees into a single minimum spanning tree.
        """
        return KruskalIterator(self.edges, self.mod_count)