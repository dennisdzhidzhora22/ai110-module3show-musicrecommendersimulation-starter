"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    intense_rock = {"genre": set(["rock", "electronic"]), "mood": set(["intense", "energetic"]),
                    "energy": 0.83, "tempo_bpm": 130, "valence": 0.5,
                    "danceability": 0.7, "acousticness": 0.4}
    
    chill_lofi = {"genre": set(["lofi", "ambient"]), "mood": set(["chill"]),
                  "energy": 0.37, "tempo_bpm": 80, "valence": 0.55,
                  "danceability": 0.45, "acousticness": 0.79}

    # Edge case: contradictory features — high energy but also high acousticness and slow tempo.
    # These are strongly anti-correlated in the dataset, so no song should satisfy all three.
    # Reveals how the weighted sum handles irreconcilable preferences.
    contradictory = {"genre": set(["folk", "metal"]), "mood": set(["peaceful", "aggressive"]),
                     "energy": 0.95, "tempo_bpm": 65, "valence": 0.5,
                     "danceability": 0.5, "acousticness": 0.90}

    # Edge case: genre and mood not present in the dataset at all.
    # The user earns 0 categorical bonus points — ranking falls back entirely on numeric similarity.
    # Tests whether the recommender degrades gracefully with no genre/mood matches.
    unknown_taste = {"genre": set(["bossa nova", "k-pop"]), "mood": set(["triumphant"]),
                     "energy": 0.70, "tempo_bpm": 110, "valence": 0.75,
                     "danceability": 0.80, "acousticness": 0.25}

    profiles = [
        ("Starter",      user_prefs),
        ("Intense Rock", intense_rock),
        ("Chill Lofi",   chill_lofi),
        ("Contradictory",  contradictory),
        ("Unknown Taste",  unknown_taste),
    ]

    for label, prefs in profiles:
        recommendations = recommend_songs(prefs, songs, k=5)
        print(f"\n{'='*40}")
        print(f"  [{label}] Top {len(recommendations)} Recommendations")
        print(f"{'='*40}\n")
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"#{i}  {song['title'].title()} by {song['artist'].title()}")
            print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Score: {score:.2f}/10")
            print(f"    Breakdown:")
            for reason in explanation.split("\n"):
                print(f"      - {reason}")
            print()


if __name__ == "__main__":
    main()
