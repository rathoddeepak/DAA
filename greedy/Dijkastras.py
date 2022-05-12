'''
----- Dijkastra's Algorithm -----
-> Used For Finding Shortest Path
-> Uses greedy method
-> We Start At Any arbitrary point
-> Then select the vertex with minimum weight
-> Then we find the adjacent vertex of the selected vertex
-> and perform relaxation of the adjacent vertex and mark the vertex as visited
-> Relaxation 
   if ((d[u] + c[u][v]) < d[v]){
	d[v] = d[u] + c[u][v]
   }
   d[u].checked = true
'''
inf = 999;
graph = [
 #0  1  2  3  4  5  6  7  8
 [0, 4, 0, 0, 0, 0, 0, 8, 0], #0
 [4, 0, 8, 0, 0, 0, 0, 11, 0], #1
 [0, 8, 0, 7, 0, 4, 0, 0, 2], #2
 [0, 0, 7, 0, 9, 14, 0, 0, 0], #3
 [0, 0, 0, 9, 0, 10, 0, 0, 0], #4
 [0, 0, 4, 14, 10, 0, 2, 0, 0], #5
 [0, 0, 0, 0, 0, 2, 0, 1, 6], #6
 [8, 11, 0, 0, 0, 0, 1, 0, 7 ], #7
 [0, 0, 2, 0, 0, 0, 6, 7, 0] #8
];

weights = [
 {'cost':0,  'checked': True},
 {'cost':4,  'checked': False},
 {'cost':inf,  'checked': False},
 {'cost':inf,  'checked': False},
 {'cost':inf,  'checked': False},
 {'cost':inf,  'checked': False},
 {'cost':inf,  'checked': False},
 {'cost':8,  'checked': False},
 {'cost':inf,  'checked': False}
]

def printWeights():
	i = 0;
	for weight in weights:
		print(i, weights[i]['cost']);
		i += 1;

def minWeight():
	minCost = inf;
	for weight in weights:
		if weight['checked'] == False and minCost > weight['cost']:
			minCost = weight['cost']

	minIndex = -1;
	for weight in weights:
		minIndex += 1;
		if weight['checked'] == False and minCost == weight['cost']:
			return minIndex

	return -1;

def dijkastra(startPoint):
	row = startPoint;
	for col in range(0, len(graph[startPoint])):
		if(graph[row][col] != 0):
			du = weights[row]['cost'];
			cuv = graph[row][col];
			dv = weights[col]['cost'];
			total = du + cuv;
			if(total < dv):
				weights[col]['cost'] = total;

	weights[startPoint]['checked'] = True;
	startPoint = minWeight();
	if(startPoint == -1):
		return
	return dijkastra(startPoint);

dijkastra(1);
printWeights();

