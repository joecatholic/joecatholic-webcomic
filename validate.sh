#!/bin/bash

# Joe Catholic Site Validator
# This script checks if everything is set up correctly

echo "================================================"
echo "Joe Catholic Site Validation"
echo "================================================"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

checks_passed=0
checks_failed=0

# Function to check if a file exists
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} Found: $1"
        ((checks_passed++))
    else
        echo -e "${RED}✗${NC} Missing: $1"
        ((checks_failed++))
    fi
}

# Function to check if a directory exists
check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} Found directory: $1"
        ((checks_passed++))
    else
        echo -e "${YELLOW}!${NC} Missing directory: $1 (will be created when needed)"
    fi
}

# Function to count files in a directory
count_files() {
    if [ -d "$1" ]; then
        count=$(ls -1 "$1" 2>/dev/null | wc -l)
        echo -e "${GREEN}✓${NC} $1: $count files"
        ((checks_passed++))
    else
        echo -e "${YELLOW}!${NC} $1: Directory doesn't exist yet"
    fi
}

echo "Checking core files..."
check_file "_config.yml"
check_file "Gemfile"
check_file "README.md"
check_file "DEPLOYMENT_GUIDE.md"
check_file "netlify.toml"

echo ""
echo "Checking layouts..."
check_dir "_layouts"
check_file "_layouts/default.html"
check_file "_layouts/comic.html"

echo ""
echo "Checking includes..."
check_dir "_includes"
check_file "_includes/comic-display.html"

echo ""
echo "Checking pages..."
check_file "index.html"
check_file "archive.html"

echo ""
echo "Checking admin setup..."
check_dir "admin"
check_file "admin/index.html"
check_file "admin/config.yml"

echo ""
echo "Checking assets..."
check_dir "assets"
check_dir "assets/css"
check_file "assets/css/style.css"
check_dir "assets/comics"
check_dir "assets/images"

echo ""
echo "Checking content..."
check_dir "_comics"
count_files "_comics"

echo ""
echo "Checking migration tools..."
check_file "migrate_comiccontrol.py"

echo ""
echo "================================================"
echo "Summary"
echo "================================================"
echo -e "${GREEN}Passed: $checks_passed${NC}"
echo -e "${RED}Failed: $checks_failed${NC}"
echo ""

if [ $checks_failed -eq 0 ]; then
    echo -e "${GREEN}All core files present!${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Add your comics to _comics/ directory"
    echo "2. Add your comic images to assets/comics/"
    echo "3. Add your logo to assets/images/logo.png"
    echo "4. Run: bundle install"
    echo "5. Run: bundle exec jekyll serve"
    echo "6. Visit: http://localhost:4000"
else
    echo -e "${RED}Some files are missing. Please check the setup.${NC}"
fi

echo ""
echo "================================================"
