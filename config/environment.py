"""
Environment Configuration Loader for the Quantum-Safe Encryption System.

This module centralizes access to environment variables and deployment configurations.
It ensures that all environment-specific settings are:
    - Modular and maintainable.
    - Loaded with sensible defaults for local development.
    - Overridden by deployment-specific configurations in production.

Features:
    - Secure handling of environment variables.
    - Support for custom configurations based on deployment stages (e.g., dev, staging, prod).
"""

import os

# Default environment configurations
ENV_DEFAULTS = {
    "APP_ENV": "development",  # Options: development, staging, production
    "LOG_LEVEL": "INFO",  # Default logging level
    "ENABLE_QKD": True,  # Toggle Quantum Key Distribution simulation
    "DEBUG": False,  # Enable or disable debugging mode
    "DATA_STORAGE_PATH": "data/",  # Default path for secure data storage
}


def get_env_setting(key, default=None):
    """
    Retrieve an environment setting with a fallback to defaults.

    Args:
        key (str): The name of the environment variable to retrieve.
        default: The default value to return if the variable is not set.

    Returns:
        str | bool | int: The value of the environment variable or the default.

    Example:
        >>> get_env_setting("APP_ENV")
        'development'
    """
    return os.getenv(key, default if default is not None else ENV_DEFAULTS.get(key))


class EnvironmentConfig:
    """
    A centralized class for managing and exposing environment-specific settings.

    Attributes:
        app_env (str): The current application environment (dev, staging, prod).
        log_level (str): The logging level for the application.
        enable_qkd (bool): Whether to enable Quantum Key Distribution simulation.
        debug_mode (bool): Whether the application is running in debug mode.
        data_storage_path (str): The default path for storing secure files.
    """

    def __init__(self):
        self.app_env = get_env_setting("APP_ENV")
        self.log_level = get_env_setting("LOG_LEVEL")
        self.enable_qkd = get_env_setting("ENABLE_QKD", default=True)
        self.debug_mode = get_env_setting("DEBUG", default=False)
        self.data_storage_path = get_env_setting("DATA_STORAGE_PATH")

    def is_production(self):
        """
        Check if the current environment is production.

        Returns:
            bool: True if the environment is production, False otherwise.
        """
        return self.app_env == "production"

    def __repr__(self):
        """
        Return a string representation of the environment configuration.
        """
        return (
            f"EnvironmentConfig(app_env='{self.app_env}', "
            f"log_level='{self.log_level}', enable_qkd={self.enable_qkd}, "
            f"debug_mode={self.debug_mode}, data_storage_path='{self.data_storage_path}')"
        )


# Initialize a global environment configuration instance
GLOBAL_ENV_CONFIG = EnvironmentConfig()

# Log environment configuration (in debug mode only)
if GLOBAL_ENV_CONFIG.debug_mode:
    print("Environment Configuration:", repr(GLOBAL_ENV_CONFIG))
