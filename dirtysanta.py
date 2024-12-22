import random

def display_ascii_art():
    ascii_art = r"""
    ______  _____  _____  _____ _____  ______ ___________ _______   __  _____  ___   _   _ _____ _____ ___  
    |  _  \/  __ \/ __  \|  _  |  ___| |  _  \_   _| ___ \_   _\ \ / / /  ___|/ _ \ | \ | |_   _|_   _/ _ \ 
    | | | || /  \/`' / /'| |/' |___ \  | | | | | | | |_/ / | |  \ V /  \ `--./ /_\ \|  \| | | |   | |/ /_\ \
    | | | || |      / /  |  /| |   \ \ | | | | | | |    /  | |   \ /    `--. \  _  || . ` | | |   | ||  _  |
    | |/ / | \__/\./ /___\ |_/ /\__/ / | |/ / _| |_| |\ \  | |   | |   /\__/ / | | || |\  | | |   | || | | |
    |___/   \____/\_____/ \___/\____/  |___/  \___/\_| \_| \_/   \_/   \____/\_| |_/\_| \_/ \_/   \_/\_| |_/
    """
    print(ascii_art)

display_ascii_art()

def get_names():
    """Prompt the user to input names."""
    print("Enter participant names (type 'done' when finished):")
    names = []
    while True:
        name = input("Name: ").strip()
        if name.lower() == 'done':
            break
        if name:
            names.append(name)
    return names

def assign_numbers(names):
    """Randomly assign numbers to names."""
    numbers = list(range(1, len(names) + 1))
    random.shuffle(numbers)
    return dict(zip(names, numbers))

def play_game(participants):
    """Play the Dirty Santa game."""
    print("Let the game begin!")
    sorted_participants = sorted(participants.items(), key=lambda x: x[1])

    turns = []
    for turn, (name, number) in enumerate(sorted_participants, start=1):
        print(f"Turn {turn}: It's {name}'s turn (Number: {number})")
        turns.append(name)
        input("Press Enter to proceed to the next turn...")

    # Final steal for participant with number 1
    first_player = sorted_participants[0][0]
    print(f"Special Rule: {first_player} (who started first) gets one last chance to steal if they choose!")
    final_choice = input("{first_player}, would you like to steal? (yes/no): ").strip().lower()
    if final_choice == 'yes':
        print(f"{first_player} gets to steal as the final move!")
    else:
        print(f"{first_player} chose not to steal. The game ends here!")

def main():
    names = get_names()

    if len(names) < 2:
        print("You need at least 2 participants to play Dirty Santa.")
        return

    participants = assign_numbers(names)
    print("Participants and their numbers:")
    for name, number in participants.items():
        print(f"{name}: {number}")

    play_game(participants)
    names = get_names()

    if len(names) < 2:
        print("You need at least 2 participants to play Dirty Santa.")
        return

    participants = assign_numbers(names)
    print("\nParticipants and their numbers:")
    for name, number in participants.items():
        print(f"{name}: {number}")

    play_game(participants)

if __name__ == "__main__":
    main()
