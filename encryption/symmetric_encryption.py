"""
Symmetric Encryption Mechanisms for Quantum-Safe Encryption System.

This module provides implementations for symmetric encryption algorithms:
    - AES-256 in GCM mode for authenticated encryption.
"""

from Cryptodome.Cipher import AES
import os


def aes_encrypt(data, key):
    """
    Encrypt data using AES-256 in GCM mode.

    Args:
        data (bytes): Data to encrypt.
        key (bytes): 256-bit encryption key.

    Returns:
        dict: Encrypted data and associated metadata (e.g., nonce, tag).
    """
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return {
        "ciphertext": ciphertext,
        "nonce": cipher.nonce,
        "tag": tag,
    }


def aes_decrypt(payload, key):
    """
    Decrypt data encrypted with AES-256 in GCM mode.

    Args:
        payload (dict): Encrypted data, nonce, and tag.
        key (bytes): 256-bit encryption key.

    Returns:
        bytes: Decrypted plaintext.
    """
    cipher = AES.new(key, AES.MODE_GCM, nonce=payload["nonce"])
    plaintext = cipher.decrypt_and_verify(payload["ciphertext"], payload["tag"])
    return plaintext
