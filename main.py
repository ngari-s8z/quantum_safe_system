"""
Main entry point for the Quantum-Safe Encryption System.

This script orchestrates the initialization, configuration, and GUI startup for the encryption platform.
It serves as the central hub for managing user interactions, module imports, and system configurations.

Modules:
    - Config: Loads system-wide settings and environment configurations.
    - GUI: Launches the graphical user interface for ease of use.
    - Logging: Provides advanced logging for debugging and monitoring purposes.
    - Testing: Offers utilities to validate cryptographic functionalities before production use.

Author:
    Quantum Security Development Team

Version:
    1.0.0
"""

import logging
import sys
from config.settings import DEFAULT_PQC_ALGORITHMS, SYMMETRIC_KEY_SIZE
from gui.main_window import MainWindow
from utilities.logging import setup_logging
from tests.test_suite import run_all_tests


def initialize_logging():
    """
    Initialize the logging framework for the system.
    Logs are written to both console and log files for debugging and monitoring purposes.
    """
    setup_logging()
    logging.info("Logging initialized successfully.")


def load_configuration():
    """
    Load system configurations, including cryptographic settings and environment variables.
    Prints the selected algorithms and parameters to the console for verification.

    Returns:
        dict: Dictionary of system settings.
    """
    logging.info("Loading system configuration...")
    config = {
        "default_algorithms": DEFAULT_PQC_ALGORITHMS,
        "symmetric_key_size": SYMMETRIC_KEY_SIZE,
    }
    logging.info(f"Configuration loaded: {config}")
    return config


def validate_system():
    """
    Perform a series of system validation checks, including:
        - Verifying cryptographic libraries.
        - Ensuring compatibility with post-quantum algorithms.
        - Running unit tests on critical modules.

    If any validation fails, the system will terminate with an error message.
    """
    logging.info("Running system validation...")
    try:
        run_all_tests()  # Executes all unit and integration tests.
        logging.info("System validation successful. All tests passed.")
    except Exception as e:
        logging.error(f"System validation failed: {str(e)}")
        sys.exit("Critical system validation error. Exiting...")


def start_gui(config):
    """
    Launch the graphical user interface for the Quantum-Safe Encryption System.

    Args:
        config (dict): System configuration dictionary passed to the GUI for customization.
    """
    logging.info("Starting the GUI...")
    try:
        app = MainWindow(config)
        app.run()
    except Exception as e:
        logging.error(f"Failed to start GUI: {str(e)}")
        sys.exit("Unable to launch the GUI. Please check logs for details.")


def display_welcome_message():
    """
    Display a welcome banner and brief description of the system to the console.
    """
    banner = """
    ==============================================================
                Quantum-Safe Encryption System v1.0
    --------------------------------------------------------------
    Protect your data in the quantum age with cutting-edge
    post-quantum cryptography and an intuitive encryption platform.
    ==============================================================
    """
    print(banner)
    logging.info("Welcome message displayed.")


def main():
    """
    Main function that orchestrates the execution of the Quantum-Safe Encryption System.
    Includes the following steps:
        1. Displaying a welcome message.
        2. Initializing logging.
        3. Loading configuration settings.
        4. Validating the system through rigorous checks.
        5. Starting the graphical user interface.

    If any step fails, the system gracefully exits with appropriate error messaging.
    """
    try:
        display_welcome_message()
        initialize_logging()
        config = load_configuration()
        validate_system()
        start_gui(config)
    except KeyboardInterrupt:
        logging.warning("System interrupted by user. Exiting...")
        sys.exit("User terminated the process.")
    except Exception as e:
        logging.critical(f"Unexpected error occurred: {str(e)}")
        sys.exit("System encountered an unexpected error. Check logs for details.")


if __name__ == "__main__":
    main()
