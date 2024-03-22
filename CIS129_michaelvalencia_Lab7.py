# Constants
SECTION_A_SEATS = 300
SECTION_B_SEATS = 500
SECTION_C_SEATS = 200

SECTION_A_PRICE = 20
SECTION_B_PRICE = 15
SECTION_C_PRICE = 10

# Function to calculate subtotal for a section
def calculate_subtotal(num_seats, price_per_seat):
    return num_seats * price_per_seat

# Function to validate input
def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Display welcome message
    print("Welcome to the Theater Seating Lab!")
    print("Section A: {} seats, ${} per seat".format(SECTION_A_SEATS, SECTION_A_PRICE))
    print("Section B: {} seats, ${} per seat".format(SECTION_B_SEATS, SECTION_B_PRICE))
    print("Section C: {} seats, ${} per seat".format(SECTION_C_SEATS, SECTION_C_PRICE))
    print()

    # Initialize variables
    total_income = 0
    section_a_sales = 0
    section_b_sales = 0
    section_c_sales = 0

    # Get input and calculate subtotal for section A
    num_seats_a = validate_input("Enter the number of tickets sold in Section A: ")
    subtotal_a = calculate_subtotal(num_seats_a, SECTION_A_PRICE)
    total_income += subtotal_a
    section_a_sales += num_seats_a
    print("Subtotal for Section A: ${}".format(subtotal_a))
    print("Total income so far: ${}".format(total_income))
    print()

    # Get input and calculate subtotal for section B
    num_seats_b = validate_input("Enter the number of tickets sold in Section B: ")
    subtotal_b = calculate_subtotal(num_seats_b, SECTION_B_PRICE)
    total_income += subtotal_b
    section_b_sales += num_seats_b
    print("Subtotal for Section B: ${}".format(subtotal_b))
    print("Total income so far: ${}".format(total_income))
    print()

    # Get input and calculate subtotal for section C
    num_seats_c = validate_input("Enter the number of tickets sold in Section C: ")
    subtotal_c = calculate_subtotal(num_seats_c, SECTION_C_PRICE)
    total_income += subtotal_c
    section_c_sales += num_seats_c
    print("Subtotal for Section C: ${}".format(subtotal_c))
    print("Total income so far: ${}".format(total_income))
    print()

    # Display overall total and section-wise sales
    print("Overall Total Income: ${}".format(total_income))
    print("Section A Sales: {} seats, ${}".format(section_a_sales, calculate_subtotal(section_a_sales, SECTION_A_PRICE)))
    print("Section B Sales: {} seats, ${}".format(section_b_sales, calculate_subtotal(section_b_sales, SECTION_B_PRICE)))
    print("Section C Sales: {} seats, ${}".format(section_c_sales, calculate_subtotal(section_c_sales, SECTION_C_PRICE)))

if __name__ == "__main__":
    main()
