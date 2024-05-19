import os
from pyuac import main_requires_admin

def set_dns(server_1=None, server_2=None):
    """
    Set DNS servers for the Wi-Fi interface. If no servers are provided,
    set the source to DHCP (i.e., automatic DNS).
    """
    try:
        if server_1 is None and server_2 is None:
            os.system('netsh interface ip set dnsservers name="Wi-Fi" source=dhcp')
        else:
            os.system(f'netsh interface ip set dns name="Wi-Fi" static {server_1}')
            os.system(f'netsh interface ip add dns name="Wi-Fi" {server_2} index=2')
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

@main_requires_admin
def main():
    while True:
        print("1: Activate Shecan\n2: Deactivate Shecan\n0: Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            if set_dns('185.51.200.2', '178.22.122.100'):
                print("Shecan has been activated.\n")
            else:
                print("Failed to activate Shecan.\n")
        
        elif choice == '2':
            if set_dns():
                print("Shecan has been deactivated.\n")
            else:
                print("Failed to deactivate Shecan.\n")
        
        elif choice == '0':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()
