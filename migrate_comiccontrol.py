#!/usr/bin/env python3
"""
ComicControl to Jekyll Migration Script

This script helps migrate your ComicControl comics from MySQL to Jekyll Markdown files.

Requirements:
    pip install pymysql python-slugify pyyaml

Usage:
    1. Update the database credentials below
    2. Run: python3 migrate_comiccontrol.py
    3. Comics will be created in _comics/ directory
"""

import pymysql
import os
from datetime import datetime
from slugify import slugify
import yaml
import shutil

# =============================================================================
# CONFIGURATION - UPDATE THESE VALUES
# =============================================================================

DB_CONFIG = {
    'host': 'localhost',  # Your MySQL host
    'user': 'your_username',  # Your MySQL username
    'password': 'your_password',  # Your MySQL password
    'database': 'your_database',  # Your ComicControl database name
    'charset': 'utf8mb4'
}

# Path to your ComicControl comics directory
SOURCE_COMICS_DIR = '/path/to/your/current/site/comics/'

# Path to this Jekyll project
OUTPUT_DIR = '_comics/'
IMAGES_DIR = 'assets/comics/'

# =============================================================================
# MIGRATION FUNCTIONS
# =============================================================================

def connect_db():
    """Connect to MySQL database"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        print("✓ Connected to database")
        return connection
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return None

def fetch_comics(connection):
    """Fetch all comics from ComicControl database"""
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # Adjust this query based on your ComicControl table structure
            # This is a typical ComicControl schema
            query = """
                SELECT 
                    id,
                    title,
                    post,
                    filename,
                    alt,
                    transcript,
                    published,
                    publish_date,
                    tags
                FROM comics
                ORDER BY publish_date ASC
            """
            cursor.execute(query)
            comics = cursor.fetchall()
            print(f"✓ Found {len(comics)} comics")
            return comics
    except Exception as e:
        print(f"✗ Failed to fetch comics: {e}")
        return []

def create_comic_file(comic, comic_number):
    """Create a Jekyll markdown file for a comic"""
    
    # Parse publish date
    pub_date = comic['publish_date']
    if isinstance(pub_date, str):
        pub_date = datetime.strptime(pub_date, '%Y-%m-%d %H:%M:%S')
    
    # Create filename
    date_str = pub_date.strftime('%Y-%m-%d')
    slug = slugify(comic['title'])
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Parse tags
    tags = []
    if comic.get('tags'):
        tags = [tag.strip() for tag in comic['tags'].split(',')]
    
    # Build frontmatter
    frontmatter = {
        'layout': 'comic',
        'title': comic['title'],
        'date': pub_date.strftime('%Y-%m-%d %H:%M:%S %z'),
        'comic_number': comic_number,
        'episode': 'Episode 1',  # You may need to adjust this
        'image': f"/assets/comics/{comic['filename']}",
        'alt': comic.get('alt', comic['title']),
        'tags': tags if tags else None,
        'published': bool(comic.get('published', 1))
    }
    
    # Add transcript if exists
    if comic.get('transcript'):
        frontmatter['transcript'] = comic['transcript']
    
    # Remove None values
    frontmatter = {k: v for k, v in frontmatter.items() if v is not None}
    
    # Build content
    content = []
    content.append('---')
    content.append(yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True))
    content.append('---')
    content.append('')
    
    # Add post content (commentary)
    if comic.get('post'):
        content.append(comic['post'])
    
    # Write file
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    
    return filename

def copy_comic_images():
    """Copy comic images to Jekyll assets directory"""
    os.makedirs(IMAGES_DIR, exist_ok=True)
    
    if not os.path.exists(SOURCE_COMICS_DIR):
        print(f"⚠ Source comics directory not found: {SOURCE_COMICS_DIR}")
        print("  Please copy images manually to: {IMAGES_DIR}")
        return 0
    
    copied = 0
    for filename in os.listdir(SOURCE_COMICS_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
            src = os.path.join(SOURCE_COMICS_DIR, filename)
            dst = os.path.join(IMAGES_DIR, filename)
            shutil.copy2(src, dst)
            copied += 1
    
    print(f"✓ Copied {copied} comic images")
    return copied

def main():
    """Main migration function"""
    print("=" * 60)
    print("ComicControl to Jekyll Migration Script")
    print("=" * 60)
    print()
    
    # Connect to database
    connection = connect_db()
    if not connection:
        return
    
    try:
        # Fetch comics
        comics = fetch_comics(connection)
        if not comics:
            print("No comics found to migrate")
            return
        
        # Create comic files
        print("\nCreating Jekyll comic files...")
        created = 0
        for idx, comic in enumerate(comics, 1):
            try:
                filename = create_comic_file(comic, idx)
                created += 1
                print(f"  ✓ Created: {filename}")
            except Exception as e:
                print(f"  ✗ Failed to create comic #{idx}: {e}")
        
        print(f"\n✓ Created {created}/{len(comics)} comic files")
        
        # Copy images
        print("\nCopying comic images...")
        copy_comic_images()
        
        print("\n" + "=" * 60)
        print("Migration Complete!")
        print("=" * 60)
        print(f"\nNext steps:")
        print(f"1. Review the files in {OUTPUT_DIR}")
        print(f"2. Verify images in {IMAGES_DIR}")
        print(f"3. Test with: bundle exec jekyll serve")
        print(f"4. Fix any issues and adjust episode numbers if needed")
        
    finally:
        connection.close()

if __name__ == "__main__":
    main()
