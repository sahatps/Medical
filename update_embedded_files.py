#!/usr/bin/env python3
"""
Update embedded files in index.html with latest versions
"""

import re
from pathlib import Path

def read_file_content(filepath):
    """Read file content and escape for JavaScript template literal"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Escape backticks and ${} for JavaScript template literals
    content = content.replace('\\', '\\\\')  # Escape backslashes first
    content = content.replace('`', '\\`')    # Escape backticks
    # Don't escape ${} in Python f-strings as they're already handled
    return content

def update_index_html():
    """Update index.html with latest embedded file contents"""

    index_path = Path('public/index.html')

    if not index_path.exists():
        print(f"❌ {index_path} not found!")
        return False

    print(f"📄 Reading {index_path}...")
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Files to embed
    files_to_embed = {
        'app_launcher.py': 'app_launcher',
        'start_app.bat': 'start_bat',
        'start_app.sh': 'start_sh',
    }

    for filepath, key in files_to_embed.items():
        file_path = Path(filepath)

        if not file_path.exists():
            print(f"⚠️  {filepath} not found, skipping...")
            continue

        print(f"📥 Reading {filepath}...")
        file_content = read_file_content(file_path)

        # Find and replace the embedded content
        # Pattern: key: { filename: '...', content: `...` }

        if key == 'app_launcher':
            pattern = r"(app_launcher:\s*\{\s*filename:\s*'app_launcher\.py',\s*content:\s*`)[^`]*(`\s*\})"
        elif key == 'start_bat':
            pattern = r"(start_bat:\s*\{\s*filename:\s*'start_app\.bat',\s*content:\s*`)[^`]*(`\s*\})"
        elif key == 'start_sh':
            pattern = r"(start_sh:\s*\{\s*filename:\s*'start_app\.sh',\s*content:\s*`)[^`]*(`\s*\})"
        else:
            continue

        replacement = r"\1" + file_content + r"\2"

        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if new_content != content:
            print(f"✅ Updated {key} in index.html")
            content = new_content
        else:
            print(f"⚠️  No changes for {key}")

    # Write updated content
    print(f"\n💾 Writing updated {index_path}...")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ index.html updated successfully!")
    return True

if __name__ == '__main__':
    print("=" * 60)
    print("🔄 Updating Embedded Files in index.html")
    print("=" * 60)
    print()

    success = update_index_html()

    if success:
        print("\n✅ All done!")
    else:
        print("\n❌ Update failed!")
        exit(1)
