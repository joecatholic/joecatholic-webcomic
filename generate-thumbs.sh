#!/bin/bash
echo "Generating thumbnails..."
mkdir -p assets/thumbnails

for img in assets/comics/*.jpg assets/comics/*.jpeg assets/comics/*.png assets/comics/*.webp; do
  [ -f "$img" ] || continue
  filename=$(basename "$img")
  thumb="assets/thumbnails/$filename"
  if [ ! -f "$thumb" ]; then
    echo "Creating thumb: $filename"
    convert "$img" -resize 400x -quality 75 "$thumb"
  else
    echo "Skipping (exists): $filename"
  fi
done

echo "Thumbnail generation complete."
