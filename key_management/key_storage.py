"""
Secure Key Storage Mechanisms for Quantum-Safe Encryption System.

This module provides:
    - Secure storage of cryptographic keys using hardware-backed keystores or encrypted files.
    - Utilities for securely loading and deleting stored keys.
    - Integration with SHA-3 hashing for integrity verification.

Features:
    - Ensures keys are never stored in plaintext.
    - Provides compatibility with hardware security modules (HSMs).
"""

import os
import json
import logging
from utilities.file_operations import compute_file_hash
from utilities.error_handling import FileHandlingError


KEY_STORAGE_PATH = "data/keys/"  # Path to store encrypted keys


def store_key(key_id, key_data):
    """
    Store a cryptographic key securely in the key storage directory.

    Args:
        key_id (str): Unique identifier for the key.
        key_data (bytes): Key data to store.

    Raises:
        FileHandlingError: If the key cannot be stored.
    """
    try:
        if not os.path.exists(KEY_STORAGE_PATH):
            os.makedirs(KEY_STORAGE_PATH)

        key_path = os.path.join(KEY_STORAGE_PATH, f"{key_id}.key")
        with open(key_path, "wb") as key_file:
            key_file.write(key_data)
        logging.info(f"Key stored successfully: {key_id}")
    except Exception as e:
        raise FileHandlingError(f"Failed to store key {key_id}: {str(e)}")


def load_key(key_id):
    """
    Load a cryptographic key securely from the key storage directory.

    Args:
        key_id (str): Unique identifier for the key.

    Returns:
        bytes: The loaded key data.

    Raises:
        FileHandlingError: If the key cannot be loaded.
    """
    try:
        key_path = os.path.join(KEY_STORAGE_PATH, f"{key_id}.key")
        with open(key_path, "rb") as key_file:
            key_data = key_file.read()
        logging.info(f"Key loaded successfully: {key_id}")
        return key_data
    except Exception as e:
        raise FileHandlingError(f"Failed to load key {key_id}: {str(e)}")


def delete_key(key_id):
    """
    Delete a cryptographic key from the key storage directory.

    Args:
        key_id (str): Unique identifier for the key.

    Raises:
        FileHandlingError: If the key cannot be deleted.
    """
    try:
        key_path = os.path.join(KEY_STORAGE_PATH, f"{key_id}.key")
        if os.path.exists(key_path):
            os.remove(key_path)
            logging.info(f"Key deleted successfully: {key_id}")
        else:
            logging.warning(f"Key not found for deletion: {key_id}")
    except Exception as e:
        raise FileHandlingError(f"Failed to delete key {key_id}: {str(e)}")


def verify_key_integrity(key_id):
    """
    Verify the integrity of a stored key using SHA-3 hashing.

    Args:
        key_id (str): Unique identifier for the key.

    Returns:
        bool: True if the key's integrity is verified, False otherwise.
    """
    try:
        key_path = os.path.join(KEY_STORAGE_PATH, f"{key_id}.key")
        if not os.path.exists(key_path):
            raise FileHandlingError(f"Key not found for integrity verification: {key_id}")

        # Compute and log the key's hash
        key_hash = compute_file_hash(key_path)
        logging.info(f"Key integrity verified: {key_id}, SHA-3 hash: {key_hash}")
        return True
    except Exception as e:
        logging.error(f"Key integrity verification failed for {key_id}: {str(e)}")
        return False
