#!/usr/bin/python3
"""
Mark Down
"""


import re
import sys
import os
import hashlib


def convert_markdown_to_html(markdown_file, output_file):
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown content from the file
    with open(markdown_file, "r") as md_file:
        markdown_content = md_file.read()

    # Replace Markdown headings with corresponding HTML tags
    html_content = re.sub(r"^(#{1,6})\s+(.+)$", r"<\1>\2</\1>", markdown_content, flags=re.MULTILINE)
    
    # Replace Markdown unordered lists with corresponding HTML tags
    html_content = re.sub(r"^\s*-\s+(.+)$", r"<ul>\n<li>\1</li>\n</ul>", markdown_content, flags=re.MULTILINE)
    
    # Replace Markdown ordered lists with corresponding HTML tags
    html_content = re.sub(r"^\s*\*\s+(.+)$", r"<ol>\n<li>\1</li>\n</ol>", markdown_content, flags=re.MULTILINE)
    
    # Replace Markdown paragraphs with corresponding HTML tags
    html_content = re.sub(r"(?<=\n\n)([^\n]+)(?=\n\n)", r"<p>\1</p>", markdown_content)

    # Replace line breaks within paragraphs
    html_content = html_content.replace("\n", "<br />\n")
    
    # Replace Markdown bold syntax with corresponding HTML tags
    html_content = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", markdown_content)
    html_content = re.sub(r"__(.+?)__", r"<em>\1</em>", html_content)
    
    # Replace Markdown bold syntax with corresponding HTML tags
    html_content = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", markdown_content)
    html_content = re.sub(r"__(.+?)__", r"<em>\1</em>", html_content)

    # Convert content to MD5 (lowercase)
    md5_hash = hashlib.md5(html_content.encode()).hexdigest()

    # Remove all 'c' (case insensitive) from the content
    modified_content = re.sub(r"c", "", html_content, flags=re.IGNORECASE)

    # Write the modified HTML content to the output file
    with open(output_file, "w") as html_file:
        html_file.write(modified_content)

    # Write the HTML content to the output file
    with open(output_file, "w") as html_file:
        html_file.write(html_content)


    # If everything is successful, exit with code 0
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
