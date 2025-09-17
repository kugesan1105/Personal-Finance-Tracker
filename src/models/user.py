"""
User Model

Defines the User class representing a user in the system.
Contains basic user information and methods for user operations.
"""

from datetime import datetime
from typing import Optional


class User:
    """
    Represents a user in the system.
    
    This class encapsulates user data and provides methods for
    user-related operations such as profile management and validation.
    """
    
    def __init__(self, user_id: int, username: str, email: str, 
                 first_name: str, last_name: str, created_at: Optional[datetime] = None):
        """
        Initialize a new User instance.
        
        Args:
            user_id (int): Unique identifier for the user
            username (str): Unique username for the user
            email (str): User's email address
            first_name (str): User's first name
            last_name (str): User's last name
            created_at (Optional[datetime]): When the user was created (defaults to now)
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at or datetime.now()
        self.is_active = True
    
    def get_full_name(self) -> str:
        """
        Returns the user's full name.
        
        Returns:
            str: The user's first and last name combined
        """
        return f"{self.first_name} {self.last_name}"
    
    def is_valid_email(self) -> bool:
        """
        Validates the user's email address format.
        
        Returns:
            bool: True if the email format is valid, False otherwise
        """
        return "@" in self.email and "." in self.email.split("@")[1]
    
    def deactivate(self) -> None:
        """
        Deactivates the user account.
        """
        self.is_active = False
    
    def activate(self) -> None:
        """
        Activates the user account.
        """
        self.is_active = True
    
    def update_email(self, new_email: str) -> bool:
        """
        Updates the user's email address after validation.
        
        Args:
            new_email (str): The new email address
        
        Returns:
            bool: True if the email was updated successfully, False otherwise
        """
        if "@" in new_email and "." in new_email.split("@")[1]:
            self.email = new_email
            return True
        return False
    
    def __str__(self) -> str:
        """
        String representation of the user.
        
        Returns:
            str: A formatted string describing the user
        """
        status = "Active" if self.is_active else "Inactive"
        return f"User({self.user_id}): {self.get_full_name()} <{self.email}> [{status}]"
    
    def __repr__(self) -> str:
        """
        Developer representation of the user.
        
        Returns:
            str: A detailed string representation for debugging
        """
        return (f"User(user_id={self.user_id}, username='{self.username}', "
                f"email='{self.email}', first_name='{self.first_name}', "
                f"last_name='{self.last_name}', is_active={self.is_active})")