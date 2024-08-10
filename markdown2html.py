#!/usr/bin/python3
"""
Mark Down
"""


import re
import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    """ convert markdown function """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown content from the input file
    with open(markdown_file, "r") as md_file:
        markdown_content = md_file.read()

    # Convert Markdown headings to HTML
    html_content = re.sub(r"(#+)\s+(.*)", r"<\1>\2</\1>", markdown_content)

    # Write the HTML content to the output file
    with open(output_file, "w") as html_file:
        html_file.write(html_content)
    sys.exit(0)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
