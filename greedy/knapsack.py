capacity = 50;
knapsack = [
	{'weight':10,'profit':60,'ratio':0},
	{'weight':20,'profit':100,'ratio':0},
	{'weight':30,'profit':120,'ratio':0}
]
length = len(knapsack)
#ratio calculation 
for i in range(0,  length):
	ratio = knapsack[i]['profit'] / knapsack[i]['weight']
	knapsack[i]['ratio'] = ratio;

#Sort in decreasing of profit
for i in range(0,  length - 1):
	for j in range(0, length - i - 1):
		if(knapsack[j]['profit'] < knapsack[j + 1]['profit']):
			knapsack[j]['profit'],knapsack[j + 1]['profit'] = knapsack[j + 1]['profit'],knapsack[j]['profit']

def start():
	global capacity
	profit = 0;
	for i in range(0,  length):		
		if(capacity > 0 and knapsack[i]['weight'] <= capacity):
			capacity -= knapsack[i]['weight']
			profit += knapsack[i]['profit']
		else:
			profit += (capacity/knapsack[i]['weight']) * knapsack[i]['profit']
			break;
	return profit;

print('Profit: ', start());