edges = {
 'A':[{'src':'A', 'dest':'F', 'weight':2},{'src':'A', 'dest':'B', 'weight':2},{'src':'A', 'dest':'D', 'weight':7}],
 'B':[{'src':'B', 'dest':'E', 'weight':3},{'src':'B', 'dest':'C', 'weight':1}],
 'C':[{'src':'C', 'dest':'F', 'weight':4}],
 'D':[{'src':'D', 'dest':'G', 'weight':5}],
 'E':[{'src':'E', 'dest':'C', 'weight':4},{'src':'E', 'dest':'D', 'weight':1}],
 'F':[{'src':'F', 'dest':'B', 'weight':5}],
 'G':[{'src':'G', 'dest':'E', 'weight':7}],
}
nonSelected = [];
parents = {
	'A':'A',
	'B':'B',
	'C':'C',
	'D':'D',
	'E':'E',
	'F':'F',
	'G':'G'
}

cost = 0;
mst = []

def parent(vertex):
	while parents[vertex] != vertex:
		vertex = parents[vertex];

	return vertex;

def prims(src):
	global cost, parents, mst, nonSelected;
	minEdge = None
	finalEdges = edges[src] + nonSelected;
	for edge in finalEdges:
		if(minEdge == None or minEdge['weight'] > edge['weight']):
			minEdge = edge;		

	if(minEdge == None):
		return

	nonSelected += edges[src];
	nonSelected.remove(minEdge);
	if(minEdge in edges[src]):
		edges[src].remove(minEdge)

	src = minEdge['src']

	if(parent(src) != parent(minEdge['dest'])):
		print(src, minEdge['dest'])
		parents[minEdge['dest']] = src;
		mst.append(minEdge);
		cost += minEdge['weight'];
	prims(minEdge['dest']);

prims('A');
print('Total Cost: ', cost);