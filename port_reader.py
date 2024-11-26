import json
from pathlib import Path

def read_port(gluetun_port_file):
    file_path = Path(gluetun_port_file)
    if file_path.is_file():
        with open(gluetun_port_file, 'r') as file:
            data = json.load(file)
            open_port = data.get('port')
            if open_port:
                return open_port
            else:
                print("Failed to extract port from JSON.")
                return None
    else:
        print(f"Gluetun port file not found at {gluetun_port_file}")
        return None
