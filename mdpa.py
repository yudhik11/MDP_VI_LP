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
	value = step + max_val
	return value, [n_val, e_val, w_val, s_val]

def VI(rows, cols, numend, end_states, numwall, walls, start, step):
	global board_copy 
	board_copy = copy.deepcopy(board)
	for i in range(100):
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
		if flag == rows * cols:
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
	global util
	util = copy.deepcopy(board)
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
			board[i][j]-=util[i][j]
	
	line1 = raw_input().split(' ')
	start = (int(line1[0]),int(line1[1]))
	step = raw_input()
	step = float(step)
	VI(rows, cols, numend, end_states, numwall, walls, start, step)
	for q in board:
		for kk in q:
			print (kk,end = "\t")
		print()
if __name__ == '__main__':
	main()
