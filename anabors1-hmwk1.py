#Austin Nabors
#COMP 4030 - Assignment 1 

#Fake coin finder
import math
import random

def get_coins():
	coins = [2]*30
	coins[random.randint(0, 29)] -= 1
	return coins

#---------------------------------
def compare_coins(coinA, coinB):
	if coinA > coinB:
		return 1
	elif coinA < coinB:
		return -1
	else:
		return 0
#---------------------------------
def sort_coints(coins):
	
	print(coins)

#------------------------------------------------
def min_between(L, i, j):
	min_index = i
	# Loop from i+1 to j to find the min
	for k in range(i+1, j+1):
		if L[k] < L[min_index]:
			min_index = k
	return min_index
#------------------------------------------------
def sortList(myList):
	for i in range(0, len(myList)-1):
		m = min_between(myList, i, len(myList)-1)
		myList[i], myList[m] = myList[m], myList[i]
#------------------------------------------------
def find_fake_coin(myList):
	sortList(A)
	return A[0]
#------------------------------------------------
def two_group_recursive(myList):
	if len(myList) == 1:
		return myList[0]
	elif len(myList) == 2:
		if myList[0] < myList[1]:
			return myList[0]
		else:
			return myList[1]
	half = math.floor(len(myList)/2)
	listA = myList[0:half]
	listB = myList[half:len(myList)]
	if sum(listA)/float(len(listA)) < sum(listB)/float(len(listB)):
		return two_group_recursive(listA)
	else:
		return two_group_recursive(listB)
#------------------------------------------------
def three_group_recursive(myList):
	if len(myList) == 1:
		return myList[0]
	elif len(myList) == 2:
		if myList[0] < myList[1]:
			return myList[0]
		else:
			return myList[1]
	third = math.floor(len(myList)/3)
	listA = myList[0:third]
	listB = myList[third:third*2]
	listC = myList[third*2:len(myList)]
	listAavg = sum(listA)/float(len(listA))
	listBavg = sum(listB)/float(len(listB))
	listCavg = sum(listC)/float(len(listC))
	if min(listAavg, listBavg, listCavg) == listAavg:
		return three_group_recursive(listA)
	elif min(listAavg, listBavg, listCavg) == listBavg:
		return two_group_recursive(listB)
	else: 
		return three_group_recursive(listC)
	
#------------------------------------------------

A = get_coins()
B = get_coins()
C = get_coins()


print("NEW LIST--------------------------------------------------")
print(A)
print("Using two groups: ", two_group_recursive(A))
print("Using three groups: ", three_group_recursive(A))

print("NEW LIST--------------------------------------------------")
print(B)
print("Using two groups: ", two_group_recursive(B))
print("Using three groups: ", three_group_recursive(B))

print("NEW LIST--------------------------------------------------")
print(C)
print("Using two groups: ", two_group_recursive(C))
print("Using three groups: ",+ three_group_recursive(C))
