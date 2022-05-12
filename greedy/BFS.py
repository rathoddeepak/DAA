'''
-------- Breadth First Search --------
-> It is graph traversal algorithm
-> it is complete algorithm 
-> provides optimal solution
-> used in finding shortest path in the graph
-> works level wise 
-> uses queue data structure 
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
queue = [];

def BFS(nextNode):
	print(nextNode, end="-> ");

	for adjNode in graph[nextNode]:
		queue.append(adjNode);

	if(len(queue) == 0):
		return

	nextNode = queue.pop(0);
	BFS(nextNode);

BFS('A');
