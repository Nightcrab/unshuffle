import numpy as np
import math
import copy

def fy_shuffle(seed, l):
	a = copy.copy(l)
	n = len(a)
	np.random.seed(seed)
	randomnum = np.random.random
	i = n-1
	while (i>0):
		i -= 1
		j = math.floor(randomnum() * (i + 1))
		tmp = a[i]
		a[i] = a[j]
		a[j] = tmp
	return a

def unshuffle(shuffle, seed, shuffled):
	l = len(shuffled)
	unshuffled = [None]*l
	identity = [x for x in range(l)]
	mapping = shuffle(seed, identity) #index,value corresponds to (new index), (old index)
	for i in range(l): #loop through mapping
		new, old = [i, mapping[i]]#we are looking at position i which is the new position. mapping[i] is the old position.
		unshuffled[old] = shuffled[new]#take the new position to the old position to unshuffle
	return unshuffled

A = fy_shuffle(1234, list("abcdefghijklmnopqrstuvwxyz"))
print(str(A)) 
A = unshuffle(fy_shuffle, 1234, A)
print(str(A)) 