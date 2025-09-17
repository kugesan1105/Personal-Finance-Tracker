"""
Unit tests for utility functions.

Tests the file operations and mathematical operations utilities.
"""

import unittest
import tempfile
import os
from unittest.mock import patch, mock_open

# Add src to path for imports
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils.file_ops import read_file, write_file, file_exists, get_file_size
from utils.math_ops import add, multiply, calculate_average, percentage_change


class TestFileOps(unittest.TestCase):
    """Test cases for file operations utilities."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_content = "This is test content\nLine 2\nLine 3"
    
    def test_write_and_read_file(self):
        """Test writing and reading a file."""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_path = temp_file.name
        
        try:
            # Test writing
            result = write_file(temp_path, self.test_content)
            self.assertTrue(result)
            
            # Test reading
            content = read_file(temp_path)
            self.assertEqual(content, self.test_content)
        finally:
            # Clean up
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_read_nonexistent_file(self):
        """Test reading a file that doesn't exist."""
        result = read_file("nonexistent_file.txt")
        self.assertIsNone(result)
    
    def test_file_exists(self):
        """Test file existence checking."""
        with tempfile.NamedTemporaryFile() as temp_file:
            # File exists
            self.assertTrue(file_exists(temp_file.name))
        
        # File doesn't exist after deletion
        self.assertFalse(file_exists(temp_file.name))
    
    def test_get_file_size(self):
        """Test getting file size."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(self.test_content)
            temp_path = temp_file.name
        
        try:
            size = get_file_size(temp_path)
            self.assertIsInstance(size, int)
            self.assertGreater(size, 0)
            
            # Test nonexistent file
            nonexistent_size = get_file_size("nonexistent.txt")
            self.assertIsNone(nonexistent_size)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)


class TestMathOps(unittest.TestCase):
    """Test cases for mathematical operations utilities."""
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0.5, 0.3), 0.8)
        self.assertEqual(add(-5, -3), -8)
    
    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(0.5, 4), 2.0)
    
    def test_calculate_average(self):
        """Test average calculation function."""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([10]), 10.0)
        self.assertEqual(calculate_average([2.5, 3.5]), 3.0)
        
        # Test empty list
        with self.assertRaises(ValueError):
            calculate_average([])
        
        # Test non-numeric values
        with self.assertRaises(TypeError):
            calculate_average([1, 2, "three"])
    
    def test_percentage_change(self):
        """Test percentage change calculation."""
        self.assertEqual(percentage_change(100, 120), 20.0)
        self.assertEqual(percentage_change(50, 25), -50.0)
        self.assertEqual(percentage_change(10, 10), 0.0)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            percentage_change(0, 10)


if __name__ == '__main__':
    # Create a test suite combining all test classes
    suite = unittest.TestSuite()
    
    # Add all test methods from TestFileOps
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFileOps))
    
    # Add all test methods from TestMathOps
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathOps))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)