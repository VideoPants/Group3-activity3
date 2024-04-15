"""_summary_
    Group Members: Syed Ali Mustafa Wasti, Youssef Marak
    
    Contributions: Syed Ali Mustafa Wasti - 65%, Youssef Marak - 35%
    
    Date: 05/02/2024
    Manifesto: This program is designed to sort data and show the sorted data in a kind of pattern.
"""

import csv

def stage_1():
    """
    Stage 1: Load Data
    Loads a CSV file and prints its contents.
    Args:
        None
    Returns:
        data: A 2D list containing the rows and columns of the CSV file.
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    file_path = input("Please enter path to the CSV file: ")

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            data = []

            for row in csv_reader:
                data.append(row)
                print(row)

            print("File exists.")
            print("Loading file...")
            print("File successfully loaded!")
            print("Loaded Table:")

            for row in data:
                print(row)

            return data

    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
        return stage_1()


def stage_2(data):
    """
    Stage 2: Clean and prepare data
    Cleans and prepares a specific column of data.
    Args:
        data: A 2D list containing the rows and columns of the CSV file.
    Returns:
        cleaned_data: A list containing the cleaned values of the specified column.
    Raises:
        ValueError: If the specified column is not numerical.
    """
    print("Stage 2: Clean and prepare data")

    columns = data[0]

    print("Choose column from selection below to clean and prepare data:")
    for i in range(len(columns)):
        print(f"{i + 1}. {columns[i]}")

    column_index = None

    while column_index is None:
        try:
            choice = int(input("Please choose column: ")) - 1

            if not columns[choice].replace(" ", "").replace("/", "").isalpha():
                print("Non-numerical column, please try again.")

            else:
                column_index = choice

        except (ValueError, IndexError):
            print("Wrong input, please try again.")
            column_index = None

    column_name = columns[column_index]
    column_data = []

    for row in range(len(data[1:])):
        if column_index >= len(data[row]):
            print("Column index out of range in row:", row)

        else:
            column_data.append(data[row][column_index])

    print("Would you like to replace empty cells from the column with:")
    print("1. Maximum value from column")
    print("2. Minimum value from column")
    print("3. Average value from column")

    choice = None

    while choice is None:
        try:
            choice = int(input("Enter your choice: "))

            if choice not in [1, 2, 3]:
                raise ValueError

        except ValueError:
            print("Invalid choice. Please try again.")
            choice = None

    if choice == 1:
        replacement_value = max([int(value) for value in column_data if value.isdigit()])

    elif choice == 2:
        replacement_value = min([int(value) for value in column_data if value.isdigit()])

    elif choice == 3:
        non_empty_values = [int(value) for value in column_data if value.isdigit()]
        replacement_value = sum(non_empty_values) / len(non_empty_values) if non_empty_values else 0

    cleaned_data = [replacement_value if value == '' else value for value in column_data]

    print("All empty values replaced with average values!")
    print("Updated Column:")
    print(cleaned_data)

    return cleaned_data


def insertion_sort(arr):
    """
    Insertion sort algorithm.
    Args:
        arr: A list of numbers to be sorted.
    Returns:
        sorted_arr: A sorted list of numbers.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def stage_3(cleaned_data):
    """
    Stage 3: Analyze Data
    Analyzes the cleaned data and sorts it.
    Args:
        cleaned_data: A list containing the cleaned values of the specified column.
    Returns:
        sorted_data: A sorted list of cleaned data.
    """
    print("Stage 3: Analyze Data")
    print("Please choose if you want to sort column in:")
    print("1. Ascending order")
    print("2. Descending order")

    try:
        choice = int(input("Please enter your choice: "))

        if choice not in [1, 2]:
            raise ValueError

    except ValueError:
        print("Invalid choice. Please try again.")
        choice = None

    if choice == 1:
        order = 'ascending'

    elif choice == 2:
        order = 'descending'

    print("Column values are sorted in", order, "order!")
    sorted_data = insertion_sort(cleaned_data)
    print("Sorted Column:")
    print(sorted_data)

    return sorted_data


def stage_4(sorted_data):
    """
    Stage 4: Visualize Data
    Visualizes the sorted data by representing each unit sold with a star.
    Args:
        sorted_data: A sorted list of cleaned data.
    """
    print("Stage 4: Visualize Data")
    print("Column: Units sold")
    print("Legend: each '*' represents 5 units")

    for value in sorted_data:
        if value.isdigit():
            stars = '*' * (int(value) // 5)
            print(stars[:20])

    print("Visualisation completed!")
    print("Thank you and goodbye!")


def main():
    """
    Main function that runs the entire program.
    """
    print("---------------------------------")
    print("Welcome to Data Analysis CLI")
    print("---------------------------------")
    print("Program stages:")
    print("1. Load Data")
    print("2. Clean and prepare data")
    print("3. Analyze Data")
    print("4. Visualize Data")

    data = stage_1()
    cleaned_data = stage_2(data)
    sorted_data = stage_3(cleaned_data)
    stage_4(sorted_data)


if __name__ == "__main__":
    main()