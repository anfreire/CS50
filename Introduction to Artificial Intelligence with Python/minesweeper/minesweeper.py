import itertools
import random
import copy


class Minesweeper():
	"""
	Minesweeper game representation
	"""

	def __init__(self, height=8, width=8, mines=8):

		# Set initial width, height, and number of mines
		self.height = height
		self.width = width
		self.mines = set()

		# Initialize an empty field with no mines
		self.board = []
		for i in range(self.height):
			row = []
			for j in range(self.width):
				row.append(False)
			self.board.append(row)

		# Add mines randomly
		while len(self.mines) != mines:
			i = random.randrange(height)
			j = random.randrange(width)
			if not self.board[i][j]:
				self.mines.add((i, j))
				self.board[i][j] = True

		# At first, player has found no mines
		self.mines_found = set()

	def print(self):
		"""
		Prints a text-based representation
		of where mines are located.
		"""
		for i in range(self.height):
			print("--" * self.width + "-")
			for j in range(self.width):
				if self.board[i][j]:
					print("|X", end="")
				else:
					print("| ", end="")
			print("|")
		print("--" * self.width + "-")

	def is_mine(self, cell):
		i, j = cell
		return self.board[i][j]

	def nearby_mines(self, cell):
		"""
		Returns the number of mines that are
		within one row and column of a given cell,
		not including the cell itself.
		"""

		# Keep count of nearby mines
		count = 0

		# Loop over all cells within one row and column
		for i in range(cell[0] - 1, cell[0] + 2):
			for j in range(cell[1] - 1, cell[1] + 2):

				# Ignore the cell itself
				if (i, j) == cell:
					continue

				# Update count if cell in bounds and is mine
				if 0 <= i < self.height and 0 <= j < self.width:
					if self.board[i][j]:
						count += 1

		return count

	def won(self):
		"""
		Checks if all mines have been flagged.
		"""
		return self.mines_found == self.mines


class Sentence():
	"""
	Logical statement about a Minesweeper game
	A sentence consists of a set of board cells,
	and a count of the number of those cells which are mines.
	"""

	def __init__(self, cells, count):
		self.cells = set(cells)
		self.count = count
		self.mines = set()
		self.safes = set()
		self.update()

	def update(self):
		'''
		Updates the sentence based on the known mines and safes.
		If the sentence has the number of cells equal to the number of mines, then all the remaining cells are mines.
		If the sentence has the count of 0, then all the cells are safe.
		'''
		if len(self.cells) == self.count:
			for cell in copy.copy(self.cells):
				self.mark_mine(cell)
		elif self.count == 0:
			for cell in copy.copy(self.cells):
				self.mark_safe(cell)

	def __eq__(self, other):
		return self.cells == other.cells and self.count == other.count

	def __str__(self):
		return f"{self.cells} = {self.count}"

	def known_mines(self):
		"""
		Returns the set of all cells in self.cells known to be mines.
		"""
		return self.mines

	def known_safes(self):
		"""
		Returns the set of all cells in self.cells known to be safe.
		"""
		return self.safes

	def mark_mine(self, cell):
		"""
		Updates internal knowledge representation given the fact that
		a cell is known to be a mine.
		"""
		if cell in self.cells:
			self.cells.remove(cell)
			self.count -= 1
			self.mines.add(cell)
			self.update()

	def mark_safe(self, cell):
		"""
		Updates internal knowledge representation given the fact that
		a cell is known to be safe.
		"""
		if cell in self.cells:
			self.cells.remove(cell)
			self.safes.add(cell)
			self.update()


class MinesweeperAI():
	"""
	Minesweeper game player
	"""

	def __init__(self, height=8, width=8):

		# Set initial height and width
		self.height = height
		self.width = width

		# Keep track of which cells have been clicked on
		self.moves_made = set()

		# Keep track of cells known to be safe or mines
		self.mines = set()
		self.safes = set()

		# List of sentences about the game known to be true
		self.knowledge = []
		'''
		Keeps trach of the unrevealed cells
		'''
		self.map = []
		for _ in range(self.height):
			self.map.append(list(itertools.repeat(False, self.width)))

	@property
	def possible_moves(self):
		'''
		Returns a list of all possible moves
		'''
		possible_moves = list()
		for x in range(self.height):
			for y in range(self.width):
				if self.map[x][y] == False:
					possible_moves.append((x, y))
		return possible_moves

	@property
	def	copy_knowledge(self):
		'''
		Returns a copy of the knowledge
		'''
		return copy.deepcopy(self.knowledge)

	def mark_mine(self, cell):
		"""
		Marks a cell as a mine, and updates all knowledge
		to mark that cell as a mine as well.
		"""
		self.mines.add(cell)
		for sentence in self.knowledge:
			sentence.mark_mine(cell)

	def mark_safe(self, cell):
		"""
		Marks a cell as safe, and updates all knowledge
		to mark that cell as safe as well.
		"""
		self.safes.add(cell)
		for sentence in self.knowledge:
			sentence.mark_safe(cell)

	def get_neighbors(self, cell):
		'''
		Returns a set of all neighbors of a cell
		'''
		neighbors = set()
		for x in range(self.height):
			for y in range(self.width):
				if x >= cell[0] - 1 and x <= cell[0] + 1:
					if y >= cell[1] - 1 and y <= cell[1] + 1:
						neighbors.add((x, y))
		neighbors.remove(cell)
		return neighbors

	def update_knowledge(self):
		'''
		Updates the knowledge base based on the current game state
		'''
		sentences_to_remove = list()
		'''
			Updates the sentence **More info on the update method of the Sentence class**
			Iterates through all the sentences in the knowledge base
			Marks all the mines and safes, currently known in the AI, in the sentence
			Marks all the mines and safes, currently known in the sentence, in the AI
			Updates the sentence again
		'''
		for sentence in self.knowledge:
			sentence.update()
			for mine in self.mines:
				sentence.mark_mine(mine)
			for safe in self.safes:
				sentence.mark_safe(safe)
			for mine in sentence.mines:
				self.mark_mine(mine)
			for safe in sentence.safes:
				self.mark_safe(safe)
			sentence.update()
		'''
			Iterates through all the sentences in the knowledge base
			Removes duplicates, by comparing the lenght of the cells and making sure the intersection of the cells is the same
			Removes sentences with no cells
			The removal its done after the loop, to avoid changing the list while iterating through it
		'''
		for i in range(len(self.knowledge)):
			for j in range(len(self.knowledge)):
				if i == j:
					continue
				elif len(self.knowledge[i].cells) == len(self.knowledge[j].cells) and \
					self.knowledge[i].cells.intersection() == self.knowledge[j].cells.intersection():
					sentences_to_remove.append(self.knowledge[i])
				elif len(self.knowledge[i].cells) == 0:
					sentences_to_remove.append(self.knowledge[i])
		for sentence in sentences_to_remove:
			if sentence in self.knowledge:
				self.knowledge.remove(sentence)

	def create_sentences(self):
		'''
		Crosses all the sentences in the knowledge base and creates new sentences
		Every new sentence passes through a update method **More info on the update method of the Sentence class**
		After updating the sentence, updates the knowledge base with the sentence "Knowledge" (Mines and Safes)
		'''
		mines = set()
		safes = set()
		for one_sentence in self.copy_knowledge:
			for another_sentence in self.copy_knowledge:
				if one_sentence == another_sentence:
					continue
				if one_sentence.cells.issubset(another_sentence.cells):
					new_cells = another_sentence.cells.difference(one_sentence.cells)
					new_count = another_sentence.count - one_sentence.count
					new_sentence = Sentence(new_cells, new_count)
					new_sentence.update()
					if new_sentence not in self.knowledge:
						self.knowledge.append(new_sentence)
					for mine in new_sentence.mines:
						mines.add(mine)
					for safe in new_sentence.safes:
						safes.add(safe)
				if another_sentence.cells.issubset(one_sentence.cells):
					new_cells = one_sentence.cells.difference(another_sentence.cells)
					new_count = one_sentence.count - another_sentence.count
					new_sentence = Sentence(new_cells, new_count)
					new_sentence.update()
					if new_sentence not in self.knowledge:
						self.knowledge.append(new_sentence)
					for mine in new_sentence.mines:
						mines.add(mine)
					for safe in new_sentence.safes:
						safes.add(safe)
		for mine in mines:
			self.mark_mine(mine)
		for safe in safes:
			self.mark_safe(safe)


	def add_knowledge(self, cell, count):
		"""
		Called when the Minesweeper board tells us, for a given
		safe cell, how many neighboring cells have mines in them.

		This function should:
			1) mark the cell as a move that has been made
			2) mark the cell as safe
			3) add a new sentence to the AI's knowledge base
			   based on the value of `cell` and `count`
			4) mark any additional cells as safe or as mines
			   if it can be concluded based on the AI's knowledge base
			5) add any new sentences to the AI's knowledge base
			   if they can be inferred from existing knowledge
		"""
		'''
			Marks the cell as a move that has been made
			Sets the map to track the moves made, to True
			Goes through a loop to update the and create new sentences
			The loop will go through at least two times, to make sure that all the sentences are updated, because the stopper **on the line below**
		is based on the length of the knowledge base, and might not be enough to update all the sentences
			The loop stops when the length of the knowledge base does not change
		'''
		self.moves_made.add(cell)
		self.map[cell[0]][cell[1]] = True
		neighbors = self.get_neighbors(cell)
		sentence = Sentence(neighbors, count)
		previous_knowledge_length = len(self.knowledge)
		self.knowledge.append(sentence)
		while True:
			self.update_knowledge()
			self.create_sentences()
			if previous_knowledge_length == len(self.knowledge):
				break
			previous_knowledge_length = len(self.knowledge)

	def make_safe_move(self):
		"""
		Returns a safe cell to choose on the Minesweeper board.
		The move must be known to be safe, and not already a move
		that has been made.

		This function may use the knowledge in self.mines, self.safes
		and self.moves_made, but should not modify any of those values.
		"""
		'''
			Checks if there are any safe moves, and if there are, returns one of them
			Else, returns None
		'''
		safe_moves = self.safes.difference(self.moves_made)
		if len(safe_moves) > 0:
			for move in safe_moves:
				return move

	def make_random_move(self):
		"""
		Returns a move to make on the Minesweeper board.
		Should choose randomly among cells that:
			1) have not already been chosen, and
			2) are not known to be mines
		"""
		'''
			Checks if there are any possible moves, and if there are, returns one of them
			by possible moves, I mean moves that are not mines and moves that have not been made
			Else, returns None
		'''
		possible_moves = set()
		for x in range(self.height):
			for y in range(self.width):
				possible_moves.add((x, y))
		possible_moves = possible_moves.difference(self.moves_made)
		possible_moves = possible_moves.difference(self.mines)
		if len(possible_moves) > 0:
			for move in possible_moves:
				return move

'''
Notes:

This AI uses a knowledge base, which is a list of sentences, to keep track of the mines and safes
The sentences are updated and created based on the mines and safes that are found
The Minesweeper game itself is a game of luck, so the AI will not always win, but it will win most of the time
'''