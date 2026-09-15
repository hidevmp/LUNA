from config.personality import LUNA_PERSONALITY
from brain.chat import chat


def main():
    print(f"{LUNA_PERSONALITY['name']} is online.")
    print(f"Creator: {LUNA_PERSONALITY['creator']}")
    print()

    chat()


if __name__ == "__main__":
    main()