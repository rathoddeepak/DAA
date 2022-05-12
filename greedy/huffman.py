data = ['a','b','c','d','e','f','g','h'];
frq = {'a' : 1, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 5, 'f' : 8, 'g' : 13, 'h' : 21}
stack = [];
bits = []
def huffman():
	n = 0;
	stackLen = len(stack);
	bitsReq = 0;
	if(stackLen == 0 and len(data) >= 1):
		n += 2;
		stack.append(data[0]);
		stack.append(data[1]);
		stack.append(frq[data[0]] + frq[data[1]]);

	for i in range(n, len(data)):
		node = frq[data[i]] + stack[-1]
		stack.append(data[i]);
		stack.append(node);

	i = 0;
	while (len(stack) != 0):
		stack.pop();
		bitsReq += (i + 1) * frq[stack.pop()];

		elm = stack[-1];
		if(isinstance(elm, str)):
			bitsReq += (i + 1) * frq[elm];
			stack.pop();

		i += 1;

	print('Bits Required: ', bitsReq);

huffman();