import json
from pathlib import Path

def update_port(transmission_settings_file, new_port):
    file_path = Path(transmission_settings_file)
    if not file_path.is_file():
        print(f"Transmission settings file not found at {transmission_settings_file}")
        return

    with open(transmission_settings_file, 'r+') as file:
        data = json.load(file)
        current_port = data.get("peer-port")

        if current_port != new_port:
            print(f"Updating Transmission peer-port from {current_port} to {new_port}.")
            data["peer-port"] = new_port
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        else:
            print("Port has not changed. No update needed.")
