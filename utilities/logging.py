"""
Advanced Logging Framework for Quantum-Safe Encryption System.

This module sets up logging to ensure system-wide traceability of operations.
Logs are written to both console and log files, supporting multiple verbosity levels.

Features:
    - Console and file logging.
    - Log rotation to manage file sizes.
    - Structured log messages with timestamps, levels, and module names.
"""

import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging():
    """
    Configure the logging framework with console and file handlers.

    Logging Levels:
        - DEBUG: Detailed information for debugging.
        - INFO: General system events and operations.
        - WARNING: Potential issues that do not stop execution.
        - ERROR: Recoverable errors and exceptions.
        - CRITICAL: Non-recoverable errors causing termination.

    Log Files:
        - Logs are saved in the `logs/` directory, with rotation to manage sizes.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a rotating file handler
    log_file = os.path.join(log_dir, "system.log")
    file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Define log format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the root logger
    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])

    logging.info("Logging system initialized.")
