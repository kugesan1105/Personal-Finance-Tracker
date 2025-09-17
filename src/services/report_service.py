"""
Report Service

Generates various types of reports using data from the data service
and utility functions for calculations and file operations.
"""

from typing import List
from datetime import datetime

from models.user import User
from models.transaction import Transaction, TransactionStatus
from utils.math_ops import calculate_average, add
from utils.file_ops import write_file


def generate_user_report(users: List[User]) -> str:
    """
    Generates a comprehensive report about users in the system.
    
    Args:
        users (List[User]): List of users to include in the report
    
    Returns:
        str: A formatted report containing user statistics and details
    """
    if not users:
        return "No users found in the system."
    
    # Calculate statistics
    total_users = len(users)
    active_users = len([user for user in users if user.is_active])
    inactive_users = total_users - active_users
    
    # Build the report
    report_lines = [
        "=" * 50,
        "USER REPORT",
        "=" * 50,
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "SUMMARY:",
        f"  Total Users: {total_users}",
        f"  Active Users: {active_users}",
        f"  Inactive Users: {inactive_users}",
        f"  Active Rate: {(active_users/total_users)*100:.1f}%",
        "",
        "USER DETAILS:",
        "-" * 30
    ]
    
    # Add individual user details
    for user in users:
        report_lines.extend([
            f"ID: {user.user_id} | {user.get_full_name()}",
            f"  Username: {user.username}",
            f"  Email: {user.email}",
            f"  Status: {'Active' if user.is_active else 'Inactive'}",
            f"  Created: {user.created_at.strftime('%Y-%m-%d')}",
            f"  Email Valid: {'Yes' if user.is_valid_email() else 'No'}",
            ""
        ])
    
    return "\n".join(report_lines)


def generate_transaction_summary(transactions: List[Transaction]) -> str:
    """
    Generates a summary report of transaction data with statistics.
    
    Args:
        transactions (List[Transaction]): List of transactions to analyze
    
    Returns:
        str: A formatted summary report of transaction statistics
    """
    if not transactions:
        return "No transactions found in the system."
    
    # Calculate statistics
    total_transactions = len(transactions)
    completed_transactions = [t for t in transactions if t.status == TransactionStatus.COMPLETED]
    pending_transactions = [t for t in transactions if t.status == TransactionStatus.PENDING]
    failed_transactions = [t for t in transactions if t.status == TransactionStatus.FAILED]
    
    # Calculate amounts
    total_amount = sum(t.amount for t in completed_transactions)
    if completed_transactions:
        average_amount = calculate_average([t.amount for t in completed_transactions])
    else:
        average_amount = 0.0
    
    # Group by transaction type
    transaction_types = {}
    for transaction in transactions:
        trans_type = transaction.transaction_type.value
        if trans_type not in transaction_types:
            transaction_types[trans_type] = 0
        transaction_types[trans_type] += 1
    
    # Build the report
    report_lines = [
        "=" * 50,
        "TRANSACTION SUMMARY REPORT",
        "=" * 50,
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "TRANSACTION STATISTICS:",
        f"  Total Transactions: {total_transactions}",
        f"  Completed: {len(completed_transactions)}",
        f"  Pending: {len(pending_transactions)}",
        f"  Failed: {len(failed_transactions)}",
        "",
        "FINANCIAL SUMMARY:",
        f"  Total Completed Amount: ${total_amount:.2f}",
        f"  Average Transaction: ${average_amount:.2f}",
        "",
        "BY TRANSACTION TYPE:",
        "-" * 25
    ]
    
    # Add transaction type breakdown
    for trans_type, count in transaction_types.items():
        percentage = (count / total_transactions) * 100
        report_lines.append(f"  {trans_type.title()}: {count} ({percentage:.1f}%)")
    
    report_lines.extend([
        "",
        "RECENT TRANSACTIONS:",
        "-" * 25
    ])
    
    # Add recent transactions (sorted by creation date)
    recent_transactions = sorted(transactions, key=lambda t: t.created_at, reverse=True)[:5]
    for transaction in recent_transactions:
        status_indicator = "✓" if transaction.is_completed() else "⏳" if transaction.status == TransactionStatus.PENDING else "✗"
        report_lines.append(
            f"  {status_indicator} {transaction.transaction_type.value.title()} - "
            f"${transaction.amount:.2f} (User {transaction.user_id}) - "
            f"{transaction.created_at.strftime('%Y-%m-%d')}"
        )
    
    return "\n".join(report_lines)


def save_user_report_to_file(users: List[User], filename: str = "user_report.txt") -> bool:
    """
    Generates a user report and saves it to a file.
    
    Args:
        users (List[User]): List of users to include in the report
        filename (str): Name of the file to save the report to
    
    Returns:
        bool: True if the report was saved successfully, False otherwise
    """
    report_content = generate_user_report(users)
    return write_file(filename, report_content)


def save_transaction_summary_to_file(transactions: List[Transaction], 
                                   filename: str = "transaction_summary.txt") -> bool:
    """
    Generates a transaction summary and saves it to a file.
    
    Args:
        transactions (List[Transaction]): List of transactions to analyze
        filename (str): Name of the file to save the summary to
    
    Returns:
        bool: True if the summary was saved successfully, False otherwise
    """
    summary_content = generate_transaction_summary(transactions)
    return write_file(filename, summary_content)