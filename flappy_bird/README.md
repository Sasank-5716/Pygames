# 🐦 Flappy Bird Clone 🎮

A Python implementation of the classic Flappy Bird game using Pygame. Navigate through pipes and aim for the high score!

[![Python Version](https://img.shields.io/badge/Python-3.7+-blue?logo=python)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green?logo=python)](https://pygame.org)
![License](https://img.shields.io/badge/License-MIT-red)

---

## 🎮 Features

- **🕹️ Classic Gameplay**: Tap to keep the bird aloft
- **📈 Score Tracking**: Real-time score and high score
- **🎯 Collision Detection**: Precise hitboxes for pipes and boundaries
- **🔄 Restart Mechanic**: Instant replay with spacebar
- **🎨 Minimalist Design**: Clean graphics and smooth animations

---

## 🖼️ Screenshots

![Gameplay](screenshot.png) *(Add your own screenshot here!)*

---

## 🛠️ Installation

**Clone and run with one command:**
Click the copy button in the top-right corner →
git clone https://github.com/yourusername/flappy-bird-clone.git && cd flappy-bird-clone

Install dependencies
pip install pygame

text

---

## 🚀 Running the Game

python flappy_bird.py

text

---

## 🕹️ How to Play

1. **Press SPACE** to start the game
2. **Tap SPACE** to make the bird flap
3. **Navigate** through pipe gaps
4. **Crash** = Game Over (Press SPACE to restart)
5. **Compete** against your high score!

---

## 🧠 Code Highlights

Core Game Loop
while True:
handle_events()
update_game_state()
render_graphics()
clock.tick(60) # 60 FPS

text

- **📦 Object-Oriented Design** (easily extendable)
- **⚡ Efficient Collision Detection** using `pygame.Rect`
- **⏲️ Pipe Generation System** with random heights
- **📊 Score Calculation** (0.5 points per pipe passed)

---

## 🛠️ Customization

- **🖌️ Change Colors** in the constants section
- **📐 Adjust Difficulty**:
pipe_gap = 150 # Decrease for harder difficulty
scroll_speed = 3 # Increase for faster gameplay
gravity = 0.5 # Increase for heavier feeling

text
- **🎵 Add Sound Effects** using `pygame.mixer`

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

---

**Happy Flapping!** 🚀