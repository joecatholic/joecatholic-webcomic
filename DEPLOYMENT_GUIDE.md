# Complete Deployment Guide for JoeCatholic.com

## Overview

This guide will walk you through deploying your webcomic from ComicControl to Jekyll + Netlify CMS. The entire process should take 2-3 hours.

## Prerequisites

- Your current ComicControl site accessible (for export)
- GitHub account (free)
- Netlify account (free)
- Basic terminal/command line knowledge

---

## Part 1: Local Setup (30-45 minutes)

### Step 1: Install Ruby and Jekyll

**On Mac:**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Ruby
brew install ruby

# Install Jekyll and Bundler
gem install bundler jekyll
```

**On Windows:**
1. Download Ruby installer from https://rubyinstaller.org/
2. Run the installer and check "Add Ruby to PATH"
3. Open Command Prompt and run:
```bash
gem install bundler jekyll
```

### Step 2: Clone/Download This Project

Download this project folder to your computer, or if using Git:
```bash
git clone [your-repo-url]
cd joecatholic-migration
```

### Step 3: Install Dependencies

```bash
bundle install
```

### Step 4: Test Locally

```bash
bundle exec jekyll serve
```

Open http://localhost:4000 in your browser. You should see the example comics.

---

## Part 2: Migrate Your Content (1-2 hours)

### Option A: Manual Migration (Recommended for 68 comics)

Since you have 68 comics, I recommend manually creating them through the admin panel after deployment. This gives you a chance to review and clean up content.

### Option B: Automated Migration (Faster but requires database access)

1. **Get Database Credentials:**
   - Login to your current hosting cPanel
   - Find your MySQL database credentials
   - Download a database backup

2. **Update Migration Script:**
   - Edit `migrate_comiccontrol.py`
   - Add your database credentials
   - Add path to your comics directory

3. **Install Python Requirements:**
   ```bash
   pip install pymysql python-slugify pyyaml
   ```

4. **Run Migration:**
   ```bash
   python3 migrate_comiccontrol.py
   ```

### Copy Comic Images

Regardless of which option you choose:

1. Download all images from your current site's `/comics/` directory
2. Copy them to `assets/comics/` in this project
3. Verify all images are present

---

## Part 3: GitHub Setup (15 minutes)

### Step 1: Create GitHub Repository

1. Go to https://github.com
2. Click "New Repository"
3. Name it: `joecatholic-webcomic`
4. Make it Public (required for free Netlify)
5. Don't initialize with README (we already have one)
6. Click "Create Repository"

### Step 2: Push Your Code

In your project folder:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Joe Catholic webcomic migration"

# Add GitHub remote (replace with your URL)
git remote add origin https://github.com/YOUR-USERNAME/joecatholic-webcomic.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Part 4: Netlify Deployment (30 minutes)

### Step 1: Create Netlify Account

1. Go to https://netlify.com
2. Sign up with GitHub (easiest option)
3. Authorize Netlify to access your repositories

### Step 2: Deploy Site

1. Click "Add new site" → "Import an existing project"
2. Choose "GitHub"
3. Select your `joecatholic-webcomic` repository
4. Build settings should auto-detect:
   - Build command: `bundle exec jekyll build`
   - Publish directory: `_site`
5. Click "Deploy site"

Wait 2-3 minutes for the first build to complete.

### Step 3: Set Up Custom Domain (Optional)

1. In Netlify dashboard, go to "Domain settings"
2. Click "Add custom domain"
3. Enter: `joecatholic.com`
4. Follow instructions to update DNS settings at your domain registrar
5. Netlify will automatically provision SSL certificate

**DNS Settings at your domain registrar:**
- Type: A Record
- Name: @
- Value: 75.2.60.5
- Type: CNAME
- Name: www
- Value: [your-site].netlify.app

### Step 4: Enable Netlify CMS

1. In Netlify dashboard, go to "Identity"
2. Click "Enable Identity"
3. Under "Registration preferences" → Select "Invite only"
4. Click "Invite users" → Add your email
5. Go to "Services" → Click "Enable Git Gateway"

### Step 5: Access Admin Panel

1. Check your email for Netlify invitation
2. Click the link and set your password
3. Go to: `https://your-site.netlify.app/admin`
4. Login with your email and password

---

## Part 5: Configure Scheduled Publishing (10 minutes)

To automatically publish comics on schedule:

1. In Netlify dashboard, go to "Build & deploy"
2. Scroll to "Build hooks"
3. Click "Add build hook"
4. Name it: "Scheduled Publish"
5. Copy the webhook URL

Then set up automated builds:

**Option A: Use Netlify's scheduled builds**
1. Install the plugin from Netlify UI
2. Set schedule to run twice daily

**Option B: Use external scheduler (more reliable)**
1. Use a service like cron-job.org (free)
2. Create two jobs:
   - Tuesday at 7:00 AM
   - Friday at 7:00 AM
3. Set them to call your build hook URL

---

## Part 6: Adding Your First Comic (5 minutes)

1. Go to `your-site.netlify.app/admin`
2. Click "New Comics" → "Comic"
3. Fill in:
   - Title: "Your Comic Title"
   - Publish Date: Set future date/time for scheduled publishing
   - Comic Number: 1
   - Episode: "Episode 1"
   - Upload your comic image
   - Alt Text: Description for accessibility
   - Tags: Add relevant tags
   - Characters: Add character names
   - Commentary: Optional description
4. Click "Publish"

The comic will appear automatically at the scheduled time!

---

## Part 7: Customization (Ongoing)

### Change Colors

Edit `assets/css/style.css`:

```css
:root {
    --primary-color: #2c5aa0;  /* Change this to your blue */
    --secondary-color: #8b0000; /* Change this to your red */
}
```

### Update Logo

Replace `/assets/images/logo.png` with your logo

### Modify Header/Footer

Edit `_layouts/default.html`

---

## Comparison: Old vs New

| Feature | ComicControl (Old) | Jekyll + Netlify (New) |
|---------|-------------------|------------------------|
| **Hosting Cost** | $5-20/month | FREE |
| **Database** | MySQL required | None (flat files) |
| **Admin Panel** | Built-in PHP | Netlify CMS (visual) |
| **Speed** | Dynamic (slower) | Static (faster) |
| **Security** | PHP vulnerabilities | Minimal attack surface |
| **Backups** | Manual database dumps | Automatic (Git) |
| **Version Control** | None | Full Git history |
| **Customization** | PHP knowledge needed | HTML/CSS (easier) |

---

## Maintenance Tasks

### Weekly (Posting Comics)
1. Log into admin panel
2. Create new comic post
3. Set publish date
4. Upload image
5. That's it! Auto-publishes on schedule

### Monthly
- Review analytics in Netlify dashboard
- Check for any build failures

### Quarterly
- Update Jekyll and plugins: `bundle update`
- Review and update any links

---

## Troubleshooting

### Build Fails
- Check Netlify build log for errors
- Most common: YAML formatting in frontmatter
- Verify all required fields are present

### Images Not Showing
- Check image paths in markdown files
- Verify images are in `assets/comics/`
- Check file names match exactly (case-sensitive)

### Admin Panel Not Loading
- Verify Git Gateway is enabled
- Check that you've been invited to Identity
- Clear browser cache

### Comics Not Appearing
- Check `published: true` in frontmatter
- Verify date is in the past
- Trigger manual deploy in Netlify

---

## Getting Help

1. Check the README.md
2. Jekyll docs: https://jekyllrb.com/docs/
3. Netlify CMS: https://decapcms.org/docs/
4. Netlify Support: https://answers.netlify.com/

---

## Cost Summary

- **Domain renewal:** ~$15/year (existing expense)
- **Hosting:** $0 (Netlify free tier)
- **CMS:** $0 (open source)
- **SSL Certificate:** $0 (included with Netlify)

**Total: ~$15/year** (vs ~$60-240/year currently)

**Annual Savings: $45-225**

---

## Next Steps After Deployment

1. ✅ Migrate all 68 comics
2. ✅ Test navigation thoroughly
3. ✅ Set up scheduled publishing
4. ✅ Update DNS to point to Netlify
5. ✅ Create a few comics in advance
6. ✅ Share the new site!
7. ✅ Keep old site running for 30 days as backup
8. ✅ Cancel old hosting after confirming everything works

---

## Timeline Estimate

- **Setup & Testing:** 1 hour
- **Content Migration:** 2-4 hours (depending on method)
- **Deployment:** 1 hour
- **DNS Propagation:** 24-48 hours
- **Testing & Refinement:** 2-3 hours

**Total: 1-2 days of work spread over a week**

---

Good luck with your migration! The end result will be faster, cheaper, and easier to maintain.
