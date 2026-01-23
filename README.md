### **100+ Python Challenges**

####This repository has been created as a way to document my progess in my quest to learn python. Challenges have been created (with the help of AI) with a focus on cyber security related tasks, with the overall challenge divided into 5 different phases, as follows:

**PHASE 1 — FOUNDATIONS WITH PURPOSE (Days 1–20)**

1. Write a script that reads a text file and prints the number of lines.
   
2. Count how many times each word appears in a file (simple frequency counter).
   
3. Extract all IP addresses from a text file using regex.
   
4. Extract all email addresses from text.
   
5. Identify the top 5 most common IPs in a log file.
   
6. Write a function that checks if a password meets complexity rules.
   
7. Build a simple "log cleaner" that removes empty lines \& comments.
   
8. Convert a CSV of users into a list of dictionaries.
   
9. Read JSON logs and print specific fields (e.g., "user" + "action").
   
10. Create a script that flags lines containing suspicious keywords.
    
11. Build a simple menu-based CLI (text menu with numbered options).
    
12. Convert timestamps in logs to a different format.
    
13. Write a script that detects duplicate entries in a file.
    
14. Sort log entries by timestamp.
    
15. Build a simple hash calculator (MD5/SHA256) for files.
    
16. Compare two files and show which lines are different.
    
17. Convert a list of dictionaries (e.g., user accounts) back into CSV.
    
18. Validate IPv4 addresses using regex.
    
19. Identify failed login attempts in an auth log file.
    
20. Extract unique domains from a list of URLs.


    **PHASE 2 — FILES, NETWORK BASICS \& AUTOMATION (Days 21–40)**
    
21. Parse Apache/Nginx logs and count HTTP status codes.
    
22. Build a script that pings a host and prints whether it's up.
    
23. Write a port-check script using socket (single port).
    
24. Extend it to check a list of ports.
    
25. Build a simple directory watcher (check for new/removed files).
    
26. Scan a folder and list the largest N files.
    
27. Detect files with double extensions (e.g., "invoice.pdf.exe").
    
28. Extract URLs from a PDF (using a library).
    
29. Build a function to normalize URLs (strip tracking params).
    
30. Parse a PCAP summary file (not raw packets) for IP/port pairs.
    
31. Generate a random password generator script.
    
32. Build a script that monitors CPU/memory usage.
    
33. Check if a list of hosts is reachable (multi-ping).
    
34. Write a script that counts how many times each user logs in (from logs).
    
35. Simulate a login system (dictionary of users/passwords).
    
36. Create a script that rotates logs (archive older ones).
    
37. Build a script that extracts EXIF metadata from an image.
    
38. Normalize email addresses (lowercase, trim, remove dots for Gmail).
    
39. Detect whether a file is base64 encoded.
    
40. Decode all base64 strings found in a text.


    **PHASE 3 — PRACTICAL SECURITY SCRIPTS (Days 41–60)**
    
41. Scan for weak passwords in a user list (dictionary attack).
    
42. Read Windows Event Logs exported to XML and summarize Event IDs.
    
43. Parse Okta logs exported to JSON and count MFA failures.
    
44. Detect long-running processes (> X seconds) on Linux using /proc.
    
45. Build a script that lists active network connections (psutil).
    
46. Read a folder of Sysmon logs and count process creations.
    
47. Write a script that extracts strings from a file (ASCII only).
    
48. Identify suspicious processes by name (blacklist).
    
49. Detect unauthorized new local users from a CSV snapshot.
    
50. Convert CSV user data into a structured inventory JSON.
    
51. Compare two inventories and list added/removed devices.
    
52. Extract domains from browsing history export (e.g., Chrome JSON).
    
53. Create a script that checks if domains use HTTPS.
    
54. Create a blacklist-checker for URLs/IPs (simple JSON file).
    
55. Analyze a Linux auth log for brute-force attempts.
    
56. Convert long logs into summaries grouped by user.
    
57. Build a script that checks file permissions on Linux paths.
    
58. Detect files with high entropy (possible encrypted/malicious).
    
59. Count how many connections each IP makes (from a log).
    
60. Simple correlation: link IP + user + event type across 2 logs.

    **PHASE 4 — BEGINNER AUTOMATION \& APIs (Days 61–80)**
    
61. Use a free IP geolocation API to enrich a list of IPs.
    
62. Query the HaveIBeenPwned password API (no hash upload needed).
    
63. Build a script that fetches RSS threat feeds.
    
64. Merge multiple feeds into a single JSON file.
    
65. Sort threat intel indicators by timestamp.
    
66. Build a CLI with argparse subcommands (analyze, clean, search).
    
67. Write a script that checks certificate expiration for a domain.
    
68. Build a small caching system for API lookups.
    
69. Create a script that exports data to Excel (openpyxl).
    
70. Build a small Flask API that just returns "healthy" (health check).
    
71. Extend the API to accept POSTed JSON and store it.
    
72. Build a script that emails yourself a report (SMTP).
    
73. Parse Jira tickets exported to CSV.
    
74. Generate a simple HTML report from a JSON dataset.
    
75. Monitor a folder and upload files to an API when added.
    
76. Query Shodan (mocked — use a static JSON example).
    
77. Build a URL screenshot tool (Selenium or an API).
    
78. Create an IP allow/deny filter script.
    
79. Write a basic IOC validator (is this a valid hash, IP, URL?).
    
80. Build a file quarantine script (move suspicious files to a folder).


    **PHASE 5 — CAPSTONE-LEVEL BUT STILL ACCESSIBLE (Days 81–100)**
    
81. Build a small log search tool (keyword + timestamp filtering).
    
82. Build a script that detects repeated login failures across days.
    
83. Create a JSON report of all findings with counts and summaries.
    
84. Build a script that tags log entries by severity.
    
85. Write a small rule engine (if IP in blacklist → mark event).
    
86. Build a script that merges 3 types of logs into a unified format.
    
87. Create a small “playbook runner” that executes tasks via functions.
    
88. Build a script that scans a folder for malware-like patterns.
    
89. Make a simple timeline tool (sort events by timestamp).
    
90. Create a script that highlights anomalies (rare users/IPs).
    
91. Write a small REST API that returns filtered log data.
    
92. Build a simple web dashboard (Flask + HTML table, very basic).
    
93. Add pagination/filtering to the dashboard.
    
94. Add a small SQLite DB and store log entries.
    
95. Add search and sorting directly from the database.
    
96. Add an API endpoint that returns statistics.
    
97. Export everything as a CSV/JSON report.
    
98. Add a simple configuration file to control behavior.
    
99. Package the project as a CLI tool with setup.py.

    **Final capstone: Build a Mini Security Log Analyzer**
    
100. Upload log file
     
101. Parse
     
102. Extract IPs/users/events
     
103. Summaries + anomalies
     
104. Produce report
