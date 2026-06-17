# ⚽ FIFA World Cup 2026 Interactive Dashboard

A premium, highly interactive soccer dashboard built with **Python Flask** and **Vanilla HTML, CSS, and JavaScript** that fetches, parses, structures, and displays real-time tournament fixtures and standings for the **FIFA World Cup 2026**. It also captures live soccer news from ESPN and features a custom multi-channel social media scorecard sharing wizard.

---

## 🚀 Key Features

*   **104-Match Fixtures Feed**: Displays all group stage and knockout matches from the official openfootball dataset, complete with scores, venues, round stages, and key match events (goalscorers and minutes).
*   **Dynamic Group Standings Widget**: Automatically calculates group standings (Position, Played, Wins, Draws, Losses, Goal Difference, and Points) in real-time from match outcomes for all 12 groups (A through L) with a dropdown switcher.
*   **Circular Flag Badges**: Dynamic mapping of team names to ISO codes to fetch country flags from FlagCDN, rendered as elegant circular badges.
*   **ESPN News Sidebar**: Live server-side parsing of ESPN Soccer RSS feed, displaying recent articles with publishing timestamps.
*   **Stadium Lights Theme System**: Seamless toggling between **Dark Emerald Night** (stadium floodlights aesthetic) and **Light Mint Grass** themes. Preserved in `localStorage`.
*   **Granular Search & Filters**: Search matches in real-time by country name, stadium, or stage, and filter matches by completed/scheduled status or group.
*   **Multi-Channel Social Sharing Modal**: Select one or more matches to build a scoreboard card. Share directly to **X (Twitter)**, **Telegram**, or **LinkedIn** with character limits tracked dynamically via an SVG progress circle.
*   **Data Export (CSV)**: Export the currently filtered matches feed into a structured CSV file with a single click.

---

## 📁 Project Structure

```text
├── app.py                  # Flask application (caching, openfootball API, ESPN RSS parser)
├── requirements.txt        # Python backend dependencies (Flask, etc.)
├── test_feed.py            # Diagnostic script to test feed connections
├── templates/
│   └── index.html          # HTML structure with news sidebar and group standings
├── static/
│   ├── css/
│   │   └── style.css       # Deep emerald night and mint grass stylesheets
│   └── js/
│       └── app.js          # Client-side state manager, standings calculator, and social composer
├── scratch_worldcup.json   # Local copy of openfootball tournament matches
└── README.md               # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone & Navigate
Clone this repository and navigate to the root directory:
```bash
cd agy-cli-projects
```

### 2. Install Dependencies
Install Flask and other backend requirements:
```bash
python3 -m pip install -r requirements.txt
```

### 3. Start the Server
Run the Flask server:
```bash
python3 app.py
```
By default, the server will start in debug mode on:
👉 **[http://127.0.0.1:5001/](http://127.0.0.1:5001/)** 
*(Note: Port 5001 is used to prevent port conflicts with macOS AirPlay Receiver on port 5000).*

---

## 📝 How to Use the App

1.  **Toggle Theme**: Click the **Sun/Moon icon** in the header. The layout switches between the Dark Emerald and Light Mint themes.
2.  **Filter & Search**:
    *   Type keywords (e.g., `"Mexico"`, `"Atlanta"`) in the search bar.
    *   Click **Completed** or **Scheduled** to view played results versus upcoming matches.
    *   Select a group (e.g., *"Group B"*) from the Group dropdown to filter fixtures.
3.  **View Standings**: Scroll to the widget under the news sidebar. Select a group from the dropdown; the table recalculates the position, goal difference, and points for that group.
4.  **Export CSV**: Click **Export CSV** in the header to download a spreadsheet of the matches matching your current filters.
5.  **Share Scorecard**:
    *   Click **Share** on any match card to open the composer.
    *   Alternatively, click multiple match cards to select them, and click **Share Scorecard** in the floating bottom bar.
    *   Choose to **Post to X**, share to **Telegram**, **LinkedIn**, or **Copy Text** to your clipboard.

---

## 🛡️ License

This project is open-source and available under the MIT License.
