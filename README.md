# File System Watcher

This Python script is designed to monitor changes within a specified directory and record these changes into a JSON file. Below is an overview of how to use and understand the script.

## Usage

1. **Installation:**
   - Ensure you have Python installed on your system.
   - Install required libraries by running:
     ```
     pip install watchdog
     ```

2. **Configuration:**
   - Open the script file and modify the following variables:
     - `directory_to_watch`: Specify the path to the directory you want to monitor.
     - `json_file_path`: Specify the path for the JSON file where changes will be recorded.

3. **Execution:**
   - Run the script using Python:
     ```
     python run.py
     ```

4. **Understanding Output:**
   - The script will continuously monitor the specified directory.
   - When changes occur (file creations, deletions, modifications), they are recorded into the JSON file specified.
   - Each recorded event includes:
     - `event_type`: Type of event (created, deleted, modified).
     - `file_path`: Path to the file associated with the event.
     - `timestamp`: Timestamp of when the event occurred.

## Example JSON Output

```json
[
    {
        "event_type": "created",
        "file_path": "/path/to/created_file.txt",
        "timestamp": "Tue Mar 16 12:00:00 2024"
    },
    {
        "event_type": "modified",
        "file_path": "/path/to/modified_file.txt",
        "timestamp": "Tue Mar 16 12:05:00 2024"
    }
]
