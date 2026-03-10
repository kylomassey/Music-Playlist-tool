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
    
def dict_to_song(data):
    from models import Song
    new_song = Song(name= data["name"], artist= data["artist"],
                    album= data["album"], year= data["year"],
                    bpm= data["bpm"], genre= data["genre"], rating= data["rating"],
                    minutes= data["minutes"], seconds= data["seconds"])
    return new_song

def to_json(data, filename= "data"):
    with open(f"{filename}.json", "w") as f:
        json.dump(data, f)

def json_to_data(filename= "data"):
    with open(f"{filename}.json", "r") as f:
        data = json.load(f)
    return data