"""
Snake Water Gun Game
A fun Python implementation of the classic hand game

"""

import random
import os
import sys

class SnakeWaterGun:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.game_history = []

        # Game choices mapping
        self.choices = {
            's': {'name': 'Snake', 'emoji': '🐍', 'value': 1},
            'w': {'name': 'Water', 'emoji': '💧', 'value': -1},
            'g': {'name': 'Gun', 'emoji': '🔫', 'value': 0}
        }

        # Reverse mapping for computer choice display
        self.reverse_choices = {
            1: 's', -1: 'w', 0: 'g'
        }

    def display_banner(self):
        """Display game banner"""
        print("=" * 60)
        print("🎮 SNAKE WATER GUN GAME 🎮")
        print("=" * 60)
        print("Rules:")
        print("🐍 Snake drinks Water (Snake wins)")
        print("💧 Water drowns Gun (Water wins)")
        print("🔫 Gun shoots Snake (Gun wins)")
        print("=" * 60)

    def get_player_choice(self):
        """Get valid player choice with error handling"""
        while True:
            print("\nChoose your weapon:")
            print("🐍 [S] Snake")
            print("💧 [W] Water") 
            print("🔫 [G] Gun")
            print("❌ [Q] Quit Game")

            choice = input("\nEnter your choice (S/W/G/Q): ").lower().strip()

            if choice == 'q':
                return None
            elif choice in self.choices:
                return choice
            else:
                print("❌ Invalid choice! Please enter S, W, G, or Q")

    def get_computer_choice(self):
        """Generate computer choice"""
        return random.choice(list(self.choices.keys()))

    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of the round"""
        player_value = self.choices[player_choice]['value']
        computer_value = self.choices[computer_choice]['value']

        if player_value == computer_value:
            return "draw"
        elif (player_value == 1 and computer_value == -1) or \
             (player_value == -1 and computer_value == 0) or \
             (player_value == 0 and computer_value == 1):
            return "player"
        else:
            return "computer"

    def display_choices(self, player_choice, computer_choice):
        """Display both choices"""
        player_info = self.choices[player_choice]
        computer_info = self.choices[computer_choice]

        print(f"\n🎯 You chose: {player_info['emoji']} {player_info['name']}")
        print(f"🤖 Computer chose: {computer_info['emoji']} {computer_info['name']}")

    def display_result(self, result):
        """Display round result"""
        if result == "draw":
            print("🤝 It's a Draw!")
        elif result == "player":
            print("🎉 You Win this round!")
            self.player_score += 1
        else:
            print("😢 Computer wins this round!")
            self.computer_score += 1

    def display_score(self):
        """Display current score"""
        print(f"\n📊 SCORE: You {self.player_score} - {self.computer_score} Computer")
        print(f"🎮 Rounds played: {self.rounds_played}")

    def play_round(self):
        """Play a single round"""
        player_choice = self.get_player_choice()

        if player_choice is None:  # Player chose to quit
            return False

        computer_choice = self.get_computer_choice()

        self.display_choices(player_choice, computer_choice)

        result = self.determine_winner(player_choice, computer_choice)
        self.display_result(result)

        # Store game history
        self.game_history.append({
            'round': self.rounds_played + 1,
            'player': player_choice,
            'computer': computer_choice,
            'result': result
        })

        self.rounds_played += 1
        self.display_score()

        return True

    def display_final_stats(self):
        """Display final game statistics"""
        print("\n" + "=" * 60)
        print("🏁 GAME OVER - FINAL STATISTICS")
        print("=" * 60)

        if self.player_score > self.computer_score:
            print("🏆 CONGRATULATIONS! YOU ARE THE CHAMPION!")
        elif self.computer_score > self.player_score:
            print("🤖 Computer wins! Better luck next time!")
        else:
            print("🤝 It's a tie! Great game!")

        print(f"\n📊 Final Score: You {self.player_score} - {self.computer_score} Computer")
        print(f"🎮 Total rounds played: {self.rounds_played}")

        if self.rounds_played > 0:
            win_rate = (self.player_score / self.rounds_played) * 100
            print(f"📈 Your win rate: {win_rate:.1f}%")

    def play_again(self):
        """Ask if player wants to play again"""
        while True:
            choice = input("\n🔄 Play another round? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no")

    def run_game(self):
        """Main game loop"""
        self.display_banner()

        print("\n🚀 Welcome! Let's start playing!")

        # Game loop
        while True:
            if not self.play_round():  # Player chose to quit
                break

            if not self.play_again():  # Player doesn't want to continue
                break

        self.display_final_stats()
        print("\n👋 Thanks for playing! Come back soon!")

# Main execution
if __name__ == "__main__":
    try:
        game = SnakeWaterGun()
        game.run_game()
    except KeyboardInterrupt:
        print("\n\n🛑 Game interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the game.")
