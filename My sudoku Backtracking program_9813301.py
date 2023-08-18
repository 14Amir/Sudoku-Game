# A Backtracking program
# in Python to solve Sudoku problem

import math


# A Utility Function to print the Grid
def print_grid(arr):
	for i in range(n):
		for j in range(n):
			print (arr[i][j], end = " "),
		print ()

		
# Function to Find the entry in
# the Grid that is still not used
# Searches the grid to find an
# entry that is still unassigned. If
# found, the reference parameters
# row, col will be set the location
# that is unassigned, and true is
# returned. If no unassigned entries
# remains, false is returned.
# 'l' is a list variable that has
# been passed from the solve_sudoku function
# to keep track of incrementation
# of Rows and Columns
def find_empty_location(arr, l):
	for row in range(n):
		for col in range(n):
			if(arr[row][col]== 0):
				l[0]= row
				l[1]= col
				return True
	return False

# Returns a boolean which indicates
# whether any assigned entry
# in the specified row matches
# the given number.
def used_in_row(arr, row, num):
	for i in range(n):
		if(arr[row][i] == num):
			return True
	return False

# Returns a boolean which indicates
# whether any assigned entry
# in the specified column matches
# the given number.
def used_in_col(arr, col, num):
	for i in range(n):
		if(arr[i][col] == num):
			return True
	return False

# Returns a boolean which indicates
# whether any assigned entry
# within the specified nxn box
# matches the given number
def used_in_box(arr, row, col, num):
	for i in range(int(math.sqrt(n))):
		for j in range(int(math.sqrt(n))):
			if(arr[i + row][j + col] == num):
				return True
	return False

# Checks whether it will be legal
# to assign num to the given row, col
# Returns a boolean which indicates
# whether it will be legal to assign
# num to the given row, col location.
def check_location_is_safe(arr, row, col, num):
	
	# Check if 'num' is not already
	# placed in current row,
	# current column and current nxn box
	return (not used_in_row(arr, row, num) and
		(not used_in_col(arr, col, num) and
		(not used_in_box(arr, row - row % int(math.sqrt(n)),
						col - col % int(math.sqrt(n)), num))))

# Takes a partially filled-in grid
# and attempts to assign values to
# all unassigned locations in such a
# way to meet the requirements
# for Sudoku solution (non-duplication
# across rows, columns, and boxes)
def solve_sudoku(arr):
	
	# 'l' is a list variable that keeps the
	# record of row and col in
	# find_empty_location Function	
	l =[0, 0]
	
	# If there is no unassigned
	# location, we are done	
	if(not find_empty_location(arr, l)):
		return True
	
	# Assigning list values to row and col
	# that we got from the above Function
	row = l[0]
	col = l[1]
	
	# consider digits 1 to 9
	for num in range(1, n+1):
		
		# if looks promising
		if(check_location_is_safe(arr,
						row, col, num)):
			
			# make tentative assignment
			arr[row][col]= num

			# return, if success,
			# ya !
			if(solve_sudoku(arr)):
				return True

			# failure, unmake & try again
			arr[row][col] = 0
			
	# this triggers backtracking		
	return False

# Driver main function to test above functions
if __name__=="__main__":
 
    # n = 9
    
    n = int(input('n = '))
    c = int(input('c = '))

# creating a 2D array for the grid
    grid =[[0 for x in range(n)]for y in range(n)]
    
# assigning values to the grid
    for k in range(c):
      print('filled cell ',k+1,': ')
      i = int(input('i = '))
      j = int(input('j = '))
      grid[i][j] = int(input('value = '))



    # assigning values to the grid


# 4*4 (First)
    # grid = [[0, 1, 0, 0],[0, 0, 0, 3],
	#   [4, 0, 0, 0],[0, 0, 4, 0]]


# 4*4 (second)
    # grid = [[1, 0, 0, 0],[0, 0, 1, 0],
	#   [0, 4, 0, 0],[0, 0, 0, 3]]


# two same num in a row and in a col (no ans)
    # grid = [[1, 9, 3, 4, 5, 6, 7, 8, 9],
    #              [2, 8, 1, 0, 0, 0, 0, 0, 0], 
    #              [3, 7, 2, 0, 0, 0, 0, 0, 0], 
    #              [4, 6, 3, 0, 0, 0, 0, 0, 0], 
    #              [5, 5, 4, 0, 0, 0, 0, 0, 0],
    #              [6, 4, 5, 0, 0, 0, 0, 0, 0],
    #              [7, 3, 6, 0, 0, 0, 0, 0, 0],
    #              [8, 2, 7, 0, 0, 0, 0, 0, 0],
    #              [9, 1, 8, 0, 0, 0, 0, 0, 0]]


    # correct one (9*9)
    # grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #       [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #       [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #       [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #       [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #       [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #       [0, 0, 5, 2, 0, 6, 3, 0, 0]]

# ans
# 3 1 6 5 7 8 4 9 2 
# 5 2 9 1 3 4 7 6 8 
# 4 8 7 6 2 9 5 3 1 
# 2 6 3 4 1 5 9 8 7 
# 9 7 4 8 6 3 1 2 5 
# 8 5 1 7 9 2 6 4 3 
# 1 3 8 9 4 7 2 5 6 
# 6 9 2 3 5 1 8 7 4 
# 7 4 5 2 8 6 3 1 9


# another correct one (9*9)
    # grid = [[0, 4, 0, 7, 0, 0, 1, 3, 0],
    #        [0, 0, 2, 0, 0, 0, 6, 0, 0],
    #        [0, 0, 0, 4, 2, 0, 0, 0, 0],
    #        [6, 0, 0, 0, 0, 2, 0, 0, 3],
    #        [2, 3, 1, 0, 7, 0, 0, 8, 0],
    #        [4, 0, 0, 3, 1, 0, 0, 0, 0],
    #        [0, 7, 0, 0, 0, 8, 0, 0, 0],
    #        [0, 0, 6, 0, 3, 0, 0, 0, 4],
    #        [8, 9, 0, 0, 5, 0, 0, 0, 6]]
  
# ans
# [9, 4, 5, 7, 8, 6, 1, 3, 2]
# [7, 1, 2, 5, 9, 3, 6, 4, 8]
# [3, 6, 8, 4, 2, 1, 5, 7, 9]
# [6, 5, 7, 8, 4, 2, 9, 1, 3]
# [2, 3, 1, 6, 7, 9, 4, 8, 5]
# [4, 8, 9, 3, 1, 5, 2, 6, 7]
# [5, 7, 4, 2, 6, 8, 3, 9, 1]
# [1, 2, 6, 9, 3, 7, 8, 5, 4]
# [8, 9, 3, 1, 5, 4, 7, 2, 6]



  

# 25 * 25 correct one
    # grid = [
    # [1,0,4,0,25,0,19,0,0,10,21,8,0,14,0,6,12,9,0,0,0,0,0,0,5],
    # [5,0,19,23,24,0,22,12,0,0,16,6,0,20,0,18,0,25,14,13,10,11,0,1,15],
    # [0,0,0,0,0,0,21,5,0,20,11,10,0,1,0,4,8,24,23,15,18,0,16,22,19],
    # [0,7,21,8,18,0,0,0,11,0,5,0,0,24,0,0,0,17,22,1,9,6,25,0,0],
    # [0,13,15,0,22,14,0,18,0,16,0,0,0,4,0,0,0,19,0,0,0,0,24,20,21,17],
    # [12,0,11,0,6,0,0,0,0,15,0,0,0,0,21,25,19,0,4,0,22,14,0,20,0],
    # [8,0,0,21,0,16,0,0,0,2,0,3,0,0,0,0,17,23,18,22,0,0,0,24,6],
    # [4,0,14,18,7,9,0,22,21,19,0,0,0,2,0,5,0,0,0,6,16,15,0,11,12],
    # [22,0,24,0,23,0,0,11,0,7,0,0,4,0,14,0,2,12,0,8,5,19,0,25,9],
    # [20,0,0,0,5,0,0,0,0,17,9,0,12,18,0,1,0,0,7,24,0,0,0,13,4],
    # [13,0,0,5,0,2,23,14,4,18,22,0,17,0,0,20,0,1,9,21,12,0,0,8,11],
    # [14,23,0,24,0,0,0,0,0,0,0,0,20,25,0,3,4,13,0,11,21,9,5,18,22],
    # [7,0,0,11,17,20,24,0,0,0,3,4,1,12,0,0,6,14,0,5,25,13,0,0,0],
    # [0,0,16,9,0,17,11,7,10,25,0,0,0,13,6,0,0,18,0,0,19,4,0,0,20],
    # [6,15,0,19,4,13,0,0,5,0,18,11,0,0,9,8,22,16,25,10,7,0,0,0,0],
    # [0,0,0,2,0,0,10,19,3,0,1,0,22,9,4,11,15,0,20,0,0,8,23,0,25],
    # [0,24,8,13,1,0,0,4,20,0,17,14,0,0,18,0,16,22,5,0,11,0,10,0,0],
    # [23,10,0,0,0,0,0,0,18,0,6,0,16,0,0,17,1,0,13,0,0,3,19,12,0],
    # [25,5,0,14,11,0,17,0,8,24,13,0,19,23,15,9,0,0,12,0,20,0,22,0,7],
    # [0,0,17,4,0,22,15,0,23,11,12,25,0,0,0,0,18,8,0,7,0,0,14,0,13],
    # [19,6,23,22,8,0,0,1,25,4,14,2,0,3,7,13,10,11,16,0,0,0,0,0,0],
    # [0,4,0,17,0,3,0,24,0,8,20,23,11,10,25,22,0,0,0,12,13,2,18,6,0],
    # [0,0,7,16,0,0,6,17,2,21,0,18,0,0,0,19,0,0,8,0,0,0,0,4,0],
    # [18,9,25,1,2,11,0,0,13,22,4,0,21,0,5,0,23,7,0,0,15,0,3,0,8],
    # [0,21,10,0,0,12,0,20,16,0,19,0,0,0,0,15,14,4,2,18,23,25,11,7,0]]


	
	# if success print the grid
    if(solve_sudoku(grid)):
	    print_grid(grid)
    else:
	    print ("Unsolvable CSP!")
 

