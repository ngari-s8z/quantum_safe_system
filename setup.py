import os



# Define the folder structure

folder_structure = {

    "quantum_safe_system": [

        "README.md",

        "requirements.txt",

        "main.py",

        {

            "config": ["settings.py", "environment.py"],

            "encryption": [

                "__init__.py",

                "pqc_algorithms.py",

                "hybrid_encryption.py",

                "symmetric_encryption.py",

                "quantum_encryption.py",

            ],

            "key_management": [

                "__init__.py",

                "key_generation.py",

                "key_exchange.py",

                "key_storage.py",

            ],

            "authentication": [

                "__init__.py",

                "hash_signatures.py",

                "forward_secrecy.py",

            ],

            "communication": [

                "__init__.py",

                "quantum_key_distribution.py",

                "tls_protocol.py",

            ],

            "hashing": [

                "__init__.py",

                "sha3_hashing.py",

                "integrity_verification.py",

            ],

            "gui": [

                "__init__.py",

                "main_window.py",

                "encryption_gui.py",

                "key_management_gui.py",

                "settings_gui.py",

            ],

            "utilities": [

                "__init__.py",

                "logging.py",

                "error_handling.py",

                "file_operations.py",

            ],

            "tests": [

                "test_encryption.py",

                "test_key_management.py",

                "test_authentication.py",

                "test_communication.py",

            ],

            "examples": ["encrypt_file.py", "secure_communication.py"],

        },

    ]

}



# Function to create files and folders

def create_structure(base_path, structure):

    for item in structure:

        if isinstance(item, str):

            # Create a file

            file_path = os.path.join(base_path, item)

            with open(file_path, 'w') as f:

                pass  # Create an empty file

        elif isinstance(item, dict):

            # Create subfolders recursively

            for folder, sub_items in item.items():

                folder_path = os.path.join(base_path, folder)

                os.makedirs(folder_path, exist_ok=True)

                create_structure(folder_path, sub_items)



# Base directory

base_dir = "quantum_safe_system"

os.makedirs(base_dir, exist_ok=True)



# Create the folder structure

create_structure(base_dir, folder_structure["quantum_safe_system"])
