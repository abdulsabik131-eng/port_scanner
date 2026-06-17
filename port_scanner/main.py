import sys
from validation import get_inputs, validate_target, parse_ports
from scanner import scan_ports
from service_detection import get_service_name
from report import print_report

def main():
    try:
        # Step 1: Get inputs & validate them
        target, port_range = get_inputs()
        target_ip = validate_target(target)
        port_list = parse_ports(port_range)
        
        # Step 2: Scan the ports
        open_ports = scan_ports(target_ip, port_list)
        
        # Step 3: Map open ports to their service names
        results = {}
        for port in open_ports:
            service = get_service_name(port)
            results[port] = service
            
        # Step 4: Display the report
        print_report(target_ip, results)

    except KeyboardInterrupt:
        print("\n[-] Exiting program...")
        sys.exit()

if __name__ == "__main__":
    main()