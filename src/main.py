"""
Personal Finance Tracker - Main Application Entry Point

This module serves as the main entry point for the Personal Finance Tracker application.
It orchestrates the loading of financial data, generation of reports, and demonstration
of key financial calculations.
"""

from services.data_service import load_users, load_transactions
from services.report_service import generate_user_report, generate_transaction_summary
from utils.file_ops import write_file
from utils.math_ops import add, multiply, calculate_average


def main():
    """
    Main application function that orchestrates the personal finance workflow.
    
    This function:
    1. Loads user accounts and transaction data
    2. Generates comprehensive financial reports
    3. Saves reports to output files
    4. Demonstrates financial calculations
    """
    print("🏦 Starting Personal Finance Tracker...")
    print("=" * 50)
    
    # Load financial data
    users = load_users()
    transactions = load_transactions()
    
    print(f"📊 Loaded {len(users)} users and {len(transactions)} transactions")
    
    # Generate comprehensive reports
    user_report = generate_user_report(users)
    transaction_summary = generate_transaction_summary(transactions)
    
    # Save reports to files for record keeping
    write_file("user_report.txt", user_report)
    write_file("transaction_summary.txt", transaction_summary)
    
    # Demonstrate financial calculations
    monthly_income = 5000.0
    monthly_expenses = 3200.0
    savings_rate = calculate_savings_rate(monthly_income, monthly_expenses)
    
    print(f"\n💰 Financial Summary:")
    print(f"   Monthly Income: ${monthly_income:.2f}")
    print(f"   Monthly Expenses: ${monthly_expenses:.2f}")
    print(f"   Savings Rate: {savings_rate:.1f}%")
    
    # Calculate compound interest example
    investment_result = calculate_compound_growth(1000, 0.07, 10)
    print(f"   Investment Growth: $1,000 → ${investment_result:.2f} (7% over 10 years)")
    
    print("\n✅ Personal Finance Tracker completed successfully!")
    print("📄 Reports saved to: user_report.txt, transaction_summary.txt")


def calculate_savings_rate(income: float, expenses: float) -> float:
    """
    Calculates the savings rate as a percentage of income.
    
    Args:
        income (float): Monthly income amount
        expenses (float): Monthly expenses amount
    
    Returns:
        float: Savings rate as a percentage
    """
    if income <= 0:
        return 0.0
    
    savings = income - expenses
    return (savings / income) * 100


def calculate_compound_growth(principal: float, rate: float, years: int) -> float:
    """
    Calculates compound interest growth over time.
    
    Args:
        principal (float): Initial investment amount
        rate (float): Annual interest rate (as decimal, e.g., 0.07 for 7%)
        years (int): Number of years
    
    Returns:
        float: Final amount after compound growth
    """
    return principal * ((1 + rate) ** years)


def analyze_spending_patterns():
    """
    Analyzes spending patterns from transaction data and provides insights.
    
    Returns:
        dict: Dictionary containing spending analysis results
    """
    transactions = load_transactions()
    
    # Filter completed transactions only
    completed_transactions = [t for t in transactions if t.is_completed()]
    
    if not completed_transactions:
        return {"error": "No completed transactions found"}
    
    # Calculate spending metrics
    amounts = [t.amount for t in completed_transactions]
    total_spending = sum(amounts)
    average_transaction = calculate_average(amounts)
    
    # Group by transaction type
    spending_by_type = {}
    for transaction in completed_transactions:
        trans_type = transaction.transaction_type.value
        spending_by_type[trans_type] = spending_by_type.get(trans_type, 0) + transaction.amount
    
    return {
        "total_spending": total_spending,
        "average_transaction": average_transaction,
        "transaction_count": len(completed_transactions),
        "spending_by_type": spending_by_type
    }


if __name__ == "__main__":
    main()