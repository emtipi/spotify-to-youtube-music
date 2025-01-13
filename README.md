
# 🎵 Spotify to YouTube Music - Liked Songs Migrator 🎵

Este script transfiere automáticamente tus canciones que te gustan de **Spotify** a la lista de **"Me gusta"** de **YouTube Music**. Sin necesidad de crear playlists manualmente, tus canciones se añaden directamente a tu biblioteca.

## 🚀 Instalación

### 1. **Clonar el repositorio**

```bash
git clone https://github.com/emtipi/spotify-to-youtube-music.git
cd spotify-to-youtube-music
```

### 2. **Instalar dependencias**

Asegúrate de tener **Python 3.8+** y luego instala las librerías necesarias:

```bash
pip install -r requirements.txt
```

📦 **Dependencias principales:**

- `spotipy` → Para acceder a la API de Spotify  
- `ytmusicapi` → Para interactuar con YouTube Music  
- `python-dotenv` → Para gestionar variables de entorno  

### 3. **Configurar las claves de Spotify**

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
```

🔑 **¿Cómo obtener estas claves?**

1. Ve a [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).  
2. Crea una aplicación.  
3. Copia el **Client ID** y **Client Secret**.  
4. Agrega el **Redirect URI**: `http://localhost:8888/callback`.

### 4. **Generar el archivo de autenticación de YouTube Music**

Abre la terminal y ejecuta el script. Si es la primera vez, te pedirá las cabeceras de YouTube Music:

```bash
python main.py
```

📥 **¿Cómo obtener las cabeceras?**

1. Abre [YouTube Music](https://music.youtube.com) en tu navegador Firefox.  
2. Presiona **F12** → Pestaña **Network**.  
3. Busca la solicitud **`browse`**.  
4. Copia cabeceras de solicitud.

⚠ **Nota:** Estos datos son privados, **no los compartas**.

## ▶️ **Uso**

```bash
python main.py
```

## 📂 **Estructura del Proyecto**

```
spotify-to-youtube-music/
├── main.py               # Script principal
├── requirements.txt      # Dependencias del proyecto
├── .env                  # Claves de Spotify
├── browser.json          # Autenticación de YouTube Music
```



## 📜 **Licencia**

Distribuido bajo la licencia **MIT**. Consulta `LICENSE` para más información.

## 💻 **Autor**

Creado por **EmTiPi**
