# hq88-domain-history-checker
Domain history checker. Checks the oldest and newest timestamps of archived captures and the total number of archived captures for a domain.

A Python 3 script that retrieves historical archive information for a given domain using the Internet Archive Wayback Machine.

The script uses the Wayback Machine CDX Server API to retrieve the following information:

Oldest Capture: The date of the earliest archived snapshot of a domain.

Newest Capture: The date of the most recent archived snapshot of a domain.

Total Captures: The total number of archived snapshots available for the domain.

Execution Time: The time required to process the domain.

1. Installation
Requirements
Make sure the following requirements are installed on your system:

Python 3.7 or later
pip (Python package manager)
Internet connection
Step 1: Clone the Repository
Clone this repository to your local machine:
```
#!/bin/bash
git clone https://github.com/the-non-binary-tree/hq88-domain-history-checker
```
Navigate to the project directory:
```
#!/bin/bash
cd <repository-directory>
```

Step 2: Create a Virtual Environment (OPTIONAL but Recommended)
Create a Python virtual environment:
```
#!/bin/bash
python3 -m venv venv
```
Activate the virtual environment.
Linux / macOS:
```
#!/bin/bash
source venv/bin/activate
```
Windows:

```
#!/bin/bash
venv\Scripts\activate
```

Step 3: Install Dependencies
This script requires the waybackpy Python library to interact with the Wayback Machine CDX Server API.
Install it using pip:
```
#!/bin/bash
pip install waybackpy
```
Alternatively, you can install dependencies from a requirements.txt file.
Create a file named requirements.txt containing:
```
#text
waybackpy
```
Then run:
```
#!/bin/bash
pip install -r requirements.txt
```

Step 4: Verify Installation
Verify that the dependency has been installed successfully:
```
#!/bin/bash
pip show waybackpy
```
You are now ready to run the script.

2. Usage
Basic Usage
Run the script with a target domain as a command-line argument:
```
#!/bin/bash
python3 wayback_api_caller.py example.com
```
Run Without Arguments
If no domain is provided, the script automatically uses example.com as the default target:
bash
```
#!/bin/bash
python3 wayback_api_caller.py
```
Example
Run the script against a target domain:
bash
```
#!/bin/bash
python3 wayback_api_caller.py google.com
```
Example output:
```
Xử lý domain: google.com
Kết quả xa nhất: 11-11-1998
Kết quả gần nhất: 16-11-2026
Tổng số save time: 1500
Thời gian xử lý domain google.com: 2.345678 giây
```
Note: The output above is illustrative. Actual results depend on the available Wayback Machine archives and network conditions.

Command-Line Arguments
| Argument	| Required |	Description
| --- | --- | --- |
| domain	| No	| The domain to query. Defaults to example.com if omitted.|


Functions Overview

The script consists of three main functions:

Function	Description

`get_oldest_capture(domain)`:	Retrieves the oldest archived snapshot date.
`get_newest_capture(domain)`:	Retrieves the newest archived snapshot date.
`get_capture_count(domain)`:	Counts the total number of archived snapshots.

Execution Time

The script uses Python's time.perf_counter() to measure the total execution time.
The execution time includes all three Wayback Machine queries:
Retrieving the oldest capture.
Retrieving the newest capture.
Counting all available snapshots.
The result is displayed in seconds with six decimal places.

Notes and Limitations

The script requires an active internet connection.
Results depend on the availability of the Internet Archive Wayback Machine CDX Server.
Some domains may not have any archived snapshots.
The total capture count may take longer for domains with a large archive history because the script iterates through all available snapshots.
Network latency and API response time may affect overall execution time.
The script currently handles NoCDXRecordFound exceptions when retrieving the oldest and newest captures. Other network or API errors may still cause execution to fail.

License

This project is provided for research and educational purposes.
