"""
Key Generation Utilities for Quantum-Safe Encryption System.

This module provides:
    - Secure generation of symmetric keys (AES).
    - Quantum-safe public-private key pair generation.
    - Key derivation using PBKDF2 for user-defined passphrases.

Features:
    - Follows best practices for entropy and randomness.
    - Integrates with post-quantum cryptographic libraries.
"""

import os
import hashlib
from Cryptodome.Protocol.KDF import PBKDF2
from encryption.pqc_algorithms import generate_lattice_keypair


def generate_symmetric_key():
    """
    Generate a secure symmetric encryption key.

    Returns:
        bytes: A 256-bit symmetric key (32 bytes).
    """
    key = os.urandom(32)  # 256-bit key
    return key


def generate_pqc_keypair():
    """
    Generate a public-private key pair using post-quantum cryptography.

    Returns:
        tuple: (public_key, private_key)
    """
    return generate_lattice_keypair()


def derive_key_from_passphrase(passphrase, salt=None):
    """
    Derive a cryptographic key from a user-defined passphrase using PBKDF2.

    Args:
        passphrase (str): The passphrase to derive the key from.
        salt (bytes): Optional salt for the key derivation. If not provided, a new one is generated.

    Returns:
        tuple: (derived_key, salt) where derived_key is the 256-bit key.
    """
    if salt is None:
        salt = os.urandom(16)  # Generate a random 128-bit salt
    key = PBKDF2(passphrase, salt, dkLen=32, count=100000, hmac_hash_module=hashlib.sha256)
    return key, salt
