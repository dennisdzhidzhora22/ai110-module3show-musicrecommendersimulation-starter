from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Parse a CSV file of songs into a list of dicts with typed fields.
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"].lower(),
                "artist":       row["artist"].lower(),
                "genre":        row["genre"].lower(),
                "mood":         row["mood"].lower(),
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict, tempo_min: float = 60.0, tempo_max: float = 152.0) -> Tuple[float, List[str]]:
    """Score a single song against user preferences, returning the total score and a list of per-feature reasons."""
    score = 0.0
    reasons = []

    # Categorical: genre match (+2.0)
    if song["genre"] in user_prefs.get("genre", set()):
        score += 2.0
        reasons.append(f"genre match (+2.0)")

    # Categorical: mood match (+1.0)
    if song["mood"] in user_prefs.get("mood", set()):
        score += 1.0
        reasons.append(f"mood match (+1.0)")

    # Numeric features: weight × (1 - |song_value - user_pref|)
    numeric_features = [
        ("energy",       2.0),
        ("danceability", 1.5),
        ("valence",      1.5),
        ("acousticness", 1.5),
    ]
    for feature, weight in numeric_features:
        song_val = song.get(feature, 0.0)
        user_val = user_prefs.get(feature, 0.0)
        contribution = weight * (1 - abs(song_val - user_val))
        score += contribution
        reasons.append(f"{feature} score ({contribution:+.2f})")

    # Tempo: normalize to [0, 1] before scoring
    tempo_range = tempo_max - tempo_min
    song_tempo_norm = (song.get("tempo_bpm", tempo_min) - tempo_min) / tempo_range
    user_tempo_norm = (user_prefs.get("tempo_bpm", tempo_min) - tempo_min) / tempo_range
    tempo_contribution = 0.5 * (1 - abs(song_tempo_norm - user_tempo_norm))
    score += tempo_contribution
    reasons.append(f"tempo score ({tempo_contribution:+.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Score all songs against user preferences and return the top k by score.
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    tempo_min = min(s["tempo_bpm"] for s in songs)
    tempo_max = max(s["tempo_bpm"] for s in songs)

    scored = [
        (song, score, "\n".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song, tempo_min, tempo_max)]
    ]

    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
