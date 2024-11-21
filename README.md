# Interactive Spotify

Generate a playlist by choosing a keyword and the number of tracks you want. Simply press "Submit," and enjoy your curated playlist!

## How It Works

Interactive Spotify connects with the Spotify API to create personalized playlists based on your input.

------

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Ollyje/interactivespotify.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd interactivespotify
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your Spotify API Key:**

   - Obtain your Spotify API credentials (Client ID, Client Secret, and Redirect URI) from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

5. **Create a `.txt` File for API Credentials:**

   - Save your credentials in a text file. Ensure the file contains:

     ```
     CLIENT_ID=your_client_id
     CLIENT_SECRET=your_client_secret
     REDIRECT_URI=your_redirect_uri
     ```

   - Ensure this file is listed in `.gitignore` to keep your credentials secure.

6. **Run the Application:**

   

------

## Usage

1. Launch the application.
2. Enter a keyword for your playlist.
3. Choose the number of tracks.
4. Press **Submit** to generate your playlist!

Enjoy discovering new music tailored to your preferences!
