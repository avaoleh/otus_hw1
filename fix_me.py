"""Otus HW1"""


def calculate_average(numbers):
    """Summary or Description of the Function

    Parameters:
    total (float): sum numbers
    count(int): count numbers

    Returns:
    average: Returning value
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
