import time
import json
from port_reader import read_port
from port_updater import update_port

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    gluetun_port_file = config.get("gluetun_port_file")
    transmission_settings_file = config.get("transmission_settings_file")
    update_interval = config.get("update_interval", 3600)

def main():
    while True:
        open_port = read_port(gluetun_port_file)
        if open_port:
            update_port(transmission_settings_file, open_port)
        print(f"Waiting for {update_interval} seconds before checking for updates...")
        time.sleep(update_interval)

if __name__ == "__main__":
    main()
