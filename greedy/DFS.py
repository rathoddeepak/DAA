'''
-------- Breadth First Search --------
-> It is graph traversal algorithm
-> it is incomplete algorithm 
-> provides non-optimal solution
-> Gets into loop if search space is infinity, or may get into cycle
-> used for cycle detection, puzzle solving, sorting topology
-> works Depth Wise
-> uses stack data structure 
-> Time Complexities -> O(n^2) O(V + E)

'''

graph = {
 'A':['B', 'C'],
 'B':['D', 'E'],
 'C':['F'],
 'D':[],
 'E':[],
 'F':[]
}
stack = [];


def DFS(nextNode):
	print(nextNode, end="");

	for adjNode in graph[nextNode]:
		stack.append(adjNode);

	if(len(stack) == 0):
		return
		
	print(' -> ', end="");
	nextNode = stack.pop();
	DFS(nextNode);

DFS('A');

