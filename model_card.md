# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

**NextSongFinder 1.o**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

The system recommends songs based on a user's given preferences for features like genre, mood, and audio characteristics like tempo and energy. It assumes this data is given upfront, and it cannot learn from listening history. In the current form, it's a classroom simulation.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Each song in the catalog is given a score out of 10 by comparing it to the user's preferences. Genre and mood are checked for exact matches, awarding flat scores. For the audio features used, which are energy, danceability, valence, acousticness, and tempo, the closer a song's value is to what the user prefers, the higher the score for that feature. Tempo is first normalized to be on a 0-1 range like the other features before scoring. Feature scores are then added up, and the top k ranking songs are returned.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains 20 songs. Genres included are pop, rock, lofi, ambient, jazz, classical, metal, synthwave, indie pop, hip-hop, r&b, folk, electronic, blues, country, reggae, and soul. Moods cover happy, chill, intense, focused, relaxed, moody, energetic, melancholic, aggressive, romantic, nostalgic, euphoric, sad, peaceful, uplifting, and longing. An additional 10 songs were added from the original 10 to bring more genre and mood coverage. Missing from the dataset is info like subgenres and behavioral data like play counts or skips.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users with clear and consistent preferences. Someone who distinctly prefers chill lofi or high energy rock will reliably be recommended songs with similar characteristics. The weighted scoring distinguishes between musically distant profiles well, so a chill lofi listener and an intense rock listener receive almost completely non-overlapping recommendations.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One big limitation of the system is that it's very strict with the genre and mood. If a genre is very closely related but not the exact same as a preferred genre, the given score doesn't consider the similarity, and instead gives a 0. Some features may also not be as relevant as I first thought. For example, Energy and Acousticness are very closely inversely correlated. Getting rid of one would probably not affect recommendations that much.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.



The user profiles I tested were the default one that was already present in the code, one focusing on intense rock and electronic, one focusing on chill lofi, one with contradictions among the feature values, and another representing unknown or less common genres and moods. What surprised me most was probably how accurate the recommendations could be, despite the relatively simple rules for the score. 

The Standard profile prefers higher energy pop music, meanwhile the Intense Rock profile prefers energetic but less happy, more serious music. The Chill Lofi profile in comparison to both prefers slower tempo, less energetic music.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I think the most impactful improvement would be replacing the binary genre/mood matching with some way of measuring similarity that gives partial credit to related genres (e.g. indie pop giving a partial score for a preference of pop). Removing acousticness would reduce redundancy in the feature set. Diversity could be improved by penalizing repeated consecutive recommendations from very similar genre clusters. It would also be nice to build the user preferences from listening history instead of having them be inputted manually.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommender systems rely on multiple different strategies to make recommendations, not just one. Using AI tools helped this time by greatly speeding up the implementation stage of the core functions in the system. Instead of having to write everything out, I could just discuss my approach and confirm that the generated code was logically sound and followed my intended approach. An interesting finding to me was that there are so many different ways to describe audio qualities other than what I knew, like valence and acousticness, and that's not even all there could be. Working on this project has made me want to pay closer attention to how the music I listen to can change the recommendations I receive in the apps I use.
