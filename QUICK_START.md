# Quick Start Guide - Get Running in 15 Minutes

This is the **fastest path** to see your webcomic running locally.

## Step 1: Install Jekyll (5 minutes)

**Mac:**
```bash
brew install ruby
gem install bundler jekyll
```

**Windows:**
- Download from https://rubyinstaller.org/
- Install and check "Add to PATH"
- Open Command Prompt:
```bash
gem install bundler jekyll
```

## Step 2: Install Dependencies (2 minutes)

In this project folder:
```bash
bundle install
```

## Step 3: Run the Site (1 minute)

```bash
bundle exec jekyll serve
```

Open http://localhost:4000

**That's it!** You should see the example comics.

---

## Next: Customize Your Site

### Add Your First Real Comic (3 minutes)

1. Create a file: `_comics/2025-02-10-your-comic-title.md`
2. Copy this template:

```markdown
---
layout: comic
title: "Your Comic Title"
date: 2025-02-10 07:00:00 -0500
comic_number: 1
episode: "Episode 1"
image: "/assets/comics/your-image.jpg"
alt: "Description of your comic"
tags: 
  - Your Tag
published: true
---

Optional commentary about this comic.
```

3. Put your comic image in `assets/comics/your-image.jpg`
4. Refresh http://localhost:4000

### Change the Logo (2 minutes)

Replace `assets/images/logo.png` with your logo image.

Edit `_layouts/default.html` line 10 to update the path if needed.

### Change Colors (2 minutes)

Edit `assets/css/style.css` lines 3-7:

```css
:root {
    --primary-color: #2c5aa0;  /* Your blue */
    --secondary-color: #8b0000; /* Your red */
}
```

---

## Ready to Deploy?

See **DEPLOYMENT_GUIDE.md** for full deployment instructions.

## Questions?

- **How do I add more comics?** Create more .md files in `_comics/`
- **Where are my images?** Put them in `assets/comics/`
- **How do I change the layout?** Edit files in `_layouts/`
- **What's this admin panel?** Set up after deploying to Netlify

---

## Common Issues

**"Bundle install fails"**
- Make sure Ruby is installed: `ruby -v`
- Try: `gem install bundler` first

**"jekyll serve fails"**
- Try: `bundle exec jekyll serve --trace` to see the error
- Most common: YAML syntax error in frontmatter

**"My comic doesn't show up"**
- Check the date isn't in the future
- Verify `published: true`
- Check the file is in `_comics/` folder

---

## File Structure at a Glance

```
joecatholic-migration/
├── _comics/              ← Your comic posts go here
├── _layouts/             ← HTML templates
├── _includes/            ← Reusable HTML components
├── assets/
│   ├── comics/          ← Comic images go here
│   ├── images/          ← Logo, etc.
│   └── css/             ← Styling
├── admin/               ← CMS configuration
├── _config.yml          ← Site settings
└── index.html           ← Homepage
```

---

**Stuck?** Read the full README.md or DEPLOYMENT_GUIDE.md
