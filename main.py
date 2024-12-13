import sys

from src.digits_to_letters import digits_to_text_fr


def main():
    """
    a quick wrapper to call the digit to text function
    Could be better to do it with click, invoke or any other tool
    But not the core of this test
    """
    number = int(sys.argv[1])
    print(number, digits_to_text_fr(number))


if __name__ == "__main__":
    main()
