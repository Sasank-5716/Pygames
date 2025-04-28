# 🐍 Classic Snake Game 🕹️

A Python implementation of the iconic Snake game using Pygame. Grow your snake, avoid collisions, and chase high scores!

[![Python Version](https://img.shields.io/badge/Python-3.7+-blue?logo=python)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green?logo=python)](https://pygame.org)
![License](https://img.shields.io/badge/License-MIT-red)

---

## 🎮 Features

- **🔄 Screen Wrapping**: Snake reappears on opposite edges
- **🍎 Food Collection**: Grow longer with each bite
- **💀 Self-Collision**: Game over when hitting yourself
- **🎮 Restart System**: Quick replay with 'R' key
- **📊 Score Tracking**: Real-time score display

---

## 🖼️ Screenshots

![Gameplay](screenshot.png) *(Add your own screenshot here!)*

---

## 🛠️ Installation

**Clone and play instantly:**
Click the copy button in the top-right corner →
git clone https://github.com/yourusername/snake-game.git && cd snake-game

Install dependencies
pip install pygame

text

---

## 🚀 How to Play

1. **Arrow Keys**: Control snake direction
2. **Collect Red Food**: Grow your snake
3. **Avoid Self**: Don't bite your tail!
4. **Game Over?**: Press R to restart or Q to quit

---

## 🧠 Code Highlights

Core Movement Logic
def move(self):
self.x += self.dx
self.y += self.dy

text
# Screen wrapping
self.x = self.x % WIDTH
self.y = self.y % HEIGHT

self.body.insert(0, (self.x, self.y))
if len(self.body) > self.length:
    self.body.pop()
text

---

## ⚙️ Customization

- **Speed Control**: Adjust `clock.tick(10)` value
- **Grid Size**: Modify `self.size` in Snake/Food classes
- **Colors**: Edit RGB values in constants section
- **Difficulty**: Add wall collision by removing wrapping logic

---

## 🕹️ Gameplay Mechanics

- **Food Spawn**: Ensures never appears on snake
while (food.x, food.y) in snake.body:
food.respawn()

text
- **Collision Detection**: Precise coordinate checking
- **Score System**: +1 point per food collected

---

## 🤝 Contributing

1. **Fork** the repository
2. **Create** feature branch (`git checkout -b feature/NewPowerup`)
3. **Commit** changes (`git commit -m 'Add new powerups'`)
4. **Push** to branch (`git push origin feature/NewPowerup`)
5. **Open** pull request

---

## 🙌 Acknowledgments

- Inspired by **Nokia's Snake** (1997)
- **Pygame** documentation
- **Python** community resources

**Happy Slithering!** 🚀