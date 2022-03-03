# There are N courses, labelled from 1 to N.
# We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.
# In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.
# Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.


def minimumSemesters(self, N, relations):
    """
    :type N: int
    :type relations: List[List[int]]
    :rtype: int
    """
    # given a directed graph, traverse as quickly as possible
    
    # I would first find the indegree = 0 of the graph
    # add it to a queue
    # how to make sure that all of the prerequesite courses are taken, maybe 
    # create a parent child hashmap and create an indegree map and decrement the indegree for each parent that takes the course
    # once a child's indegree becomes 0, set its semestre count to be parent's semestre count + 1 and add it to the queue
    
    # first create the graph of course
    g = {}
    ind = {}
    for i in range(1, N + 1):
	    g[i] = list()
	    ind[i] = 0
	
    for p, c in relations:
	    g[p].append(c)
	    ind[c] += 1
    
    q = deque([])
    for v, indegree in ind.items():
		if indegree == 0:
			q.append((v, 1))
    
    count = 0
    max_semestre = 1
    while q:
	    curr_node, curr_semestre = q.popleft()
	    max_semestre = max(max_semestre, curr_semestre)
	    count += 1
	    for child in g[curr_node]:
	        ind[child] -= 1
	        if ind[child] == 0:
		    q.append((child, curr_semestre + 1))

    return -1 if count != N else max_semestre
