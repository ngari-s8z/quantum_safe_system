"""
Hybrid Encryption Schemes Combining Symmetric and Post-Quantum Cryptography.

This module implements a hybrid encryption model:
    - Symmetric encryption for data confidentiality.
    - Post-quantum cryptography (PQC) for secure key exchange.
"""

from encryption.symmetric_encryption import aes_encrypt, aes_decrypt
from encryption.pqc_algorithms import generate_lattice_keypair, lattice_encrypt, lattice_decrypt


def hybrid_encrypt(data):
    """
    Perform hybrid encryption:
    1. Generate a symmetric key.
    2. Encrypt the data using symmetric encryption.
    3. Encrypt the symmetric key using lattice-based PQC.

    Args:
        data (bytes): Data to encrypt.

    Returns:
        dict: Encrypted payload containing ciphertext and encrypted key.
    """
    symmetric_key = os.urandom(32)  # 256-bit symmetric key
    encrypted_data = aes_encrypt(data, symmetric_key)
    public_key, private_key = generate_lattice_keypair()
    encrypted_key = lattice_encrypt(symmetric_key, public_key)

    return {
        "ciphertext": encrypted_data,
        "encrypted_key": encrypted_key,
        "private_key": private_key,  # For demonstration (not stored like this in production)
    }


def hybrid_decrypt(payload):
    """
    Perform hybrid decryption:
    1. Decrypt the symmetric key using lattice-based PQC.
    2. Decrypt the data using symmetric decryption.

    Args:
        payload (dict): Encrypted payload containing ciphertext and encrypted key.

    Returns:
        bytes: Decrypted plaintext.
    """
    encrypted_key = payload["encrypted_key"]
    private_key = payload["private_key"]
    symmetric_key = lattice_decrypt(encrypted_key, private_key)
    plaintext = aes_decrypt(payload["ciphertext"], symmetric_key)
    return plaintext
