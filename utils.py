import json

def format_duration(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"

def validate_str (value, name):
    if value is not None and not isinstance(value, str):
        raise TypeError(f"{name} must be a string or None")
    
def validate_number (value, name):
    if value is not None and not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number or None")
    
def to_json(data, filename= "data.json"):
    with open(f"{filename}", "w", encoding= "utf-8") as f:
        json.dump(data, f)

def json_to_data(filename= "data.json"):
    try:
        with open(f"{filename}", "r", encoding= "utf-8") as f:
            data = json.load(f)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{filename} does not exist") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in file: {filename}") from exc
    
    return data