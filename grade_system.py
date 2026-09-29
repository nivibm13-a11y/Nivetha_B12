
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


def get_mark():
    while True:
        try:
            score = int(input("Enter your mark (0-100): "))

            if score < 0 or score > 100:
                print("Invalid mark. Please enter a number between 0 and 100.")
            else:
                return score

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    score = get_mark()
    grade = calculate_grade(score)

    print(f"Mark: {score}")
    print(f"Grade: {grade}")


main()
