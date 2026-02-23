# Jin Han Jun

def show_instructions():
    """Display the game introduction and commands."""
    print("Star Kingdom Text Adventure")
    print("Collect 6 items to defeat Balthasar and save the Star Kingdom.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to inventory: get <item name>")
    print("-" * 40)


def show_status(current_room, inventory, rooms):
    """Display the player's current status."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("-" * 40)

def main():

    # Dictionary linking rooms and items
    rooms = {
        "Starlight Dining Room": {
            "North": "Stoney Cellar",
            "East": "Starbright Garden",
            "item": "Shield of Dawn"
        },
        "Starbright Garden": {
            "West": "Starlight Dining Room",
            "East": "Crystal Bridge",
            "item": "Guardian's Blade"
        },
        "Stoney Cellar": {
            "South": "Starlight Dining Room",
            "North": "Brush Peak",
            "item": "Challenger's Armor"
        },
        "Crystal Bridge": {
            "West": "Starbright Garden",
            "North": "Elderwood Library",
            "item": "King's Helmet"
        },
        "Brush Peak": {
            "South": "Stoney Cellar",
            "East": "Rainbow Den",
            "item": "Guardian's Hammer"
        },
        "Elderwood Library": {
            "South": "Crystal Bridge",
            "East": "Sky Summit",
            "item": "Hero's Potion"
        },
        "Rainbow Den": {
            "West": "Brush Peak",
            "North": "Sky Summit"
        },
        "Sky Summit": {
            "West": "Elderwood Library",
            "South": "Rainbow Den"
        }
    }

    villain_room = "Sky Summit"
    required_items = 6

    inventory = []
    current_room = "Starlight Dining Room"

    show_instructions()

    # Gameplay loop
    while True:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ")
        command_parts = command.split()

        if len(command_parts) >= 2 and command_parts[0].lower() == "go":
            direction = command_parts[1].title()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("Invalid direction. Try again.")

        elif len(command_parts) >= 2 and command_parts[0].lower() == "get":
            requested_item = " ".join(command_parts[1:])

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if requested_item.lower() == room_item.lower():
                    inventory.append(room_item)
                    del rooms[current_room]["item"]
                    print(f"{room_item} added to inventory.")
                else:
                    print("That item is not in this room.")
            else:
                print("No item in this room.")

        else:
            print("Invalid command. Use 'go <direction>' or 'get <item>'.")

        # Win/Lose Check
        if current_room == villain_room:
            if len(inventory) == required_items:
                print("\nYou encountered Balthasar!")
                print("You defeated Balthasar. The Star Kingdom is safe!")
                print("Congratulations! You win!")
            else:
                print("\nYou encountered Balthasar!")
                print("You did not collect all required items.")
                print("GAME OVER.")

            print("Thanks for playing the game.")
            break


if __name__ == "__main__":
    main()