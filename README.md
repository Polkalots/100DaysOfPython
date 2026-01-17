### This repository has been created as a way to document my progess in my quest to learn python. Challenges have been created with a focus on cyber security related tasks, with the overall challenge divided into 5 different phases, as follows:

#### PHASE 1 — FOUNDATIONS WITH PURPOSE (Days 1–20)

Write a script that reads a text file and prints the number of lines.

Count how many times each word appears in a file (simple frequency counter).

Extract all IP addresses from a text file using regex.

Extract all email addresses from text.

Identify the top 5 most common IPs in a log file.

Write a function that checks if a password meets complexity rules.

Build a simple "log cleaner" that removes empty lines & comments.

Convert a CSV of users into a list of dictionaries.

Read JSON logs and print specific fields (e.g., "user" + "action").

Create a script that flags lines containing suspicious keywords.

Build a simple menu-based CLI (text menu with numbered options).

Convert timestamps in logs to a different format.

Write a script that detects duplicate entries in a file.

Sort log entries by timestamp.

Build a simple hash calculator (MD5/SHA256) for files.

Compare two files and show which lines are different.

Convert a list of dictionaries (e.g., user accounts) back into CSV.

Validate IPv4 addresses using regex.

Identify failed login attempts in an auth log file.

Extract unique domains from a list of URLs.


#### PHASE 2 — FILES, NETWORK BASICS & AUTOMATION (Days 21–40)

Parse Apache/Nginx logs and count HTTP status codes.

Build a script that pings a host and prints whether it's up.

Write a port-check script using socket (single port).

Extend it to check a list of ports.

Build a simple directory watcher (check for new/removed files).

Scan a folder and list the largest N files.

Detect files with double extensions (e.g., "invoice.pdf.exe").

Extract URLs from a PDF (using a library).

Build a function to normalize URLs (strip tracking params).

Parse a PCAP summary file (not raw packets) for IP/port pairs.

Generate a random password generator script.

Build a script that monitors CPU/memory usage.

Check if a list of hosts is reachable (multi-ping).

Write a script that counts how many times each user logs in (from logs).

Simulate a login system (dictionary of users/passwords).

Create a script that rotates logs (archive older ones).

Build a script that extracts EXIF metadata from an image.

Normalize email addresses (lowercase, trim, remove dots for Gmail).

Detect whether a file is base64 encoded.

Decode all base64 strings found in a text.


#### PHASE 3 — PRACTICAL SECURITY SCRIPTS (Days 41–60)

Scan for weak passwords in a user list (dictionary attack).

Read Windows Event Logs exported to XML and summarize Event IDs.

Parse Okta logs exported to JSON and count MFA failures.

Detect long-running processes (> X seconds) on Linux using /proc.

Build a script that lists active network connections (psutil).

Read a folder of Sysmon logs and count process creations.

Write a script that extracts strings from a file (ASCII only).

Identify suspicious processes by name (blacklist).

Detect unauthorized new local users from a CSV snapshot.

Convert CSV user data into a structured inventory JSON.

Compare two inventories and list added/removed devices.

Extract domains from browsing history export (e.g., Chrome JSON).

Create a script that checks if domains use HTTPS.

Create a blacklist-checker for URLs/IPs (simple JSON file).

Analyze a Linux auth log for brute-force attempts.

Convert long logs into summaries grouped by user.

Build a script that checks file permissions on Linux paths.

Detect files with high entropy (possible encrypted/malicious).

Count how many connections each IP makes (from a log).

Simple correlation: link IP + user + event type across 2 logs.


#### PHASE 4 — BEGINNER AUTOMATION & APIs (Days 61–80)

Use a free IP geolocation API to enrich a list of IPs.

Query the HaveIBeenPwned password API (no hash upload needed).

Build a script that fetches RSS threat feeds.

Merge multiple feeds into a single JSON file.

Sort threat intel indicators by timestamp.

Build a CLI with argparse subcommands (analyze, clean, search).

Write a script that checks certificate expiration for a domain.

Build a small caching system for API lookups.

Create a script that exports data to Excel (openpyxl).

Build a small Flask API that just returns "healthy" (health check).

Extend the API to accept POSTed JSON and store it.

Build a script that emails yourself a report (SMTP).

Parse Jira tickets exported to CSV.

Generate a simple HTML report from a JSON dataset.

Monitor a folder and upload files to an API when added.

Query Shodan (mocked — use a static JSON example).

Build a URL screenshot tool (Selenium or an API).

Create an IP allow/deny filter script.

Write a basic IOC validator (is this a valid hash, IP, URL?).

Build a file quarantine script (move suspicious files to a folder).


#### PHASE 5 — CAPSTONE-LEVEL BUT STILL ACCESSIBLE (Days 81–100)

Build a small log search tool (keyword + timestamp filtering).

Build a script that detects repeated login failures across days.

Create a JSON report of all findings with counts and summaries.

Build a script that tags log entries by severity.

Write a small rule engine (if IP in blacklist → mark event).

Build a script that merges 3 types of logs into a unified format.

Create a small “playbook runner” that executes tasks via functions.

Build a script that scans a folder for malware-like patterns.

Make a simple timeline tool (sort events by timestamp).

Create a script that highlights anomalies (rare users/IPs).

Write a small REST API that returns filtered log data.

Build a simple web dashboard (Flask + HTML table, very basic).

Add pagination/filtering to the dashboard.

Add a small SQLite DB and store log entries.

Add search and sorting directly from the database.

Add an API endpoint that returns statistics.

Export everything as a CSV/JSON report.

Add a simple configuration file to control behavior.

Package the project as a CLI tool with setup.py.

#### Final capstone: Build a Mini Security Log Analyzer

Upload log file

Parse

Extract IPs/users/events

Summaries + anomalies

Produce report
