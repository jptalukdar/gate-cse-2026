#!/usr/bin/env python3
"""
Script to recursively add blank lines before the first item in markdown lists.
Handles numbered lists (1., 2., etc.) and bullet lists (- or *).
Skips if a blank line already exists before the list.
"""

import re
import os
import argparse
from pathlib import Path


def is_list_item(line: str) -> bool:
    """Check if line is a list item (numbered or bullet)."""
    stripped = line.lstrip()
    # Numbered list: 1., 2., etc.
    if re.match(r'^\d+\.\s', stripped):
        return True
    # Bullet list: - or *
    if re.match(r'^[-*]\s', stripped):
        return True
    return False


def is_blank_line(line: str) -> bool:
    """Check if line is blank (empty or whitespace only)."""
    return line.strip() == ''


def fix_list_spacing(content: str) -> str:
    """Add blank line before first list item if not already present."""
    lines = content.split('\n')
    result = []
    
    for i, line in enumerate(lines):
        # Check if current line is a list item
        if is_list_item(line):
            # Check if previous line exists and is not blank
            if i > 0 and not is_blank_line(lines[i - 1]):
                # Check if previous line is NOT also a list item (we only want first item)
                if not is_list_item(lines[i - 1]):
                    result.append('')  # Add blank line
        result.append(line)
    
    return '\n'.join(result)


def process_file(filepath: Path, dry_run: bool = False) -> bool:
    """Process a single markdown file. Returns True if modified."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        modified = fix_list_spacing(original)
        
        if original != modified:
            if dry_run:
                print(f"[DRY RUN] Would modify: {filepath}")
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified)
                print(f"Modified: {filepath}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def process_directory(directory: Path, dry_run: bool = False) -> tuple[int, int]:
    """
    Recursively process all markdown files in directory.
    Returns (total_files, modified_files).
    """
    total = 0
    modified = 0
    
    for filepath in directory.rglob('*.md'):
        total += 1
        if process_file(filepath, dry_run):
            modified += 1
    
    return total, modified


def main():
    parser = argparse.ArgumentParser(
        description='Add blank lines before first list items in markdown files.'
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Directory to process recursively (default: current directory)'
    )
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    
    args = parser.parse_args()
    directory = Path(args.path)
    
    if not directory.exists():
        print(f"Error: Path '{directory}' does not exist.")
        return 1
    
    if directory.is_file():
        if directory.suffix == '.md':
            process_file(directory, args.dry_run)
        else:
            print("Error: File must be a .md file")
            return 1
    else:
        total, modified = process_directory(directory, args.dry_run)
        print(f"\nProcessed {total} files, {'would modify' if args.dry_run else 'modified'} {modified} files.")
    
    return 0


if __name__ == '__main__':
    exit(main())
