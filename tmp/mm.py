import math

def minimax (
    curDepth,               # current depth in game tree
    nodeIndex,              # index of current node in scores[]
    maxTurn,                # True if player is maximizer, False if minimizer
    scores,                 # scores[] represents leaves of game tree
    targetDepth             # depth of game tree
):

	# targetDepth reached
	if (curDepth == targetDepth): 
		return scores[nodeIndex]
	
	if (maxTurn):
		return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth), 
			minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
	
	else:
		return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth), 
			minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )
	

scores = [3, 12, 8, 2, 4, 6, 4, 5, 2]
treeDepth = 2

print("Value :")
print(minimax(0, 0, True, scores, treeDepth))
