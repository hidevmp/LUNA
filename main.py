from config.personality import LUNA_PERSONALITY


def main():
    print(f"{LUNA_PERSONALITY['name']} is online.")
    print(f"Creator: {LUNA_PERSONALITY['creator']}")
    print(f"Personality: {LUNA_PERSONALITY['style']}")
    print(f"Tone: {LUNA_PERSONALITY['tone']}")
    print()
    print(LUNA_PERSONALITY["description"])


if __name__ == "__main__":
    main()