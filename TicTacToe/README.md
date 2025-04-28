# ⭕ Tic-Tac-Toe Game ❌  
A classic two-player implementation of Tic-Tac-Toe built with Python and Pygame. Play against a friend on the same device!

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://python.org)  
[![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-green?logo=python)](https://pygame.org)  
![License](https://img.shields.io/badge/License-MIT-red)

---

## 🎮 Features  
- **👥 Two-Player Mode**: Alternate turns between X and O  
- **🏆 Win Detection**: Instant recognition of 3-in-a-row  
- **🎨 Minimalist Design**: Clean grid and smooth animations  
- **🔄 Restart Option**: Quick replay with one click  
- **📊 Score Tracking**: Wins for X and O displayed  

---

## 🖼️ Screenshots  
![Tic-Tac-Toe Gameplay](screenshot.png)  

---

## 🛠️ Installation  
**Clone and play:**  
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
pip install pygame

text

---

## 🚀 Running the Game  
python tictactoe.py

text

---

## 🕹️ How to Play  
1. **Players alternate turns**: X starts first  
2. **Click any empty square** to place your mark  
3. **First to get 3 in a row** (horizontal, vertical, or diagonal) wins  
4. **Press R** to restart the game  
5. **Press Q** to quit  

---

## ⚙️ Project Structure  
tic-tac-toe/
│
├── tictactoe.py # Main game logic
├── requirements.txt
├── README.md
└── screenshot.png 

text

---

## 🧠 Code Highlights  
- **Grid System**: 3x3 board with precise click detection  
Calculate grid position from mouse click
col = mouse_pos // (WIDTH // 3)
row = mouse_pos // (HEIGHT // 3)

text
- **Win Condition Check**:  
Check all 8 possible winning combinations
win_conditions = [
# Rows
[(0,0), (0,1), (0,2)],
[(1,0), (1,1), (1,2)],
[(2,0), (2,1), (2,2)],
# Columns
[(0,0), (1,0), (2,0)],
# ... etc ...
]

text
- **Restart Logic**: Reset board with one keypress  
if event.key == pygame.K_r:
board = [[None for _ in range(3)] for _ in range(3)]

text

---

## 🛠️ Customization  
- **Player Color**: Modify X (red) and O (blue) RGB values  
- **Grid Size**: Change WIDTH/HEIGHT for bigger board  
- **AI Opponent**: Add single-player mode with minimax algorithm  
def minimax(board, depth, is_maximizing):
# AI logic here

text

---

**May the best strategist win!** 🧠⚡
