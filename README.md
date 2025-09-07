# 🐍💧🔫 Snake Water Gun Game

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Game](https://img.shields.io/badge/Game-Classic-orange)]()

> A modern Python implementation of the classic Snake Water Gun hand game with enhanced features, beautiful UI, and comprehensive statistics tracking.

## 🎮 About the Game

Snake Water Gun is a classic hand game similar to Rock Paper Scissors, but with a unique twist! This Python implementation brings the traditional game to your terminal with enhanced features and a beautiful user interface.

### Game Rules
- 🐍 **Snake drinks Water** → Snake wins
- 💧 **Water drowns Gun** → Water wins  
- 🔫 **Gun shoots Snake** → Gun wins
- Same choices result in a draw

## ✨ Features

### 🎯 Core Gameplay
- **Single Player Mode**: Play against intelligent computer opponent
- **Interactive UI**: Beautiful terminal interface with emojis and colors
- **Input Validation**: Robust error handling for user inputs
- **Quit Anytime**: Graceful exit option during gameplay

### 📊 Advanced Features  
- **Score Tracking**: Real-time score updates throughout the game
- **Game Statistics**: Detailed win rate and performance metrics
- **Game History**: Complete log of all rounds played
- **Play Again Option**: Continue playing multiple rounds seamlessly
- **Professional Code Structure**: Object-oriented design with clean architecture

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses only built-in modules)

### Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/snake-water-gun-game.git
   cd snake-water-gun-game
   ```

2. **Run the game**
   ```bash
   python snake_water_gun.py
   ```

3. **Start playing!**
   - Choose your weapon: Snake (S), Water (W), or Gun (G)
   - Watch the computer make its choice
   - See the results and track your progress
   - Play as many rounds as you want!

## 🎲 How to Play

1. **Launch the game** - Run the Python script
2. **Choose your weapon** - Enter S for Snake, W for Water, or G for Gun
3. **View results** - See both choices and who won the round
4. **Track progress** - Monitor your score and statistics
5. **Continue or quit** - Play another round or exit with final stats

## 📸 Game Preview

```
============================================================
🎮 SNAKE WATER GUN GAME 🎮
============================================================
Rules:
🐍 Snake drinks Water (Snake wins)
💧 Water drowns Gun (Water wins)
🔫 Gun shoots Snake (Gun wins)
============================================================

Choose your weapon:
🐍 [S] Snake
💧 [W] Water
🔫 [G] Gun
❌ [Q] Quit Game

Enter your choice (S/W/G/Q): s

🎯 You chose: 🐍 Snake
🤖 Computer chose: 💧 Water

🎉 You Win this round!

📊 SCORE: You 1 - 0 Computer
🎮 Rounds played: 1
```

## 🛠️ Technical Implementation

### Code Structure
- **Object-Oriented Design**: Clean `SnakeWaterGun` class with organized methods
- **Error Handling**: Comprehensive exception handling and input validation
- **Modular Functions**: Separated concerns with dedicated methods for each feature
- **Documentation**: Complete docstrings and inline comments

### Key Components
- `SnakeWaterGun` class: Main game controller
- `get_player_choice()`: Handles user input with validation
- `determine_winner()`: Implements game logic and rules
- `display_stats()`: Shows comprehensive game statistics
- `run_game()`: Main game loop with flow control

## 🔧 Customization

Want to modify the game? Here are some ideas:

- **Add new weapons**: Extend the `choices` dictionary
- **Change UI elements**: Modify emojis and formatting
- **Add difficulty levels**: Implement different AI strategies
- **Save game history**: Add file I/O to persist game data
- **Tournament mode**: Create multi-round tournaments

## 📈 Development Insights

This project demonstrates:
- **Python Fundamentals**: Variables, functions, control structures
- **Object-Oriented Programming**: Classes, methods, encapsulation
- **User Interface Design**: Terminal-based UI with enhanced UX
- **Error Handling**: Robust input validation and exception management
- **Code Organization**: Clean, maintainable, and scalable structure

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Ideas for Contributions
- GUI version using Tkinter or Pygame
- Multiplayer mode
- AI with learning capabilities
- Sound effects and animations
- Mobile app version

## 📝 Project Roadmap

### Version 1.0 ✅
- [x] Basic game functionality
- [x] Score tracking
- [x] Enhanced UI with emojis
- [x] Input validation
- [x] Game statistics

### Version 2.0 (Planned)
- [ ] GUI version
- [ ] Sound effects
- [ ] AI difficulty levels
- [ ] Tournament mode
- [ ] Game replay feature

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Bhavish**  
- GitHub: [@bhavishbytes](https://github.com/bhavishbytes)
- Email: bhavish@example.com

## 🙏 Acknowledgments

- Inspired by the classic Rock Paper Scissors game
- Built as part of learning Python programming
- Thanks to the Python community for excellent documentation
- Special thanks to all contributors and testers

## 📊 Repository Stats

![GitHub stars](https://img.shields.io/github/stars/bhavishbytes/snake-water-gun-game)
![GitHub forks](https://img.shields.io/github/forks/bhavishbytes/snake-water-gun-game)
![GitHub issues](https://img.shields.io/github/issues/bhavishbytes/snake-water-gun-game)
![GitHub last commit](https://img.shields.io/github/last-commit/bhavishbytes/snake-water-gun-game)

---

⭐ **If you enjoyed this game, please give it a star!** ⭐

*Happy Gaming! 🎮*
