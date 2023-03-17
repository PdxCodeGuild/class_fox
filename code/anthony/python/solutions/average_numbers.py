

def get_total(list_of_numbers: list) -> int:
    total = 0
    # loop over the elements
    for num in list_of_numbers:
        total = total + num

    return total


def get_average(total: int, nums: list) -> int:
    average = total / len(nums)
    return average


def get_numbers_from_user():
    """
    This function will ask the user for numbers until the type 'done'
    """
    # Loop over and over asking the user for a number
    # while loop
    numbers = []
    while True:
        user_input = input("Enter a number, or 'done': ")
        # if user enters 'done' stop the loop: break
        if user_input == 'done':
            break
        # if user entered number add it to list
        elif user_input.isdigit():
            numbers.append(int(user_input))
        else:
            print("Invalid entry. Try again.")

    return numbers


nums = get_numbers_from_user()

total = get_total(nums)

average = get_average(total, nums)

print(average)
