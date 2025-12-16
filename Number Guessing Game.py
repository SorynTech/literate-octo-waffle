import random
# Get number of players
num_players = int(input("How many players? "))

# Collect all player names
players = []
for i in range(num_players):
    name = input(f"Enter name for Player {i + 1}: ")
    players.append(name)

# Generate the target number (same for all players)
target = random.randint(1, 200)

# Store attempts for each player
attempts = {player: 0 for player in players}
game_over = False
winner = None

# Open file in append mode
with open("game_scores.txt", "a") as file:
    file.write(f"\n{'=' * 40}\n")
    file.write(f"NEW MULTIPLAYER GAME - {num_players} Players\n")
    file.write(f"Target number: {target}\n")
    file.write(f"Players: {', '.join(players)}\n")
    file.write(f"{'=' * 40}\n")

    # Players take turns until someone wins
    current_player_index = 0

    while not game_over:
        player = players[current_player_index]

        print(f"\n--- {player}'s Turn ---")
        guess = int(input(f"{player}, guess a number between 1 and 200: "))
        attempts[player] += 1

        # Write each guess to file
        file.write(f"{player} - Attempt {attempts[player]}: {guess}\n")

        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"\n🎉 Correct! {player} wins with {attempts[player]} attempts!")
            winner = player
            game_over = True
            file.write(f"\n{'=' * 40}\n")
            file.write(f"🎉 WINNER: {player}\n")
            file.write(f"Winning Score: {attempts[player]} attempts\n")
            file.write(f"{'=' * 40}\n")

        # Move to next player
        current_player_index = (current_player_index + 1) % num_players

    # Write all player stats
    file.write("\nFinal Statistics:\n")
    for player in players:
        status = "WINNER" if player == winner else "Played"
        file.write(f"  {player}: {attempts[player]} attempts - {status}\n")

    file.write("=" * 40 + "\n")

print("\nGame saved to game_scores.txt!")
#aasas