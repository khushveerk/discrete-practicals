# discrete-practicals
## que 1 -Create a class SET. Create member functions to perform the following SET operations:-

from itertools import chain, combinations, product

class SET:
    def __init__(self, elements):
        self.set = set(elements)

    def is_member(self, element):
        return element in self.set

    def powerset(self):
        return list(chain.from_iterable(combinations(self.set, r) for r in range(len(self.set)+1)))

    def is_subset(self, other_set):
        return self.set.issubset(other_set.set)

    def union(self, other_set):
        return self.set.union(other_set.set)

    def intersection(self, other_set):
        return self.set.intersection(other_set.set)

    def complement(self, universal_set):
        return universal_set.set.difference(self.set)

    def difference(self, other_set):
        return self.set.difference(other_set.set)

    def symmetric_difference(self, other_set):
        return self.set.symmetric_difference(other_set.set)

    def cartesian_product(self, other_set):
        return list(product(self.set, other_set.set))


def menu():
    print("\n==== SET OPERATIONS MENU ====")
    print("1. Check Membership")
    print("2. Powerset")
    print("3. Subset Check")
    print("4. Union")
    print("5. Intersection")
    print("6. Complement (Provide Universal Set)")
    print("7. Set Difference")
    print("8. Symmetric Difference")
    print("9. Cartesian Product")
    print("10. Exit")


if __name__ == "__main__":
    A = SET(input("Enter elements of Set A (space separated): ").split())
    B = SET(input("Enter elements of Set B (space separated): ").split())

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            ele = input("Enter element to check in Set A: ")
            print(f"{ele} is in Set A? {A.is_member(ele)}")

        elif choice == "2":
            print("Powerset of Set A:")
            for subset in A.powerset():
                print(subset)

        elif choice == "3":
            print("Is A a subset of B?", A.is_subset(B))

        elif choice == "4":
            print("Union of A and B:", A.union(B))

        elif choice == "5":
            print("Intersection of A and B:", A.intersection(B))

        elif choice == "6":
            U = SET(input("Enter elements of Universal Set (space separated): ").split())
            print("Complement of A w.r.t Universal Set:", A.complement(U))

        elif choice == "7":
            print("A - B:", A.difference(B))

        elif choice == "8":
            print("Symmetric Difference of A and B:", A.symmetric_difference(B))

        elif choice == "9":
            print("Cartesian Product A × B:")
            for pair in A.cartesian_product(B):
                print(pair)

        elif choice == "10":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

#enter a=1 2 3 4 ,b= 2 3 4 and enter any choice like 5,7 or 3 any 
#-------------------------------------------------------------------------------------------------
# que 2 - Create a class RELATION, use Matrix notation to represent a relation. Include member functions to check if the relation is Reflexive, Symmetric, Anti-symmetric, Transitive.
# Using these functions check whether the given relation is: Equivalence or Partial Order relation or None


class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def is_reflexive(self):
        for i in range(self.n):
            if self.matrix[i][i]:
                return True

    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == self.matrix[j][i]:
                    return True

    def is_antisymmetric(self):
        for i in range(self.length):
            for j in range(self.length): 
                if i != j and self.matrix[i][j] and self.matrix[j][i]:
                    return False
        return True
        

    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j]:
                    for k in range(self.n):
                        if self.matrix[j][k] and not self.matrix[i][k]:
                            return False
        return True
    

    def relation_type(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return "Equivalence"
        elif self.is_reflexive() and self.is_antisymmetric() and self.is_transitive():
            return "Partial Order"
        else:
            return "None"

# Example
matrix = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
r = RELATION(matrix)
print("Type of relation is :", r.relation_type())

# answer is equivalence

                          #OR

## 22222222222222222222
from numpy import array # type: ignore

class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.length = len(matrix)

    def reflexive(self):
        for i in range(self.length):
            if not self.matrix[i][i]:
                return False
        return True

    def symmetric(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def transitive(self):
        for i in range(self.length):
            for j in range(self.length):
                for k in range(self.length):
                    if self.matrix[i][j] and self.matrix[j][k] and not self.matrix[i][k]:
                        return False
        return True

    def antisymmetric(self):
        for i in range(self.length):
            for j in range(self.length): 
                if i != j and self.matrix[i][j] and self.matrix[j][i]:
                    return False
        return True

# Function to enter matrix (outside the class, not inside)
def enter_matrix():
    list1 = list(map(int, input("Enter all elements of the relation matrix (space-separated): ").split()))
    row = int(input("Enter number of rows (same as columns, since it's a square matrix): "))
    matrix = array(list1).reshape(row, row)
    print("The relation matrix is:\n", matrix)
    return matrix

# Main function (also outside the class)
def main():
    matrix = enter_matrix()
    rel = RELATION(matrix)
    
    if rel.reflexive() and rel.symmetric() and rel.transitive():
        print("✅ The relation is an **Equivalence Relation**")
    elif rel.reflexive() and rel.antisymmetric() and rel.transitive():
        print("✅ The relation is a **Partial Order Relation**")
    else:
        print(" The relation is **Neither Equivalence nor Partial Order**")

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------


# que 3- Write a Program that generates all the permutations of a given set of digits, with or without repition.

from itertools import permutations , product

def generate_permutation(set,repetition):
    if repetition:
        return list(product(set,repeat=len(set)))
    else:
        return list(permutations(set))
    
if __name__ =="__main__" :
    set=list(map(int,input("enter the elements withspace").split()))
        
    with_repetition = generate_permutation(set, repetition=True)
    without_repetition = generate_permutation(set, repetition=False)
        
    print("\n permutation with repetition ")
    for perm in with_repetition:
        print(perm)
            
    print("\n permutation withoutrepetition ")
    for perm in without_repetition:
        print(perm)
            
    print(f"\n Total with repetition :{len(with_repetition)}")
    print(f"\n Total without repetition : {len(without_repetition)}")
    
# enter elements as 1 2 3 then answer come and toatl with=27 and without =6

#-------------------------------------------------------------------------------------------------


#que 4 - For any number n, write a program to list all the solutions of the equation x1 + x2 + x3 + ...+ xn = C, 
      # where C is a constant (C<=10) and x1, x2,x3,...,xn are nonnegative integers, using brute force strategy.

from itertools import product

def find_solution(n,C):
    solutions=[]
    for combo in product(range (C+1) ,repeat=n):
        if sum(combo)== C:
            solutions.append(combo)
    return solutions 

if __name__ == "__main__":
    n=int(input("enter the no of variables:"))
    C=int(input("enter the value of C (C<=10) :"))
    
    if C>10 or C<0:
        print("C must be in btw 0 and 10 (inclusive)")
    else:
        solutions=find_solution(n,C)
        print(f"\n all the solutions for x1 , x2 , x3 ,.......x{n}=C{n} are :")
        for sol in solutions:
            print(sol)
        print(f" \n total solutions found : {len(solutions)}")
        

#enter variables 3and the c = 3 then answer is 10 and many solutions also


#-------------------------------------------------------------------------------------------------


# que 5 - Write a Program to evaluate a polynomial function.
# (For example store f(x) = 4n2 + 2n + 9 in an array and for a given value of n, say n = 5, compute the value of f(n))

def solve_function():
    func =list(map(int,input("enter the coeffients of the function(highest to lowest) separated by space").split()))
    num =int(input("enter the value of variable"))
    
    value =0
    degree=len(func)-1
    for i in range(len(func)):
        value += func[i] * ( num ** degree-i)
        return value
    
# Call th function and print the value
print("value of the function is :" , solve_function())

# enter fun as 9 4 2 and value as 5 then answer is 225

#-------------------------------------------------------------------------------------------------


#que 6 -Write a Program to check if a given graph is a complete graph.
  # Represent the graph using the Adjacency Matrix representation.

def is_complete_matrix(adj):
    n=len(adj)
    for i in range(n):
        for j in range(n):
            if i!=j and adj[i][j] !=1 :
                return False
    return True

# Example 
matrix =[
    [0,1,1],
    [1,0,1],
    [1,1,0]
]
print("is complete(matrix)",is_complete_matrix(matrix))

                     #OR 
def is_complete_graph(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 0:  # No self-loop
                    return False
            else:
                if matrix[i][j] != 1:  # All distinct pairs must be connected
                    return False
    return True

def main():
    n = int(input("Enter the number of vertices in the graph: "))
    print("Enter the adjacency matrix row by row (space-separated):")

    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            print("Invalid row length. Matrix must be square.")
            return
        matrix.append(row)

    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

    if is_complete_graph(matrix):
        print("\nThe graph is a COMPLETE graph.")
    else:
        print("\nThe graph is NOT a complete graph.")

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------


# que 7 -Write a Program to check if a given graph is a complete graph.
 # Represent the graph using the Adjacency List representation

def is_complete_list(adj_list):
    n=len(adj_list)
    for i in range(n):
        if len(adj_list[i]) != n-1 :
            return False
    return True

#example
adj_list = [[1,2],[0,2],[0,1]]
print("Is complete (list)", is_complete_list(adj_list))

                        #OR
def is_complete_graph(adj_list):
    n = len(adj_list)
    for vertex, neighbors in adj_list.items():
        if len(neighbors) != n - 1:
            return False
    return True

def main():
    n = int(input("Enter the number of vertices: "))
    adj_list = {}

    print("Enter the adjacency list for each vertex:")
    for i in range(n):
        neighbors = list(map(int, input(f"Enter neighbors of vertex {i} (space-separated): ").split()))
        adj_list[i] = neighbors

    print("\nAdjacency List:")
    for vertex in adj_list:
        print(f"{vertex}: {adj_list[vertex]}")

    if is_complete_graph(adj_list):
        print("\nThe graph is a COMPLETE graph.")
    else:
        print("\nThe graph is NOT a complete graph.")

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------------------------------


# que 8 -Write a Program to accept a directed graph G and compute the in-degree and out degree of each vertex

def compute_degrees(adj_matrix):
    n = len(adj_matrix)
    in_deg = [0]*n
    out_deg = [0]*n
    for i in range(n):
        for j in range(n):
            out_deg[i] += adj_matrix[i][j]
            in_deg[j] += adj_matrix[i][j]
    for i in range(n):
        print(f"Vertex {i}: In-degree = {in_deg[i]}, Out-degree = {out_deg[i]}")

# Example
graph = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0]
]
compute_degrees(graph)

                      #OR 
class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add a directed edge from u to v
        self.adj_list[u].append(v)

    def compute_degrees(self):
        in_degree = [0] * self.vertices
        out_degree = [0] * self.vertices

        for u in range(self.vertices):
            out_degree[u] = len(self.adj_list[u])  # Count of outgoing edges
            for v in self.adj_list[u]:
                in_degree[v] += 1  # Count of incoming edges

        print("\nVertex\tIn-Degree\tOut-Degree")
        for i in range(self.vertices):
            print(f"{i}\t{in_degree[i]}\t\t{out_degree[i]}")

    def print_adj_list(self):
        print("\nAdjacency List:")
        for i in range(self.vertices):
            print(f"{i}: {self.adj_list[i]}")


# Main program
if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of directed edges: "))

    graph = DirectedGraph(n)

    for i in range(e):
        u, v = map(int, input(f"Enter edge {i+1} (from to): ").split())
        graph.add_edge(u, v)

    graph.print_adj_list()
    graph.compute_degrees()
