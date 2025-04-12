import json
import csv
import os


def ensure_dir_exists(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)


def save_to_json(data, filename):
    try:
        ensure_dir_exists(filename)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"[+] Saved to {filename}")
    except IOError as e:
        print(f"[!] Failed to save JSON: {e}")


def save_to_csv(data, filename):
    try:
        ensure_dir_exists(filename)
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"[+] Saved to {filename}")
    except Exception as e:
        print(f"[!] Failed to save CSV: {e}")


def load_from_json(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError("File does not exist.")
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error loading JSON: {e}")
        return []
