# Create Music Based on Trends - Tableau Dashboard

                🔽 START TO ANALIZE NOW 🔽
                    How does it work?

Select your chosen country in the filter below. Watch out for trends!
Filter your data based on BPM, Key Note, Popularity, Genres and Related Artists.
---

## **Suggested Structure:**

### :raising_hand: **Trends By Country**
### :baby: **Beta Version. First Version from this database music dashboard.**

### :running: **One-liner**
Construction of a dashboard analyzing data from the top songs from 50 countries on Spotify (weekly updateded). This could be helpful engaing new audience and personalize music  based on data trends by country.

### :computer: **Technology stack**
In summary, the software's primary programming language is Python. The main libraries used are spotipy, pandas, csv, datetime, time, and re. The software appears to be intended as a standalone application or script to interact with the Spotify Web API and possibly perform data analysis on the retrieved data using pandas.

### :boom: **Core technical concepts and inspiration**
Welcome to the "Create Your Music Based on Facts" Tableau Dashboard! This project is all about exploring and analyzing data from the top songs in 50 different countries on Spotify, providing you with valuable insights and trends in global music preferences. Whether you're a music enthusiast, a data analyst, or simply curious about music from around the world, this dashboard is designed to captivate and engage you.
How to Use the Dashboard

    Choose Your Country: Begin by selecting your chosen country from the filter provided. The dashboard will dynamically update to display the relevant data for your selected country.

    Explore Music Trends: Once you've selected a country, you can explore various music trends. Use the available filters to dive into specific aspects of the songs, such as Beats Per Minute (BPM), Key Note, Popularity, Genres, and Related Artists.

    Stay Updated: The data in this dashboard is regularly updated on a weekly basis, allowing you to keep track of evolving music trends from different countries over time.

### :wrench: **Configuration**
The provided code is a Python script that interacts with the Spotify Web API to retrieve music information and perform data analysis on the retrieved data using the spotipy and pandas libraries. Here's a summary of the key components and steps:

    Libraries Used:
        spotipy: A Python library for the Spotify Web API interaction.
        SpotifyClientCredentials: A class from spotipy used for authenticating with the Spotify Web API.
        pandas: A powerful data manipulation and analysis library for Python.
        csv: A built-in Python library for working with CSV files.
        datetime: A built-in Python library for manipulating dates and times.
        time: A built-in Python library for various time-related functions.
        re: A built-in Python library for working with regular expressions.

    Configuration and Requirements:
        The script requires Python to be installed on the system.
        The spotipy library must be installed using pip.
        Spotify API credentials (Client ID and Client Secret) are necessary to authenticate with the Spotify Web API.
        API credentials are stored securely in a config.ini file, which is created in the same directory as the script.
        The config.ini file format includes sections for Spotify credentials.

    Usage:
        Users need to install Python and spotipy library (if not already installed).
        Create a Spotify Developer account and obtain API credentials (Client ID and Client Secret).
        Save the credentials in the config.ini file.
        Run the Python script, which uses spotipy to interact with the Spotify Web API, retrieves music data, and performs data analysis using pandas.

Overall, the script serves as a standalone application for fetching and analyzing music data from Spotify, providing users with insights and analytics based on the retrieved information.

### :file_folder: **Folder structure**
```
C:.
│   .gitignore
│   README.md
│
├───.ipynb_checkpoints
├───data
│       artists_relatedcleanok2.csv
│       data.csv
│       MusiScraper_2023_07_15_21_34_28.csv
│
├───notebooks
│   │   .cache
│   │   .cache-bruni fv
│   │   .cache-brunifv
│   │   config.ini
│   │   feature
│   │   galvanized-yeti-392822-af9b0ee2e65f.json
│   │   RelatedArtists.ipynb
│   │   song_artist
│   │   spotify_related_artists.py
│   │   TopSpotiScraper.ipynb
│   │
│   └───.ipynb_checkpoints
│           RelatedArtists-checkpoint.ipynb
│           TopSpotiScraper-checkpoint.ipynb
│
└───wip
        spotify-recommendation-engine.ipynb

(projectofinal) PS C:\Users\bfven\ironhack\Projectofinal>
```

> Do not forget to include `__trash__` and `.env` in `.gitignore` 

### :shit: **ToDo**
Data Collection Enhancement: Enhance data collection capabilities to retrieve a more comprehensive dataset from the Spotify API. Consider fetching user-specific data, audio features, and other relevant information that could be useful for building a robust recommendation system.

    Data Preprocessing: Implement data preprocessing techniques to handle missing values, outliers, and data normalization. Clean the data and prepare it for training machine learning models.

    Machine Learning Model Selection: Research and explore different machine learning algorithms suitable for music recommendation systems, such as collaborative filtering, content-based filtering, or hybrid approaches.

    Model Training and Evaluation: Train the selected machine learning models using the preprocessed data. Evaluate the models using appropriate metrics to ensure they provide accurate and relevant recommendations.

    User Interface Development: Create a user-friendly interface to interact with the recommendation system. Allow users to input preferences, view recommended tracks, and explore music based on various criteria.

    Personalization: Implement personalized recommendation functionality, considering each user's listening history, preferences, and behavior to provide tailored music suggestions.

    Integration with Spotify API: Integrate the machine learning-based recommendation system with the Spotify API to access real-time data and enable seamless playback of recommended tracks within the application.

    Performance Optimization: Optimize the recommendation system's performance to handle a large number of users and deliver quick and accurate recommendations.

Features Planned:

    Personalized Recommendations: Provide users with personalized music suggestions based on their listening habits and preferences.
    Playlist Generation: Allow users to generate playlists automatically based on their favorite tracks and genres.
    Popular Music Trends: Display trending and popular tracks in real-time.
    Similar Artists/Tracks: Suggest similar artists or tracks based on a user's favorite selections.
    Music Exploration: Offer users the ability to explore new music genres and discover hidden gems.

Known Bugs (Shortlist):

    Time Complexity: The current data retrieval and preprocessing processes might take longer for a large dataset, leading to slower response times. Optimize these processes to improve system efficiency.

    Overfitting: Machine learning models might suffer from overfitting, causing less diverse and relevant recommendations. Implement regularization techniques to mitigate this issue.

    Cold Start Problem: The system might face challenges in recommending music for new users with limited listening history. Explore methods to handle the cold start problem effectively.

    API Rate Limiting: The Spotify API imposes rate limits on the number of requests, leading to potential API call failures. Implement error handling and rate-limiting strategies to prevent disruptions.

    User Diversity: Ensure that the recommendations cater to a diverse user base, considering different music tastes and preferences.

Remember to continuously test and iterate on the system to enhance its performance, accuracy, and user experience throughout its development.


### :love_letter: **Contact info**:

    Name: Bruna Venturini
    Email: brunafventurini@gmail.com
    GitHub: https://github.com/Brunaventurini
---
