#!/usr/bin/env bash

# Exit immediately if a command fails with a non-zero status
set -euo pipefail

folders=(client server website)

for folder in "${folders[@]}"; do
  echo -n "Downloading $folder translations. "
  # Ensure the directory exists
  mkdir -p "$folder"

  # -f: fail silently on HTTP errors (don't save 404 page)
  # -s: silent mode (hides progress bar)
  # -S: Show error message on fail
  # -L: follow redirects
  curl -fsSL -X GET "https://hosted.weblate.org/download/trilium/$folder/en/" >"$folder/trilium-$folder-en.json"
  curl -fsSL -X GET "https://hosted.weblate.org/download/trilium/$folder/hi/" >"$folder/trilium-$folder-hi.json"
  echo "Done."
done

# download readme files, weblate returns markdown
echo -n "Downloading readme translations. "
mkdir -p "readme"
curl -fsSL -X GET "https://hosted.weblate.org/download/trilium/readme/en/" >"readme/trilium-readme-en.md"
curl -fsSL -X GET "https://hosted.weblate.org/download/trilium/readme/hi/" >"readme/trilium-readme-hi.md"
echo "Done."
