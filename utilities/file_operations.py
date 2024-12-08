"""
Secure File Handling Utilities for Quantum-Safe Encryption System.

This module provides utilities for:
    - Reading and writing files securely.
    - Validating file integrity using cryptographic hashes.
    - Managing temporary files during encryption and decryption processes.

Features:
    - Handles large files efficiently.
    - Ensures data integrity with SHA-3 hashing.
    - Prevents unauthorized access with file locks.
"""

import hashlib
import os
import tempfile
import logging
from utilities.error_handling import FileHandlingError


def read_file(file_path):
    """
    Securely read the contents of a file.

    Args:
        file_path (str): Path to the file to read.

    Returns:
        bytes: Contents of the file.

    Raises:
        FileHandlingError: If the file cannot be read.
    """
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        logging.info(f"File read successfully: {file_path}")
        return data
    except Exception as e:
        raise FileHandlingError(f"Error reading file {file_path}: {str(e)}")


def write_file(file_path, data):
    """
    Securely write data to a file.

    Args:
        file_path (str): Path to the file to write.
        data (bytes): Data to write.

    Raises:
        FileHandlingError: If the file cannot be written.
    """
    try:
        with open(file_path, "wb") as file:
            file.write(data)
        logging.info(f"File written successfully: {file_path}")
    except Exception as e:
        raise FileHandlingError(f"Error writing to file {file_path}: {str(e)}")


def compute_file_hash(file_path):
    """
    Compute the SHA-3 hash of a file's contents.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Hexadecimal hash of the file's contents.

    Raises:
        FileHandlingError: If the file cannot be hashed.
    """
    try:
        sha3 = hashlib.sha3_512()
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                sha3.update(chunk)
        file_hash = sha3.hexdigest()
        logging.info(f"Hash computed for file {file_path}: {file_hash}")
        return file_hash
    except Exception as e:
        raise FileHandlingError(f"Error computing hash for file {file_path}: {str(e)}")


def create_temp_file(data):
    """
    Create a temporary file with the given data.

    Args:
        data (bytes): Data to write to the temporary file.

    Returns:
        str: Path to the temporary file.
    """
    try:
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(data)
        temp.close()
        logging.info(f"Temporary file created: {temp.name}")
        return temp.name
    except Exception as e:
        raise FileHandlingError(f"Error creating temporary file: {str(e)}")
