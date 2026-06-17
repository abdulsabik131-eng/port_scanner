def print_report(target, scan_results):
    """Prints results in a clean format."""
    print("\n" + "="*40)
    print(f" SCAN REPORT FOR: {target}")
    print("="*40)
    
    if not scan_results:
        print("No open ports found.")
        print("="*40)
        return

    print("PORT\tSTATE\tSERVICE")
    print("-"*40)
    
    # scan_results will be a dictionary like {22: 'SSH', 80: 'HTTP'}
    for port, service in scan_results.items():
        print(f"{port}\tOPEN\t{service}")
        
    print("="*40 + "\n")