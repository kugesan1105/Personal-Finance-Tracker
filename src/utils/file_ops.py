"""
File Operations Utilities

Provides helper functions for reading and writing files.
These utilities handle common file operations with error handling.
"""

import os
from typing import Optional


def read_file(file_path: str, encoding: str = "utf-8") -> Optional[str]:
    """
    Reads the contents of a file and returns it as a string.
    
    Args:
        file_path (str): The path to the file to read
        encoding (str): The file encoding (default: utf-8)
    
    Returns:
        Optional[str]: The file contents as a string, or None if reading fails
    
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None


def write_file(file_path: str, content: str, encoding: str = "utf-8") -> bool:
    """
    Writes content to a file, creating directories if necessary.
    
    Args:
        file_path (str): The path where the file should be written
        content (str): The content to write to the file
        encoding (str): The file encoding (default: utf-8)
    
    Returns:
        bool: True if the file was written successfully, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(file_path, 'w', encoding=encoding) as file:
            file.write(content)
        
        print(f"Successfully wrote file: {file_path}")
        return True
    
    except IOError as e:
        print(f"Error writing file '{file_path}': {e}")
        return False


def file_exists(file_path: str) -> bool:
    """
    Checks if a file exists at the specified path.
    
    Args:
        file_path (str): The path to check
    
    Returns:
        bool: True if the file exists, False otherwise
    """
    return os.path.isfile(file_path)


def get_file_size(file_path: str) -> Optional[int]:
    """
    Gets the size of a file in bytes.
    
    Args:
        file_path (str): The path to the file
    
    Returns:
        Optional[int]: The file size in bytes, or None if the file doesn't exist
    """
    try:
        return os.path.getsize(file_path)
    except OSError:
        return None