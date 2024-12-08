"""
Secure Key Exchange Protocols for Quantum-Safe Encryption System.

This module implements:
    - Lattice-based key exchange for quantum-safe communication.
    - Hybrid key exchange combining symmetric and post-quantum cryptography.
"""

from encryption.pqc_algorithms import lattice_encrypt, lattice_decrypt
from key_management.key_generation import generate_pqc_keypair, generate_symmetric_key


def quantum_safe_key_exchange():
    """
    Perform a quantum-safe key exchange using lattice-based cryptography.

    Returns:
        tuple: (shared_secret, encrypted_symmetric_key)
    """
    # Generate key pair
    public_key, private_key = generate_pqc_keypair()

    # Generate symmetric key
    symmetric_key = generate_symmetric_key()

    # Encrypt symmetric key using lattice-based cryptography
    encrypted_key = lattice_encrypt(symmetric_key, public_key)

    # Simulate sharing the encrypted key (would normally be transmitted over a secure channel)
    decrypted_key = lattice_decrypt(encrypted_key, private_key)

    return decrypted_key, encrypted_key


def hybrid_key_exchange():
    """
    Perform a hybrid key exchange combining symmetric and PQC encryption.

    Returns:
        dict: Hybrid key exchange payload including encrypted data and keys.
    """
    shared_secret, encrypted_symmetric_key = quantum_safe_key_exchange()

    return {
        "shared_secret": shared_secret,
        "encrypted_symmetric_key": encrypted_symmetric_key,
    }
  
