# This script has several issues:
# - Hardcoded credentials
# - No exception handling
# - Unused imports
# - Code duplication

import os
import sys

# Hardcoded credentials
username = "admin"
password = "password123"

def connect_to_database():
    # No exception handling
    connection = f"Connecting to database with username: {username} and password: {password}"
    print(connection)
    return connection

def main():
    connect_to_database()
    connect_to_database()  # Code duplication

if __name__ == "__main__":
    main()