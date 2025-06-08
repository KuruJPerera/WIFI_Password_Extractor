import os  # Import os module

def get_wifi_passwords():
    """Retrieves saved Wi-Fi passwords from a Windows machine."""
    command = "netsh wlan show profiles"
    profiles = os.popen(command).read()  # Get the list of Wi-Fi profiles
    
    # Extracts the Wi-Fi profile names using splitting feature.
    profile_names = [line.split(':')[1].strip() for line in profiles.split('\n') if "All User Profile" in line]
    
    for profile in profile_names:
        result = os.popen(f"netsh wlan show profile name=\"{profile}\" key=clear").read()  # Get the profile details
        for line in result.split('\n'):
            if "Key Content" in line:
                password = line.split(':')[1].strip()  # Extract password
                print(f"Wi-Fi: {profile}, Password: {password}")

# Run the function
get_wifi_passwords()

