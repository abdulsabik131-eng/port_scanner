->Features:
  *Modular Architecture: Separated into validation, scanning, service lookup, and reporting modules.
  *Domain Resolution: Automatically converts domain names (like google.com) into IP addresses.
  *Service Detection: Shows the standard protocol running on discovered open ports.
  *Clean UI: Displays a formatted table of results directly in your terminal.

->Project Structure:

   port_scanner/
   │
   ├── main.py               # The main controller that ties everything together
   ├── validation.py         # Handles and validates user inputs (IP/Ports)
   ├── scanner.py            # Core logic for checking open TCP ports
   ├── service_detection.py  # Detects service names for open ports
   └── report.py             # Formats and prints the final scan results

->How to Use:
   *run main.py file 
   *enter domain name (or) ip address
   *then enter port range like (1-1000)
   *this tool provide service name too

-> sample output:
   
Enter Target IP or Domain (e.g: 192.168.1.1 or google.com): google.com
Enter Port Range (e.g: 20-80): 1-500

[*] Scanning 142.250.206.174...

========================================
 SCAN REPORT FOR: 142.250.206.174
========================================
PORT    STATE   SERVICE
----------------------------------------
80      OPEN    HTTP
443     OPEN    HTTPS
========================================
