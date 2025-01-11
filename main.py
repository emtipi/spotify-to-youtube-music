import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic, setup

load_dotenv()

# ----------------- CONFIGURACIÓN -----------------
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Archivo de autenticación de YouTube Music
YT_HEADERS_FILE = 'browser.json'

# -------------------------------------------------

# Autenticación con Spotify
def spotify_auth():
    scope = "user-library-read"
    sp_oauth = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=scope
    )
    return Spotify(auth_manager=sp_oauth)

# Autenticación con YouTube Music
def youtube_auth():
    if not os.path.exists(YT_HEADERS_FILE):
        print("❗ No se encontró el archivo 'browser.json'.")
        print("📥 Pega las cabeceras HTTP de YouTube Music y presiona Enter dos veces:\n")

        headers_raw = ""
        while True:
            try:
                linea = input()
                if linea == "":
                    break
                headers_raw += linea + "\n"
            except KeyboardInterrupt:
                break

        setup(filepath=YT_HEADERS_FILE, headers_raw=headers_raw)
        print("✅ Archivo 'browser.json' generado correctamente.")

    else:
        print("✅ Se encontró 'browser.json'. Usando para autenticación.")

    return YTMusic(YT_HEADERS_FILE)

# Obtener canciones que te gustan en Spotify
def get_spotify_liked_tracks(sp):
    liked_tracks = []
    results = sp.current_user_saved_tracks(limit=50)

    while results:
        for item in results['items']:
            track = item['track']
            song = f"{track['name']} {track['artists'][0]['name']}"
            liked_tracks.append(song)
            print(f"🎵 Encontrada en Spotify: {song}")

        if results['next']:
            results = sp.next(results)
        else:
            results = None
    return liked_tracks

# Añadir canciones directamente a la lista de "Me gusta" de YouTube Music
def add_to_liked_songs(ytmusic, songs):
    for song in songs:
        search_results = ytmusic.search(song, filter='songs')
        if search_results:
            video_id = search_results[0].get('videoId')
            if video_id:
                # Marcar la canción como "Me gusta"
                ytmusic.rate_song(video_id, "LIKE")
                print(f"👍 Añadido a 'Me gusta' en YouTube Music: {song}")
            else:
                print(f"⚠️ No se encontró videoId para: {song}")
        else:
            print(f"❌ No encontrado en YouTube Music: {song}")

# ------------------ EJECUCIÓN ------------------
def main():
    sp = spotify_auth()
    ytmusic = youtube_auth()

    print("\n🔎 Obteniendo canciones que te gustan en Spotify...")
    liked_songs = get_spotify_liked_tracks(sp)

    print("\n👍 Añadiendo canciones a 'Me gusta' en YouTube Music...")
    add_to_liked_songs(ytmusic, liked_songs)

if __name__ == "__main__":
    main()
