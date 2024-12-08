"""
Main script for managing the Quantum-Safe System project.
This script acts as an advanced entry point for the entire application, enabling centralized configuration, testing,
and module orchestration.

Dependencies:
- Django framework
- Quantum-safe cryptography libraries
- Blockchain interaction packages
"""

import os
import sys
import logging
import django
from django.core.management import execute_from_command_line
from core.logging import setup_logging
from core.error_handling import handle_exception
from config.environment import load_environment_variables

# Setting up logging
logger = logging.getLogger(__name__)

# Define project settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def initialize_django():
    """
    Initializes Django for the project.
    Ensures environment variables are loaded and Django modules are ready to use.
    """
    try:
        logger.info("Loading environment variables...")
        load_environment_variables()
        logger.info("Initializing Django framework...")
        django.setup()
        logger.info("Django initialized successfully.")
    except Exception as e:
        logger.critical("Failed to initialize Django.", exc_info=True)
        raise e


def run_management_command(command: list):
    """
    Executes a Django management command.
    Args:
        command (list): A list containing the management command and its arguments.
    """
    try:
        logger.info(f"Executing management command: {' '.join(command)}")
        execute_from_command_line(command)
    except Exception as e:
        logger.error(f"Management command failed: {command[1]}", exc_info=True)
        raise e


def display_menu():
    """
    Displays an interactive menu for managing project tasks.
    """
    menu_options = {
        "1": "Run Development Server",
        "2": "Apply Migrations",
        "3": "Create Superuser",
        "4": "Run Tests",
        "5": "Generate Quantum-Safe Keys",
        "6": "Exit"
    }
    print("\nQuantum-Safe System Management Menu:")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    choice = input("\nSelect an option (1-6): ")
    return choice


def main():
    """
    Main function to manage the Quantum-Safe System.
    Provides a CLI for performing various project-related tasks.
    """
    try:
        # Initialize logging and Django
        setup_logging()
        initialize_django()

        while True:
            choice = display_menu()
            if choice == "1":
                run_management_command([sys.argv[0], "runserver"])
            elif choice == "2":
                run_management_command([sys.argv[0], "migrate"])
            elif choice == "3":
                run_management_command([sys.argv[0], "createsuperuser"])
            elif choice == "4":
                run_management_command([sys.argv[0], "test"])
            elif choice == "5":
                from key_management.views import generate_keys
                logger.info("Generating quantum-safe keys...")
                result = generate_keys()
                logger.info(f"Quantum-safe keys generated: {result}")
            elif choice == "6":
                logger.info("Exiting the Quantum-Safe System management.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    except Exception as main_exception:
        handle_exception(main_exception)
        sys.exit(1)


if __name__ == "__main__":
    main()
  
