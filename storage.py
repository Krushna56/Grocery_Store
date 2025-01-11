import json
from pathlib import Path
from datetime import datetime

class JsonStorage:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._load_data()
    
    def _load_data(self):
        if Path(self.filename).exists():
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {'products': [], 'sales': [], 'last_id': 0}
    
    def _save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_next_id(self):
        self.data['last_id'] += 1
        self._save_data()
        return self.data['last_id']