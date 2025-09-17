"""
Unit tests for service functions.

Tests the data service and report service functionality.
"""

import unittest
from datetime import datetime
import os
import sys

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from services.data_service import load_users, load_transactions, create_sample_user, create_sample_transaction
from services.report_service import generate_user_report, generate_transaction_summary
from models.user import User
from models.transaction import Transaction, TransactionType, TransactionStatus


class TestDataService(unittest.TestCase):
    """Test cases for data service functions."""
    
    def test_load_users(self):
        """Test loading sample users."""
        users = load_users()
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)
        
        # Check that all items are User objects
        for user in users:
            self.assertIsInstance(user, User)
            self.assertIsInstance(user.user_id, int)
            self.assertIsInstance(user.username, str)
            self.assertIsInstance(user.email, str)
    
    def test_load_transactions(self):
        """Test loading sample transactions."""
        transactions = load_transactions()
        self.assertIsInstance(transactions, list)
        self.assertGreater(len(transactions), 0)
        
        # Check that all items are Transaction objects
        for transaction in transactions:
            self.assertIsInstance(transaction, Transaction)
            self.assertIsInstance(transaction.transaction_id, int)
            self.assertIsInstance(transaction.user_id, int)
            self.assertIsInstance(transaction.amount, float)
            self.assertIsInstance(transaction.transaction_type, TransactionType)
    
    def test_create_sample_user(self):
        """Test creating a sample user."""
        user = create_sample_user(99, "test_user", "test@example.com", "Test", "User")
        
        self.assertIsInstance(user, User)
        self.assertEqual(user.user_id, 99)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertTrue(user.is_active)
    
    def test_create_sample_transaction(self):
        """Test creating a sample transaction."""
        transaction = create_sample_transaction(
            99, 1, 100.50, TransactionType.DEPOSIT, "Test deposit"
        )
        
        self.assertIsInstance(transaction, Transaction)
        self.assertEqual(transaction.transaction_id, 99)
        self.assertEqual(transaction.user_id, 1)
        self.assertEqual(transaction.amount, 100.50)
        self.assertEqual(transaction.transaction_type, TransactionType.DEPOSIT)
        self.assertEqual(transaction.description, "Test deposit")
        self.assertEqual(transaction.status, TransactionStatus.PENDING)


class TestReportService(unittest.TestCase):
    """Test cases for report service functions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create sample users for testing
        self.test_users = [
            User(1, "john", "john@test.com", "John", "Doe"),
            User(2, "jane", "jane@test.com", "Jane", "Smith"),
        ]
        self.test_users[1].deactivate()  # Make one user inactive
        
        # Create sample transactions for testing
        self.test_transactions = [
            Transaction(1, 1, 100.0, TransactionType.DEPOSIT, "Test deposit"),
            Transaction(2, 2, 50.0, TransactionType.WITHDRAWAL, "Test withdrawal"),
            Transaction(3, 1, 25.0, TransactionType.PAYMENT, "Test payment"),
        ]
        # Complete some transactions
        self.test_transactions[0].complete_transaction()
        self.test_transactions[2].complete_transaction()
    
    def test_generate_user_report(self):
        """Test generating a user report."""
        report = generate_user_report(self.test_users)
        
        self.assertIsInstance(report, str)
        self.assertIn("USER REPORT", report)
        self.assertIn("Total Users: 2", report)
        self.assertIn("Active Users: 1", report)
        self.assertIn("Inactive Users: 1", report)
        self.assertIn("john", report)
        self.assertIn("jane", report)
    
    def test_generate_user_report_empty(self):
        """Test generating a user report with no users."""
        report = generate_user_report([])
        self.assertEqual(report, "No users found in the system.")
    
    def test_generate_transaction_summary(self):
        """Test generating a transaction summary."""
        summary = generate_transaction_summary(self.test_transactions)
        
        self.assertIsInstance(summary, str)
        self.assertIn("TRANSACTION SUMMARY REPORT", summary)
        self.assertIn("Total Transactions: 3", summary)
        self.assertIn("Completed: 2", summary)
        self.assertIn("Pending: 1", summary)
        self.assertIn("deposit", summary.lower())
        self.assertIn("withdrawal", summary.lower())
        self.assertIn("payment", summary.lower())
    
    def test_generate_transaction_summary_empty(self):
        """Test generating a transaction summary with no transactions."""
        summary = generate_transaction_summary([])
        self.assertEqual(summary, "No transactions found in the system.")


class TestUserModel(unittest.TestCase):
    """Test cases for User model functionality."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.user = User(1, "testuser", "test@example.com", "Test", "User")
    
    def test_user_creation(self):
        """Test user object creation."""
        self.assertEqual(self.user.user_id, 1)
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")
        self.assertTrue(self.user.is_active)
    
    def test_get_full_name(self):
        """Test getting full name."""
        self.assertEqual(self.user.get_full_name(), "Test User")
    
    def test_email_validation(self):
        """Test email validation."""
        self.assertTrue(self.user.is_valid_email())
        
        # Test invalid email
        self.user.email = "invalid-email"
        self.assertFalse(self.user.is_valid_email())
    
    def test_activate_deactivate(self):
        """Test user activation and deactivation."""
        self.assertTrue(self.user.is_active)
        
        self.user.deactivate()
        self.assertFalse(self.user.is_active)
        
        self.user.activate()
        self.assertTrue(self.user.is_active)


class TestTransactionModel(unittest.TestCase):
    """Test cases for Transaction model functionality."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.transaction = Transaction(1, 1, 100.0, TransactionType.DEPOSIT, "Test transaction")
    
    def test_transaction_creation(self):
        """Test transaction object creation."""
        self.assertEqual(self.transaction.transaction_id, 1)
        self.assertEqual(self.transaction.user_id, 1)
        self.assertEqual(self.transaction.amount, 100.0)
        self.assertEqual(self.transaction.transaction_type, TransactionType.DEPOSIT)
        self.assertEqual(self.transaction.description, "Test transaction")
        self.assertEqual(self.transaction.status, TransactionStatus.PENDING)
    
    def test_amount_validation(self):
        """Test transaction amount validation."""
        self.assertTrue(self.transaction.is_valid_amount())
        
        # Test negative amount
        negative_transaction = Transaction(2, 1, -50.0, TransactionType.WITHDRAWAL)
        self.assertFalse(negative_transaction.is_valid_amount())
    
    def test_transaction_status_changes(self):
        """Test transaction status changes."""
        self.assertEqual(self.transaction.status, TransactionStatus.PENDING)
        
        self.transaction.complete_transaction()
        self.assertEqual(self.transaction.status, TransactionStatus.COMPLETED)
        self.assertTrue(self.transaction.is_completed())
    
    def test_cancel_transaction(self):
        """Test transaction cancellation."""
        # Can cancel pending transaction
        result = self.transaction.cancel_transaction()
        self.assertTrue(result)
        self.assertEqual(self.transaction.status, TransactionStatus.CANCELLED)
        
        # Cannot cancel already cancelled transaction
        result = self.transaction.cancel_transaction()
        self.assertFalse(result)
    
    def test_formatted_amount(self):
        """Test formatted amount display."""
        self.assertEqual(self.transaction.get_formatted_amount(), "$100.00")


if __name__ == '__main__':
    # Create a test suite combining all test classes
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [TestDataService, TestReportService, TestUserModel, TestTransactionModel]
    
    for test_class in test_classes:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_class))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)