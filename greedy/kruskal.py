edges = [
 {'src':'B', 'dest':'C', 'weight':1},
 {'src':'E', 'dest':'D', 'weight':1}, 

 {'src':'A', 'dest':'B', 'weight':2},
 {'src':'A', 'dest':'F', 'weight':2},
 

 {'src':'B', 'dest':'E', 'weight':3},

 {'src':'E', 'dest':'C', 'weight':4},
 {'src':'C', 'dest':'F', 'weight':4},
 

 {'src':'D', 'dest':'G', 'weight':5},
 {'src':'F', 'dest':'B', 'weight':5},

 {'src':'G', 'dest':'E', 'weight':7},
 {'src':'A', 'dest':'D', 'weight':7},
]

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

for edge in edges:
	if(parent(edge['src']) != parent(edge['dest'])):
		parents[edge['dest']] = edge['src'];
		mst.append(edge);
		cost += edge['weight'];

print('Total Cost: ', cost);