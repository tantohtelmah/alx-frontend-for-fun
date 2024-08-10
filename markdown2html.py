#!/usr/bin/env python3
import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Your conversion logic goes here (e.g., using a Markdown library or regex)

    # If everything is successful:
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
