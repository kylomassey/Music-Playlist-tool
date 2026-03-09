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