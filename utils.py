from models import Song

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
    
def dict_to_song(data):
    new_song = Song(name= data["name"], artist= data["artist"],
                    album= data["album"], year= data["year"],
                    bpm= data["bpm"], genre= ["genre"], 
                    minutes= data["minutes"], seconds= data["seconds"])
    return new_song