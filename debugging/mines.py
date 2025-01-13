#!/usr/bin/python3
import random
import os

# Clear the screen for a clean game interface
def clear_screen():
os.system('cls' if os.name == 'nt' else 'clear')

# Minesweeper game class
class Minesweeper:
def __init__(self, width=10, height=10, mines=10):
self.width = width
self.height = height
self.total_cells = width * height
self.mines = set(random.sample(range(self.total_cells), mines))
self.non_mine_cells = self.total_cells - mines  # Calculate non-mine cells
self.field = [[' ' for _ in range(width)] for _ in range(height)]
self.revealed = [[False for _ in range(width)] for _ in range(height)]
self.revealed_cells = 0  # Keep track of revealed cells

 # Print the game board
 def print_board(self, reveal=False):
clear_screen()
print('  ' + ' '.join(str(i) for i in range(self.width)))
for y in range(self.height):
print(y, end=' ')
for x in range(self.width):
if reveal or self.revealed[y][x]:
if (y * self.width + x) in self.mines:
print('*', end=' ')
else:
count = self.count_mines_nearby(x, y)
print(count if count > 0 else ' ', end=' ')
else:
print('.', end=' ')
print()

# Count nearby mines for a given cell
def count_mines_nearby(self, x, y):
count = 0
for dx in [-1, 0, 1]:
for dy in [-1, 0, 1]:
nx, ny = x + dx, y + dy
if 0 <= nx < self.width and 0 <= ny < self.height:
if (ny * self.width + nx) in self.mines:
count += 1
return count

# Reveal a cell and check win/loss conditions
def reveal(self, x, y):
if self.revealed[y][x]:
return True  # Skip already revealed cells

# Check if the cell is a mine
if (y * self.width + x) in self.mines:
return False

# Reveal the cell
self.revealed[y][x] = True
self.revealed_cells += 1  # Increment revealed cells

# Check for win condition
if self.revealed_cells == self.non_mine_cells:
self.print_board(reveal=True)
print("Congratulations! You've won the game.")
exit()

# If the cell has no nearby mines, reveal adjacent cells recursively
if self.count_mines_nearby(x, y) == 0:
for dx in [-1, 0, 1]:
for dy in [-1, 0, 1]:
nx, ny = x + dx, y + dy
if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
self.reveal(nx, ny)
return True

# Main game loop
def play(self):
while True:
self.print_board()
try:
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
if not self.reveal(x, y):
self.print_board(reveal=True)
print("Game Over! You hit a mine.")
break
except ValueError:
print("Invalid input. Please enter numbers only.")

# Run the game
if __name__ == "__main__":
game = Minesweeper()
game.play()
