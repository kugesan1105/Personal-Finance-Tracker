"""
Data Service

Provides functions for loading and creating sample data.
In a real application, this would connect to a database or external API.
"""

from datetime import datetime, timedelta
from typing import List
import random

from models.user import User
from models.transaction import Transaction, TransactionType


def load_users() -> List[User]:
    """
    Loads a list of sample users.
    
    In a real application, this would fetch users from a database.
    
    Returns:
        List[User]: A list of sample User objects
    """
    sample_users = [
        User(1, "john_doe", "john@example.com", "John", "Doe"),
        User(2, "jane_smith", "jane@example.com", "Jane", "Smith"),
        User(3, "bob_wilson", "bob@example.com", "Bob", "Wilson"),
        User(4, "alice_brown", "alice@example.com", "Alice", "Brown"),
        User(5, "charlie_davis", "charlie@example.com", "Charlie", "Davis")
    ]
    
    # Set different creation dates for variety
    base_date = datetime.now() - timedelta(days=30)
    for i, user in enumerate(sample_users):
        user.created_at = base_date + timedelta(days=i * 7)
    
    return sample_users


def load_transactions() -> List[Transaction]:
    """
    Loads a list of sample transactions.
    
    In a real application, this would fetch transactions from a database.
    
    Returns:
        List[Transaction]: A list of sample Transaction objects
    """
    transaction_types = [TransactionType.DEPOSIT, TransactionType.WITHDRAWAL, 
                        TransactionType.TRANSFER, TransactionType.PAYMENT]
    
    sample_transactions = []
    
    # Create 15 sample transactions
    for i in range(1, 16):
        user_id = random.randint(1, 5)
        amount = round(random.uniform(10.0, 1000.0), 2)
        transaction_type = random.choice(transaction_types)
        
        transaction = Transaction(
            transaction_id=i,
            user_id=user_id,
            amount=amount,
            transaction_type=transaction_type,
            description=f"Sample {transaction_type.value} transaction #{i}"
        )
        
        # Set some transactions as completed
        if i % 3 == 0:
            transaction.complete_transaction()
        
        # Set creation date in the past
        transaction.created_at = datetime.now() - timedelta(days=random.randint(1, 30))
        
        sample_transactions.append(transaction)
    
    return sample_transactions


def create_sample_user(user_id: int, username: str, email: str, 
                      first_name: str, last_name: str) -> User:
    """
    Creates a new sample user with the provided information.
    
    Args:
        user_id (int): Unique identifier for the user
        username (str): Username for the user
        email (str): User's email address
        first_name (str): User's first name
        last_name (str): User's last name
    
    Returns:
        User: A new User object with the provided information
    """
    return User(user_id, username, email, first_name, last_name)


def create_sample_transaction(transaction_id: int, user_id: int, amount: float,
                            transaction_type: TransactionType, description: str = "") -> Transaction:
    """
    Creates a new sample transaction with the provided information.
    
    Args:
        transaction_id (int): Unique identifier for the transaction
        user_id (int): ID of the user who initiated the transaction
        amount (float): Transaction amount
        transaction_type (TransactionType): Type of the transaction
        description (str): Optional description of the transaction
    
    Returns:
        Transaction: A new Transaction object with the provided information
    """
    return Transaction(transaction_id, user_id, amount, transaction_type, description)


def get_user_by_id(user_id: int) -> User:
    """
    Retrieves a user by their ID.
    
    Args:
        user_id (int): The ID of the user to retrieve
    
    Returns:
        User: The user with the specified ID, or None if not found
    """
    users = load_users()
    for user in users:
        if user.user_id == user_id:
            return user
    return None


def get_transactions_by_user(user_id: int) -> List[Transaction]:
    """
    Retrieves all transactions for a specific user.
    
    Args:
        user_id (int): The ID of the user whose transactions to retrieve
    
    Returns:
        List[Transaction]: A list of transactions for the specified user
    """
    all_transactions = load_transactions()
    return [transaction for transaction in all_transactions if transaction.user_id == user_id]