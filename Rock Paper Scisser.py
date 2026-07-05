import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("=" * 40)
print("      ROCK PAPER SCISSORS")
print("=" * 40)

while True:
    user = input("\nChoose Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("🤝 It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1

    else:
        print("💻 Computer Wins!")
        computer_score += 1

    print("\nScore")
    print("-------------------")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    play = input("\nPlay Again? (y/n): ").lower()

    if play != "y":
        break

print("\nFinal Score")
print("-------------------")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("🏆 Congratulations! You won the game.")
elif computer_score > user_score:
    print("😢 Computer won the game.")
else:
    print("🤝 The game ended in a tie.")

print("\nThanks for playing!")