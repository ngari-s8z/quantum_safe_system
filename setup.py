import os

# Define the project structure (relative to the current directory)
structure = {
    "authentication": ["migrations", "admin.py", "apps.py", "models.py", "serializers.py", "tests.py", "urls.py", "views.py"],
    "blockchain": ["migrations", "admin.py", "apps.py", "models.py", "serializers.py", "tests.py", "urls.py", "views.py"],
    "communication": ["migrations", "admin.py", "apps.py", "models.py", "serializers.py", "tests.py", "urls.py", "views.py"],
    "config": ["__init__.py", "asgi.py", "settings.py", "urls.py", "wsgi.py", "environment.py"],
    "core": ["__init__.py", "error_handling.py", "file_operations.py", "logging.py", "permissions.py"],
    "encryption": ["migrations", "admin.py", "apps.py", "models.py", "serializers.py", "tests.py", "urls.py", "views.py"],
    "examples": ["blockchain_key_management.py", "encrypt_file.py", "secure_communication.py"],
    "frontend": ["README.md"],
    "hashing": ["migrations", "admin.py", "apps.py", "models.py", "serializers.py", "tests.py", "urls.py", "views.py"],
    "key_management": ["migrations", "admin.py", "apps.py", "models.py", "serializers.py", "tests.py", "urls.py", "views.py"],
    "tests": [
        "test_authentication.py",
        "test_blockchain.py",
        "test_communication.py",
        "test_encryption.py",
        "test_key_management.py",
        "test_smart_contracts.py",
    ],
}

# Create directories and files relative to the current directory
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, list):
            # Create a directory and files inside it
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                file_path = os.path.join(path, file_name)
                if not os.path.exists(file_path):
                    with open(file_path, "w") as f:
                        f.write(f"# {file_name}\n")
                        if file_name.endswith(".py"):
                            f.write(f"# This is {file_name} for the {name} app\n")
        elif isinstance(content, dict):
            # Recursively create directories
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)

# Run the setup
if __name__ == "__main__":
    print("Creating project structure...")
    create_structure(".", structure)  # Use the current directory as the base path
    print("Project structure created successfully!")
