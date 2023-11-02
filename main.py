class Question:
    def __init__(self, text, options=None):
        self.text = text
        self.options = options
        self.answer = None

    def ask(self):
        print(self.text)
        if self.options:
            for i, option in enumerate(self.options, start=1):
                print(f"{i}. {option}")
            while True:
                try:
                    choice = int(input("Enter your choice (1, 2, 3, ...): "))
                    if 1 <= choice <= len(self.options):
                        self.answer = self.options[choice - 1]
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            self.answer = input()

def main():
    print("Welcome to the Lawnmower Quiz!")
    print("Answer the following questions to find the perfect mower for you.")

    questions = [
        Question("How much land are you cutting? (e.g., 1/4 acre, 1 acre, 2 acres, etc.): "),
        Question("What is your budget for a lawnmower? (e.g., $3000, $4000, etc.): "),
        Question("What is your preferred style of mower?", ["Zero Turn", "Lawn Tractor", "Stander", "Walk Behind"]),
    ]

    user_answers = []

    for question in questions:
        question.ask()
        user_answers.append(question.answer)

    # Retrieve the answers to the questions
    land_size_answer = float(user_answers[0].split()[0])  # Extract the numeric value from the land size answer
    budget_answer = float(user_answers[1].replace('$', '').replace(',', ''))  # Extract the numeric value from the budget answer
    mower_preference_answer = user_answers[2]

    # Define the end results based on user's answers
    results = [
        {
            "land_size_range": (0, 2),  # Land size range from 0 to 2 acres
            "price": 3699.00,  # Price for Husqvarna Z200F Series
            "mower_style": "Zero Turn",  # Preferred mower style
            "recommendation": "Husqvarna Z200F Series is a great choice for your lawn."
        },
        {
            "land_size_range": (0, 2),  # Land size range from 0 to 2 acres
            "price": 6229.00,  # Price for Spartan RZ-C
            "mower_style": "Zero Turn",  # Preferred mower style
            "recommendation": "Spartan RZ-C is a high-performance zero-turn mower suitable for your lawn."
        },
        {
            "land_size_range": (0, 6),  # Land size range from 0 to 6 acres
            "price": 7739.00,  # Price for Spartan RZ-Pro
            "mower_style": "Zero Turn",  # Preferred mower style
            "recommendation": "Spartan RZ-Pro is a professional-grade zero-turn mower for your lawn."
        },
        {
            "land_size_range": (0, 4),  # Land size range from 0 to 4 acres
            "price": 6929.00,  # Price for Spartan RZ
            "mower_style": "Zero Turn",  # Preferred mower style
            "recommendation": "Spartan RZ is a versatile zero-turn mower for your lawn."
        },
        {
            "land_size_range": (0, 8),  # Land size range from 0 to 8 acres (updated)
            "price": 9419.00,  # Price for Spartan RZ-HD (updated)
            "mower_style": "Zero Turn",  # Preferred mower style
            "recommendation": "Spartan RZ-HD is an entry-level commercial Zero Turn."
        },
        {
            "land_size_range": (0, 1),  # Land size range from 0 to 1 acre (updated)
            "price": 2499.00,  # Price for Husqvarna YTH21546 (updated)
            "mower_style": "Lawn Tractor",  # Preferred mower style
            "recommendation": "Husqvarna YTH21546 is a good mower for your lawn."
        },
        {
            "land_size_range": (0, 3),  # Land size range from 0 to 3 acres
            "price": 3099.00,  # Price for Husqvarna TS148K Series
            "mower_style": "Lawn Tractor",  # Preferred mower style
            "recommendation": "Husqvarna TS148K is a great choice for your lawn."
        },
        {
            "land_size_range": (0, 3.5),  # Land size range from 0 to 4 acres
            "price": 2599.00,  # Price for Husqvarna TS148L
            "mower_style": "Lawn Tractor",  # Preferred mower style
            "recommendation": "Husqvarna TS148L is a great choice for your lawn."
        },
    ]

    # Find all matching mowers based on user's selections
    matching_mowers = []
    for result in results:
        if (
            result["land_size_range"][0] <= land_size_answer <= result["land_size_range"][1]
            and result["price"] <= budget_answer  # Check if the mower price is within budget
            and result["mower_style"] == mower_preference_answer
        ):
            matching_mowers.append(result["recommendation"])

    if matching_mowers:
        print("\nBased on your answers, the following mowers match your selections:")
        for i, mower in enumerate(matching_mowers, start=1):
            print(f"{i}. {mower}")
    else:
        print("\nSorry, we couldn't find any matching mowers based on your selections.")

if __name__ == "__main__":
    main()
