import urllib.request
import xml.etree.ElementTree as ET
import json
import sys
import ssl

WORLDCUP_FEED_URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"
NEWS_FEED_URL = "https://www.espn.com/espn/rss/soccer/news"

def test_feeds():
    context = ssl._create_unverified_context()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

    # 1. Test World Cup Feed
    try:
        print("Testing FIFA World Cup 2026 JSON Feed...")
        req = urllib.request.Request(WORLDCUP_FEED_URL, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=context) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        matches = data.get("matches", [])
        print(f"✓ World Cup Feed OK. Loaded {len(matches)} matches.")
        if matches:
            first = matches[0]
            print(f"  First match: {first.get('date')} - {first.get('team1')} vs {first.get('team2')} ({first.get('group', 'Playoffs')})")
    except Exception as e:
        print(f"✗ World Cup Feed FAILED: {e}")
        sys.exit(1)

    # 2. Test ESPN News Feed
    try:
        print("\nTesting ESPN Soccer RSS News Feed...")
        req = urllib.request.Request(NEWS_FEED_URL, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=context) as response:
            xml_data = response.read()
        
        root = ET.fromstring(xml_data)
        channel = root.find('channel')
        items = channel.findall('item') if channel is not None else []
        print(f"✓ ESPN News Feed OK. Parsed {len(items)} headlines.")
        if items:
            first_title = items[0].find('title')
            title_text = first_title.text if first_title is not None else "No Title"
            print(f"  Latest news title: '{title_text}'")
    except Exception as e:
        print(f"✗ ESPN News Feed FAILED: {e}")
        sys.exit(1)

    print("\nAll feed checks passed successfully!")

if __name__ == "__main__":
    test_feeds()
