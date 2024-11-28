import time
import json
import sys
from port_reader import read_port
from port_updater import update_port

# Override stdout to always flush
sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

# Load configuration
try:
    with open("./settings/config.json", "r") as config_file:
        config = json.load(config_file)
        gluetun_port_file = config.get("gluetun_port_file")
        transmission_settings_file = config.get("transmission_settings_file")
        update_interval = config.get("update_interval", 3600)
except Exception as e:
    print(f"Error loading configuration: {e}")
    exit(1)

def main():
    while True:
        try:
            open_port = read_port(gluetun_port_file)
            if open_port:
                update_port(transmission_settings_file, open_port)
            print(f"Waiting for {update_interval} seconds before checking for updates...")
            time.sleep(update_interval)
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error starting main function: {e}")
