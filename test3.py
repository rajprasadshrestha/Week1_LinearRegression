# This script has several issues:
# - Hardcoded IP address
# - No logging
# - Function with too many parameters
# - Long method

import json

def process_data(data, param1, param2, param3, param4, param5, param6):
    # Function with too many parameters
    result = {}
    for key, value in data.items():
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

def main():
    # Hardcoded IP address
    server_ip = "192.168.1.1"
    print(f"Connecting to server at {server_ip}")

    # No logging
    data = {"key1": "value1", "key2": "value2", "key3": "value3"}
    processed_data = process_data(data, 1, 2, 3, 4, 5, 6)
    print(json.dumps(processed_data, indent=4))

if __name__ == "__main__":
    main()