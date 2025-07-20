import os
import re

# Root directory to scan
root_dir = "posts"

# Regex patterns
empty_tags_pattern = re.compile(r'^Tags\s*=\s*\[\s*\]\s*$', re.IGNORECASE)
categories_pattern = re.compile(r'^Categories\s*=\s*(\[.*\])\s*$', re.IGNORECASE)

for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(dirpath, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            if empty_tags_pattern.match(line):
                continue  # Remove `Tags = []`
            m = categories_pattern.match(line)
            if m:
                new_lines.append(f"Tags = {m.group(1)}\n")  # Rename `Categories = [...]` to `Tags = [...]`
            else:
                new_lines.append(line)

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

print("✅ All markdown files updated recursively.")
