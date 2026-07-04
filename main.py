from brain import ask


def main():
    print("===================================")
    print("        BEN AI Assistant")
    print("Type 'exit' to quit.")
    print("===================================")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        response = ask(user_input)

        print(f"\nBen: {response}")


if __name__ == "__main__":
    main()