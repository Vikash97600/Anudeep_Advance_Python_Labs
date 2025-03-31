def calculate_expenses(expenses):
    """
    Calculate total expenses.

    Args:
        expenses (list): A list of expense amounts.

    Returns:
        float: The total expenses.
    """
    return sum(expenses)

def calculate_income(incomes):
    """
    Calculate total income.

    Args:
        incomes (list): A list of income amounts.

    Returns:
        float: The total income.
    """
    return sum(incomes)

def calculate_savings(income, expenses):
    """
    Calculate savings based on income and expenses.

    Args:
        income (float): Total income.
        expenses (float): Total expenses.

    Returns:
        float: The total savings (income - expenses).
    """
    return income - expenses