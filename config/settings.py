"""
System-Wide Cryptographic Settings for the Quantum-Safe Encryption System.

This module defines:
    - Default cryptographic algorithms and their parameters.
    - Key sizes and security parameters for encryption.
    - Toggleable simulation options for advanced quantum key distribution (QKD).

Features:
    - Modular cryptographic settings to allow easy upgrades to new algorithms.
    - Constants for both symmetric and post-quantum encryption.
    - Integration with `environment.py` for environment-specific overrides.
"""

from config.environment import get_env_setting

# Post-Quantum Cryptography Algorithms (selected based on NIST recommendations)
DEFAULT_PQC_ALGORITHMS = {
    "key_exchange": "Kyber",  # Lattice-based algorithm
    "digital_signatures": "XMSS",  # Hash-based signatures
    "hashing": "SHA3-512"  # Quantum-safe cryptographic hashing
}

# Symmetric Encryption Algorithms
SYMMETRIC_ENCRYPTION = {
    "algorithm": "AES",
    "key_size": 256,  # AES-256 for robust symmetric encryption
    "mode": "GCM"  # Galois/Counter Mode for authenticated encryption
}

# Quantum Key Distribution (QKD) Simulation Settings
QKD_SETTINGS = {
    "enabled": get_env_setting("ENABLE_QKD", default=True),
    "simulator": "QuantumSimulator"  # Placeholder for quantum simulation library
}

# Advanced Security Settings
SECURITY_PARAMS = {
    "enable_forward_secrecy": True,
    "min_password_entropy": 16,  # Minimum password entropy for user authentication
    "hash_iterations": 100000,  # PBKDF2 hashing iterations for password storage
}

# Logging cryptographic settings (debugging purpose only)
if get_env_setting("DEBUG", default=False):
    print("Cryptographic Settings Loaded:", {
        "DEFAULT_PQC_ALGORITHMS": DEFAULT_PQC_ALGORITHMS,
        "SYMMETRIC_ENCRYPTION": SYMMETRIC_ENCRYPTION,
        "QKD_SETTINGS": QKD_SETTINGS,
        "SECURITY_PARAMS": SECURITY_PARAMS,
    })
