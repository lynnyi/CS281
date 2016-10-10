

global psi
psi = {}

psi1 = [0.7, 0.3]
psi2 = [0.1, 0.9]

psi = {'1':psi1, '3':psi1, '5':psi1}
psi['2']=psi2
psi['4']=psi2

global ecf
ecf = [[1,0.45],[0.45,1]]


global edges
edges = [[1,2],[2,4],[2,5],[1,3],[3,6]]

#neighbors
global neighbors
def initialize_neighbors(edges):
	global neighbors
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

initialize_neighbors(edges)
print(neighbors)

global messages
def initialize_messages(edges):
	global messages
	messages = {}
	for [i,j] in edges:
		messages[str(i)+'-'+str(j)]=.1
		messages[str(j)+'-'+str(i)]=.1


initialize_messages(edges)
print(messages)
def update(edge):
	return	
