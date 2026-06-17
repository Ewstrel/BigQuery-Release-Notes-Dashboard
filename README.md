# BigQuery Release Notes Dashboard

A premium, interactive web application built with **Python Flask** and **Vanilla HTML, CSS, and JavaScript** that fetches, parses, structures, and displays Google Cloud BigQuery release notes. It features a dynamic theme switcher, search and categorization filters, and direct X/Twitter sharing integrations.

---

## 🚀 Key Features

*   **Live RSS/Atom Parsing**: Server-side script fetches Google's official BigQuery Atom feed and parses XML namespaces dynamically.
*   **Smart Server Caching**: Utilizes a 60-second in-memory cache to maintain quick loading times and respect Google's endpoint rate limits.
*   **Granular Update Splitting**: Frontend DOM parser splits daily entries (which often combine multiple features and issues) into individual, category-coded update cards.
*   **Dynamic Theme Switcher**: Toggle instantly between a sleek **Dark Mode** (default) and a warm **Light Beige Theme**. The selected theme is preserved locally in the browser's `localStorage`.
*   **One-Click Copy**: Copy a formatted, plain-text summary of any update (complete with doc links) directly to your clipboard.
*   **CSV Export**: Download currently searched, filtered, and sorted updates into a standard CSV file with one click.
*   **Real-time Filtering & Search**: Instant client-side search indexing and filter buttons for category sorting (Features, Changes, Issues, Breaking, Announcements).
*   **Interactive Tweet Composer**: Custom modal composer formats updates into tweets, tracks X's 280-character limit, warns the user of overflows, and aggregates multi-selected updates into a single tweet.

---

## 📁 Project Structure

```text
├── app.py                  # Python Flask server & XML parsing backend
├── requirements.txt        # Python backend dependencies
├── templates/
│   └── index.html          # Frontend HTML skeleton
├── static/
│   ├── css/
│   │   └── style.css       # Stylesheets supporting both dark & light themes
│   └── js/
│       └── app.js          # App state, client parsing, theme toggle & CSV export
├── .gitignore              # Git ignore rules (venv, cache, IDE folders)
└── README.md               # Project documentation
```

---

## 🛠️ Installation & Setup

### Prerequisites
Make sure you have **Python 3** and **Node.js** installed on your system.

### 1. Clone & Navigate
Navigate to your project directory:
```bash
cd agy-cli-projects
```

### 2. Install Dependencies
Install the required packages listed in `requirements.txt`:
```bash
python3 -m pip install -r requirements.txt
```

### 3. Start the Flask Server
Run the Flask server:
```bash
python3 app.py
```
By default, the server will start in debug mode on:
👉 **[http://127.0.0.1:5001/](http://127.0.0.1:5001/)** (adjusted to port 5001 to prevent conflicts with macOS AirPlay Receiver on port 5000)

---

## 📝 How to Use the App

1.  **Toggle Theme**: Click the **Sun/Moon icon** in the header actions. The layout will switch between Dark Mode and Light Beige Mode instantly.
2.  **Refresh Feed**: Click **Refresh** in the header. The sync icon will rotate, bypassing the 60-second in-memory cache to fetch live feed updates immediately.
3.  **Export CSV**: Click **Export CSV** in the header. It will download a CSV file containing only the updates that are currently visible (matching your search/filters).
4.  **Filter and Search**:
    *   Type keywords (e.g., `"Gemini"`, `"pricing"`, `"UDF"`) in the search input to filter the feed in real-time.
    *   Click category badges (e.g., *Features*, *Issues*, *Breaking*) to isolate specific update types.
    *   Toggle chronological sorting using the dropdown.
5.  **Copy Update**: Click the **Copy** button in the footer of any card. The text will be formatted and copied to your clipboard, and the button will temporarily display "Copied!".
6.  **Single Tweet**: Click **Tweet** at the bottom-right of any update card. A modal will appear with pre-formatted text containing the category emoji, update description, and link to the official docs.
7.  **Multi-Select Tweet**: 
    *   Click on multiple cards (or their checkboxes) to select them. A floating bar at the bottom will display the selected count.
    *   Click **Tweet Selected**. The modal compiles a summary. If the text exceeds 280 characters, it will intelligently truncate details and append `+ more updates!` to fit within X/Twitter limits.
8.  **Publishing**: Edit the text in the modal if needed, then click **Post to X** to open the official Twitter Web Intent. Alternatively, click **Copy Text** to save it to your clipboard.

---

## 🛡️ License

This project is open-source and available under the MIT License.
