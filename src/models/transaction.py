"""
Transaction Model

Defines the Transaction class representing a financial transaction in the system.
Contains transaction details and methods for transaction operations.
"""

from datetime import datetime
from enum import Enum
from typing import Optional


class TransactionType(Enum):
    """Enumeration of possible transaction types."""
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"
    PAYMENT = "payment"


class TransactionStatus(Enum):
    """Enumeration of possible transaction statuses."""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Transaction:
    """
    Represents a financial transaction in the system.
    
    This class encapsulates transaction data and provides methods for
    transaction-related operations such as validation and status management.
    """
    
    def __init__(self, transaction_id: int, user_id: int, amount: float,
                 transaction_type: TransactionType, description: str = "",
                 created_at: Optional[datetime] = None):
        """
        Initialize a new Transaction instance.
        
        Args:
            transaction_id (int): Unique identifier for the transaction
            user_id (int): ID of the user who initiated the transaction
            amount (float): Transaction amount
            transaction_type (TransactionType): Type of the transaction
            description (str): Optional description of the transaction
            created_at (Optional[datetime]): When the transaction was created (defaults to now)
        """
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.created_at = created_at or datetime.now()
        self.status = TransactionStatus.PENDING
    
    def is_valid_amount(self) -> bool:
        """
        Validates that the transaction amount is positive.
        
        Returns:
            bool: True if the amount is valid (positive), False otherwise
        """
        return self.amount > 0
    
    def complete_transaction(self) -> None:
        """
        Marks the transaction as completed.
        """
        if self.status == TransactionStatus.PENDING:
            self.status = TransactionStatus.COMPLETED
    
    def fail_transaction(self, reason: str = "") -> None:
        """
        Marks the transaction as failed.
        
        Args:
            reason (str): Optional reason for the failure
        """
        self.status = TransactionStatus.FAILED
        if reason:
            self.description += f" [Failed: {reason}]"
    
    def cancel_transaction(self) -> bool:
        """
        Cancels the transaction if it's still pending.
        
        Returns:
            bool: True if the transaction was cancelled, False if it couldn't be cancelled
        """
        if self.status == TransactionStatus.PENDING:
            self.status = TransactionStatus.CANCELLED
            return True
        return False
    
    def get_formatted_amount(self) -> str:
        """
        Returns the transaction amount formatted as currency.
        
        Returns:
            str: The amount formatted as a currency string
        """
        return f"${self.amount:.2f}"
    
    def is_completed(self) -> bool:
        """
        Checks if the transaction is completed.
        
        Returns:
            bool: True if the transaction is completed, False otherwise
        """
        return self.status == TransactionStatus.COMPLETED
    
    def __str__(self) -> str:
        """
        String representation of the transaction.
        
        Returns:
            str: A formatted string describing the transaction
        """
        return (f"Transaction({self.transaction_id}): {self.transaction_type.value.title()} "
                f"of {self.get_formatted_amount()} - {self.status.value.title()}")
    
    def __repr__(self) -> str:
        """
        Developer representation of the transaction.
        
        Returns:
            str: A detailed string representation for debugging
        """
        return (f"Transaction(transaction_id={self.transaction_id}, user_id={self.user_id}, "
                f"amount={self.amount}, type={self.transaction_type}, "
                f"status={self.status}, created_at={self.created_at})")