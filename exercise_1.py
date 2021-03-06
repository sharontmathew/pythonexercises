# -*- coding: utf-8 -*-
"""exercise 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TD6x_4pvt-XmZWr5ROxjOpO7QlM0eCmv
"""

# function which return reverse of a string
 
def isPalindrome(word):
    return word == word[::-1]
 
 
# Driver code
word = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

# Insertion Sort

# Function to do insertion sort
def insertionSort(list):

	# Traverse through 1 to len(arr)
	for i in range(1, len(list)):

		key = list[i]

		# Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
		j = i-1
		while j >=0 and key < list[j] :
				list[j+1] = list[j]
				j -= 1
		list[j+1] = key


list = [1, 11, 10, 5, 6]
insertionSort(list)
print ("Sorted array is:")
for i in range(len(list)):
	print ("%d" %list[i])

#Merge sort

def mergeSort(nlist):
    #with the help of Spliting
    print("Splitting ",nlist)
    if len(nlist)>1:
        #Dividing the list into two
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    #Merging the list        
    print("Merging ",nlist)

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)

#Total number of  triplets in a list with given sum 0

#importing the library
from itertools import combinations
  
def findTriplets(lst, key):
  def valid(val):
    return sum(val) == key
  return list(filter(valid, list(combinations(lst, 3))))
  

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(findTriplets(list, 10))

#list concatenation


test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

#concatenation
for i in test_list2 :
	test_list1.append(i)

# Printing concatenated list
print ("Concatenated list using naive method : " + str(test_list1))

#list to dictionary

def Convert(lst):
	res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
	return res_dct
		
#dictionary
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))

# Add two matrices

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]
	
Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]
	

result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)):

# iterate through columns
  for j in range(len(X[0])):
    result[i][j] = X[i][j] + Y[i][j]

for r in result:
	print(r)

#Binary search tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    
    if not nums:
        return None
    mid_val = len(nums)//2
    node = TreeNode(nums[mid_val])
    node.left = sorted_array_to_bst(nums[:mid_val])
    node.right = sorted_array_to_bst(nums[mid_val+1:])
    return node

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
    
result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
preOrder(result)

#delete a node from binary search tree

class Solution:
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
 
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
 
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
 
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
 
        return root

import pandas as pd
import numpy as np

#iporting the dataset using the function pd.read_csv
data = pd.read_csv("/content/drive/MyDrive/DataSets/twitter-sentiments.csv")
data.head(10)