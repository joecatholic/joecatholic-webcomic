# Joe Catholic Webcomic - Jekyll Migration

This is a complete migration of JoeCatholic.com from ComicControl (PHP/MySQL) to Jekyll (static site) with Netlify CMS for easy content management.

## Features

✅ **No Database Required** - All content stored in flat files (Markdown)
✅ **Visual Admin Panel** - Netlify CMS provides a WordPress-like editing experience
✅ **Automatic RSS Feed** - Built-in RSS generation
✅ **Comic Navigation** - First/Previous/Archive/Next/Latest buttons
✅ **Archive Page** - Searchable and filterable by episode
✅ **Tag System** - Tags and character filtering
✅ **Scheduled Posts** - Set publish dates in the future
✅ **Free Hosting** - Deploy to Netlify, GitHub Pages, or Vercel
✅ **Full Design Control** - Easy to customize CSS and templates

## Quick Start

### Local Development

1. **Install Jekyll** (one-time setup):
   ```bash
   # On Mac (requires Homebrew)
   brew install ruby
   gem install bundler jekyll
   
   # On Windows
   # Download and install from https://rubyinstaller.org/
   ```

2. **Install dependencies**:
   ```bash
   bundle install
   ```

3. **Run local server**:
   ```bash
   bundle exec jekyll serve
   ```
   
   Visit: http://localhost:4000

### Deploying to Netlify (Recommended)

1. **Push to GitHub**:
   - Create a new repository on GitHub
   - Push this code to your repository
   
2. **Connect to Netlify**:
   - Go to https://netlify.com
   - Click "New site from Git"
   - Connect your GitHub repository
   - Build settings:
     - Build command: `jekyll build`
     - Publish directory: `_site`
   
3. **Enable Netlify CMS**:
   - In Netlify dashboard, go to Identity
   - Click "Enable Identity"
   - Go to Settings > Identity > Registration preferences
   - Set to "Invite only"
   - Invite yourself via email
   
4. **Enable Git Gateway**:
   - Still in Identity settings
   - Scroll to "Services" > "Git Gateway"
   - Click "Enable Git Gateway"

5. **Access Admin Panel**:
   - Visit: `https://your-site.netlify.app/admin`
   - Login with the email you invited
   - Start adding comics!

## Content Structure

### Adding Comics

Comics are stored in `_comics/` folder as Markdown files:

```markdown
---
layout: comic
title: "Comic Title"
date: 2025-11-07 07:00:00 -0500
comic_number: 1
episode: "Episode 1"
image: "/assets/comics/comic-image.jpg"
alt: "Image description"
tags: 
  - Tag 1
  - Tag 2
characters:
  - Character Name
published: true
---

Optional commentary about the comic goes here.
```

### Using the Admin Panel

Once Netlify is set up:
1. Go to `yourdomain.com/admin`
2. Click "New Comics" → "Comic"
3. Fill in the form
4. Upload your comic image
5. Set publish date (can be future for scheduling)
6. Click "Publish"

The comic will automatically:
- Appear on the homepage when published
- Be added to the archive
- Generate navigation links
- Update the RSS feed

## Migration Steps from ComicControl

### 1. Export Your Comics

From your current ComicControl site, you need to export:
- All comic images from `/comics/` directory
- Comic metadata (title, date, tags, etc.) from MySQL

### 2. Convert to Jekyll Format

I can create a Python script to help you convert your ComicControl MySQL data into Jekyll-formatted Markdown files.

### 3. Transfer Images

Copy all images to `/assets/comics/` directory

### 4. Test Locally

Run `bundle exec jekyll serve` and verify everything looks correct

### 5. Deploy

Push to GitHub and connect to Netlify

## Customization

### Changing Colors/Styling

Edit `/assets/css/style.css` - Look for the `:root` variables at the top:

```css
:root {
    --primary-color: #2c5aa0;  /* Main blue color */
    --secondary-color: #8b0000; /* Red accent color */
    /* etc. */
}
```

### Modifying Layout

- Homepage: `index.html`
- Comic post: `_layouts/comic.html`
- Archive: `archive.html`
- Navigation/Header: `_layouts/default.html`

### Changing Configuration

Edit `_config.yml` for site-wide settings

## Posting Schedule

To post twice a week automatically:
1. Create comics in the admin panel
2. Set future dates (e.g., Tuesday and Friday at 7 AM)
3. The comics will automatically appear when the date arrives
4. Netlify rebuilds the site automatically on schedule

## Cost Breakdown

- **Hosting**: $0 (Netlify free tier)
- **Domain**: ~$15/year (if using custom domain)
- **CMS**: $0 (Netlify CMS is free)
- **Total**: ~$15/year vs. typical $5-20/month hosting

## Support

If you need help:
1. Check Jekyll documentation: https://jekyllrb.com/docs/
2. Netlify CMS docs: https://decapcms.org/docs/
3. Create an issue in this repository

## License

Content © Fr. Christopher J. Decker and Collarmark Productions
Theme and code can be freely modified for your use.
