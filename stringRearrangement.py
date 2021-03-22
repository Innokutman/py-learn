# https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9
def stringsRearrangement(inputArray):
    for p in permutation(inputArray):
        ans = True
        for i in range(len(p) - 1):
            if charDiff(p[i], p[i + 1]) != 1:
                ans = False
                break
        if ans:
            return ans
    return False
def charDiff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count
# def splitString(word):
#     return [c for c in word]
def permutation(inputArray):
    if len(inputArray) == 0:
        return []
    elif len(inputArray) == 1:
        return [inputArray]
    l = []
    for i in range(len(inputArray)):
        j = inputArray[i]
        newList = inputArray[:i] + inputArray[i+1:]
        for p in permutation(newList):
            l.append([j] + p)
    return l
# def stringsRearrangement(inputArray):
#     #FIRST
#     #Note that the task is equivalent to finding a Hamiltonian path in the graph where the nodes are our strings
#     #and there is an edge where the distance between two strings is one.
#     #Hamiltonian path is NP-complete but this possibly is not because we are looking at a specific subset of all graphs.
#     #Intuitively: incomplete hypercubes but I have not constructed a proof.
#     #I have come to expect that the most upvoted solution to these is a fancy oneliner by someone who just 'gets' it.
#     #So I assume my solution building on that intuition is too complicated
    
#     #SECOND
#     #Note that in  ["aaaa", "aaab", "aabb", "abbb", "abab", "baab"] every vertex except the first and the last have
#     #two neighbours and yet there is no solution. None of the sample tests is of that kind.
#     #This means that the sample tests pass with a way to easy solution.
    
#     #THIRD
#     #Note that the hypercube can be broken into two or more parts like so: 
#     #["ccaa", "ccab", "ccba", "ccbb", "ddaa", "ddab", "ddba", "ddbb"]
#     #This test case will also fail with the overly simple solution which all the other samples pass.
    
#     #FOURTH
#     #https://app.codesignal.com/forum/btzBAiv9irK3yc4RT
    
#     #FIFTH
#     #Now that I have actually seen the most upvoted solution it uses permutations (i. e. brute force).
#     #I am suprised that this is fast enough.
#     #It is pretty obvious that my approach on average considers far less options than the brute force approach
#     #but it burns more time on every permutation to find shortcuts
#     #so in the end I think my approach is faster for larger N
    
    
#     def recursion(N, n, k, adjaceny, adj, tab):
#         if n == (N-1):
#             return n
        
#         #Keep tab of all vertices already used as a starting vertice. 
#         #This solution starts over with the last vertice of a dead end as the start.
#         #Empirically it works pretty well on the tests. 
#         #What this means is that if the graph broken into parts, 
#         #starting vertices not reachable from the 0-vertex are not even considered.
#         if n == 0:
#             tab = tab | set([k])
            
#         #Remove k from all further considerations
#         adj2 = [row[:] for row in adj]
#         for j in range(N):
#             adj2[j][k] = False
#             adj2[k][j] = False
        
#         max = n
#         for j in range(N):
#             if adj[k][j]:
#                 #Obviously we want to search depth first so that we can stop if we complete a path.
#                 u = recursion(N, n+1, j, adjaceny, adj2, tab)
#                 if u == (N-1):
#                     return u
                
#                 #Failing to find a solution below j, what about solutions that start with j?
#                 if j not in tab:
#                     v = recursion(N, 0, j, adjaceny, adjaceny, tab)
#                     if v == (N-1):
#                         return v
#                     if v > max:
#                         max = v     
#                 if u > max:
#                     max = u
#         #This is just cosmetics.
#         return max
                    
#     N = len(inputArray)
    
#     adjaceny = [[False]*N for i in range(N)]
    
#     for j in range(N-1):
#         for i in range(j+1, N):
#             hamming = sum(u != v for u, v in zip(inputArray[i], inputArray[j]))
#             adjaceny[i][j] = (hamming==1)
#             adjaceny[j][i] = (hamming==1)
    
#     #At most two vertices can have degree one. The first and the last in the sequence. 
#     #All other vertices need to have degree > 1
#     #We can use that property to optimise
#     degOne = set()
#     for i in range(N):
#         s = sum (adjaceny[i]) 
#         if s == 0:
#             return False
#         if s == 1:
#             degOne = degOne | set([i])
#     if len(degOne) > 2:
#         return False
    
#     tab = set() if len(degOne) == 0 else set(range(N)) - degOne
    
#     p = recursion(N, 0, 0, adjaceny, adjaceny, tab)
    
#     return (N-1) == p