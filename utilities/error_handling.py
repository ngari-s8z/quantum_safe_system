"""
Custom Error Handling Framework for Quantum-Safe Encryption System.

This module defines a comprehensive framework for managing exceptions
and error reporting across all components of the system.

Features:
    - Custom exception hierarchy for cryptographic errors.
    - Centralized error logging.
    - Structured tracebacks for debugging.
"""

import logging
import traceback


class EncryptionSystemError(Exception):
    """
    Base class for all custom exceptions in the Quantum-Safe Encryption System.
    """
    def __init__(self, message):
        super().__init__(message)
        logging.error(f"EncryptionSystemError: {message}")


class KeyManagementError(EncryptionSystemError):
    """
    Exception raised for errors in key generation, exchange, or storage.
    """
    def __init__(self, message="Key management error occurred."):
        super().__init__(message)


class EncryptionError(EncryptionSystemError):
    """
    Exception raised for errors during encryption or decryption processes.
    """
    def __init__(self, message="Encryption error occurred."):
        super().__init__(message)


class FileHandlingError(EncryptionSystemError):
    """
    Exception raised for errors in secure file handling operations.
    """
    def __init__(self, message="File handling error occurred."):
        super().__init__(message)


def handle_exception(e):
    """
    Centralized exception handling function.

    Logs the exception details and provides structured tracebacks for debugging.

    Args:
        e (Exception): The exception instance to handle.
    """
    logging.error("An exception occurred.")
    logging.error(traceback.format_exc())
    print(f"An error occurred: {str(e)}")
