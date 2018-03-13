from __future__ import print_function
import copy, time
def update(row, col, step, walls):
	# N E W S
	nbrs = [(row - 1, col), (row, col+1), (row, col-1), (row+1, col) ]
	utility = []
	for i in range(4):
		if nbrs[i][0] < 0 or nbrs[i][1] < 0 or nbrs[i][0] > len(board)-1 \
			or nbrs[i][1] > len(board[0])-1 or nbrs[i] in walls:
			utility.append(board_copy[row][col] + util[row][col] )
		else:
			utility.append(board_copy[nbrs[i][0]][nbrs[i][1]] + util[nbrs[i][0]][nbrs[i][1]])

	e_val = 0.8 * utility[1] + 0.1 * utility[0] + 0.1 * utility[3] 
	w_val = 0.8 * utility[2] + 0.1 * utility[0] + 0.1 * utility[3] 
	n_val = 0.8 * utility[0] + 0.1 * utility[1] + 0.1 * utility[2] 
	s_val = 0.8 * utility[3] + 0.1 * utility[1] + 0.1 * utility[2]
	max_val = max(e_val, w_val, n_val, s_val)
	print( row, col, "    N = ", n_val+step," E = ", e_val+step,\
	" W = ", w_val+step, " S = ",s_val+step)
	value = step + max_val
	return value, [n_val, e_val, w_val, s_val]

def final_policy(start, end_states, vals):
	curr = [ start[0], start[1] ]
	while (curr[0], curr[1]) not in end_states:
		print( curr, end =" --> ")
		news = vals[curr[0]][curr[1]]
		max_value = max(news)
		max_index = news.index(max_value)
		if max_index == 0:
			curr[0] -= 1
		if max_index == 1:
			curr[1] += 1
		if max_index == 2:
			curr[1] -= 1
		if max_index == 3:
			curr[0] += 1

	print( curr)
	print("-"*70)

def policy(start, end_states, vals, walls):
	print("POLICY\n")
	for i in range(len(board)):
		for j in range(len(board[0])):
			if (i,j) in walls:
				print( "W", end = "\t")
			elif (i,j) in end_states:
				print( (board[i][j]), end = "\t")
			else:
				max_value = max(vals[i][j])
				max_index = vals[i][j].index(max_value)
				if max_index == 0:
					print( "NORTH", end="\t")
				if max_index == 1:
					print( "EAST", end="\t")
				if max_index == 2:
					print( "WEST", end="\t")
				if max_index == 3:
					print( "SOUTH", end="\t")
		print()
	print("-"*70)

def VI(rows, cols, numend, end_states, numwall, walls, start, step):
	global board_copy 
	board_copy = copy.deepcopy(board)
	for i in range(100):
		print("-"*70)
		print("Iteration - ",i+1,"\n")
		flag = 0
		vals = []
		for row in range(rows):
			vals.append([])
			for col in range(cols):
				vals[row].append([])
		for row in range(rows):
			for col in range(cols):
				if (row, col) in end_states or (row, col) in walls:
					flag+=1
					continue
				board[row][col], vals[row][col] = update(row, col, step, walls)
				if ((board[row][col] < 1.01 * board_copy[row][col]) \
					and (board[row][col] > 0.99 * board_copy[row][col])) or \
					((board[row][col] > 1.01 * board_copy[row][col]) \
					and (board[row][col] < 0.99 * board_copy[row][col])) :
					flag += 1
		print( "\nBoard\n")
		for q in board:
			for kk in q:
				print (kk, end="\t")
			print()
		print()
		policy(start, end_states, vals, walls)
		print("\n\n\n\n\n\n")
		if flag == rows * cols:
			final_policy(start, end_states, vals)
			return
		for row in range(rows):
			for col in range(cols):
				if (row, col) in end_states or (row, col) in walls:
					continue
				board_copy[row][col] = board[row][col]

def main():
	line1 = raw_input().split(' ')
	rows = int(line1[0])
	cols = int(line1[1])
	global board 
	board= []
	for i in range(rows):
		line = raw_input().split(' ')
		board.append([])
		for j in range(cols):
			board[i].append(float(line[j]))
	print(board)
	global util
	util = copy.deepcopy(board)
	print (util)
	line1 = raw_input().split(' ')
	numend = int(line1[0])
	numwall = int(line1[1])
	end_states = []
	walls = []
	for i in range(numend):
		line1 = raw_input().split(' ')
		end_states.append((int(line1[0]),int(line1[1])))
		util[int(line1[0])][int(line1[1])] = 0
	for i in range(numwall):
		line1 = raw_input().split(' ')
		walls.append((int(line1[0]),int(line1[1])))
	for i in range(rows):
		for j in range(cols):
			board[i][j] -= util[i][j]
	
	line1 = raw_input().split(' ')
	start = (int(line1[0]),int(line1[1]))
	step = raw_input()
	step = float(step)
	print ("board")
	for q in board:
		for kk in q:
			print (kk,end = "\t")
		print()
	print("utility")
	for q in util:
		for kk in q:
			print (kk,end = "\t")
		print()
	print()

	VI(rows, cols, numend, end_states, numwall, walls, start, step)
	print()
	print ("BOARD")
	for q in board:
		for kk in q:
			print (kk,end = "\t")
		print()
if __name__ == '__main__':
	main()
