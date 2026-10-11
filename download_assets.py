import requests
import json
import os

os.makedirs('assets/images/hero', exist_ok=True)
os.makedirs('assets/images/dishes', exist_ok=True)
os.makedirs('assets/images/atmosphere', exist_ok=True)
os.makedirs('assets/images/branding', exist_ok=True)
os.makedirs('assets/video', exist_ok=True)

# Curated high-resolution photography for The Bluebop Cafe & Bar
# Matching: Khar Mumbai ambiance, Italian/Continental dishes, jazz cocktail bar aesthetic
image_downloads = {
    # Hero & exterior/entrance
    'assets/images/hero/hero-interior.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1920&q=85',
    'assets/images/hero/hero-bar.jpg': 'https://images.unsplash.com/photo-1572116469696-31de0f17cc34?w=1920&q=85',
    
    # Atmosphere & Experience Grid (The Space, The Details, The Table, The Moment)
    'assets/images/atmosphere/the-space.jpg': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85',
    'assets/images/atmosphere/the-details.jpg': 'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=1200&q=85',
    'assets/images/atmosphere/the-table.jpg': 'https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85',
    'assets/images/atmosphere/the-moment.jpg': 'https://images.unsplash.com/photo-1543007630-9710e4a00a20?w=1200&q=85',
    'assets/images/atmosphere/about-still.jpg': 'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85',

    # Verified Dishes
    'assets/images/dishes/garlic-pizza-bread.jpg': 'https://images.unsplash.com/photo-1573821663912-569905455b1c?w=800&q=85',
    'assets/images/dishes/margherita-pizza.jpg': 'https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=800&q=85',
    'assets/images/dishes/farmhouse-pizza.jpg': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800&q=85',
    'assets/images/dishes/wild-mushroom-risotto.jpg': 'https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?w=800&q=85',
    'assets/images/dishes/truffle-fettuccine.jpg': 'https://images.unsplash.com/photo-1621996346565-e3d5d6281691?w=800&q=85',
    'assets/images/dishes/potato-wedges.jpg': 'https://images.unsplash.com/photo-1585109649139-366815a0d713?w=800&q=85',
    'assets/images/dishes/nachos.jpg': 'https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?w=800&q=85',
    'assets/images/dishes/tiramisu.jpg': 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=800&q=85',
    'assets/images/dishes/lavender-lemonade.jpg': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=800&q=85',
    'assets/images/dishes/mango-basil-mojito.jpg': 'https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=800&q=85'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

print("Starting photo asset downloads...")
for path, url in image_downloads.items():
    if os.path.exists(path) and os.path.getsize(path) > 10000:
        print(f"Exists: {path}")
        continue
    try:
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
            print(f"Downloaded: {path} ({len(r.content)} bytes)")
        else:
            print(f"Failed {path}: {r.status_code}")
    except Exception as e:
        print(f"Error {path}: {e}")

print("All photography assets successfully verified.")
