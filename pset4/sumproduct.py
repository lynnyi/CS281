import copy
import numpy

psi = {}
psi1 = [0.7, 0.3]
psi2 = [0.1, 0.9]
psi = {1:psi1, 3:psi1, 5:psi1}
psi[2]=psi2
psi[4]=psi2
psi[6]=psi2
ecf = [[1,0.45],[0.45,1]]
edges = [[1,2],[2,4],[2,5],[1,3],[3,6]]
numStates=2
nodes = 6
diameter=2
	
#neighbors
def initialize_neighbors(edges):
	neighbors = {}
	for [i,j] in edges:
		if i in neighbors.keys():
			neighbors[i].append(j)
		else:
			neighbors[i] = [j]
		if j in neighbors.keys():
			neighbors[j].append(i)
		else:
			neighbors[j] = [i]
	return neighbors

#messages key as 'i-j' for message i->j
def initialize_messages(edges, numStates):
	messages = {}
	for [i,j] in edges:
		messages[str(i)+'-'+str(j)]=[.1]*numStates
		messages[str(j)+'-'+str(i)]=[.1]*numStates
	return messages


#O(s * neighbors)
def update(edge, state, neighbors, messages, numStates, psi, ecf):
	print(edge)
	[i,j] = edge
	s = 0
	for state_s in range(numStates):
		i_neighbors = neighbors[i]
		product = 1
		for n in i_neighbors:
			if n != j:
				product *= messages[str(n)+'-'+str(i)][state_s]	
		s += psi[i][state_s]*ecf[state_s][state]*product
		print(s)
	return s


#O(Diameter*edges*states)*O(update)
def sum_product(edges, neighbors, numStates, psi, ecf, diameter):
	messages = initialize_messages(edges, numStates)
	for step in range(diameter):
		new_messages=copy.copy(messages)
		for edge in edges:
			[i,j]=edge
			for state in range(numStates):
				new_messages[str(i)+'-'+str(j)][state] = update(edge,state,neighbors,messages,numStates,psi,ecf)
				new_messages[str(j)+'-'+str(i)][state] = update([j,i],state,neighbors,messages,numStates,psi,ecf)
		messages=new_messages
	return messages

def calculate_probability(nodes, neighbors, messages, psi):
	probability = []
	for n in range(1,nodes+1):
		p = psi[n]
		n_neighbors = neighbors[n]
		for neighbor in n_neighbors:
			p = numpy.multiply(p,messages[str(neighbor)+'-' + str(n)])
		probability.append(p)
	probability = [i/sum(i) for i in probability]
	return probability


neighbors = initialize_neighbors(edges)
final_messages = sum_product(edges, neighbors, numStates, psi, ecf, diameter)
probability = calculate_probability(nodes,neighbors,final_messages,psi)
print(probability)
