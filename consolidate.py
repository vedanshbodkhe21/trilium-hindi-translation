import json
import os

def generate_comparison_html(en_file, hi_file, output_file):
    if not os.path.exists(en_file) or not os.path.exists(hi_file):
        print("Error: JSON files not found.")
        return

    with open(en_file, 'r', encoding='utf-8') as f:
        en_data = json.load(f)
    
    with open(hi_file, 'r', encoding='utf-8') as f:
        hi_data = json.load(f)

    all_keys = sorted(en_data.keys())

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trilium Translation Comparison</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Outfit:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #6366f1;
            --bg: #0f172a;
            --surface: #1e293b;
            --text: #f1f5f9;
            --text-muted: #94a3b8;
            --border: #334155;
            --missing: #450a0a;
            --missing-text: #fca5a5;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 4rem;
            line-height: 1.6;
            font-size: 1.75rem;
        }}

        header {{
            margin-bottom: 2rem;
            text-align: center;
        }}

        h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 5rem;
            margin-bottom: 1rem;
            background: linear-gradient(to right, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .stats {{
            font-size: 1.5rem;
            color: var(--text-muted);
            margin-bottom: 3rem;
        }}

        table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: var(--surface);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            border: 1px solid var(--border);
        }}

        th {{
            background: #334155;
            padding: 1rem;
            text-align: left;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            position: sticky;
            top: 0;
            z-index: 10;
        }}

        td {{
            padding: 1rem;
            border-bottom: 1px solid var(--border);
            vertical-align: top;
        }}

        tr:last-child td {{
            border-bottom: none;
        }}

        .key-cell {{
            font-family: monospace;
            font-size: 1.5rem;
            color: #818cf8;
            width: 25%;
        }}

        .en-cell {{
            width: 40%;
        }}

        .hi-cell {{
            width: 40%;
        }}

        .missing-row {{
            background-color: var(--missing);
        }}

        .missing-row td {{
            border-bottom-color: #7f1d1d;
        }}

        .empty-tag {{
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background: #991b1b;
            color: white;
            border-radius: 6px;
            font-size: 1.2rem;
            font-weight: bold;
            text-transform: uppercase;
        }}

        tr:hover td {{
            background-color: rgba(255, 255, 255, 0.03);
        }}

        footer {{
            margin-top: 5rem;
            text-align: center;
            color: var(--text-muted);
            font-size: 1.2rem;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Localization Quality Control</h1>
        <div class="stats">
            Comparing <strong>{len(all_keys)}</strong> keys from <code>{en_file}</code> to <code>{hi_file}</code>
        </div>
    </header>

    <table>
        <thead>
            <tr>
                <th>Key Path</th>
                <th>English (Source)</th>
                <th>Hindi (Target)</th>
            </tr>
        </thead>
        <tbody>
"""

    for key in all_keys:
        en_val = en_data.get(key, "")
        hi_val = hi_data.get(key, "")
        
        is_missing = not hi_val or hi_val.strip() == ""
        row_class = ' class="missing-row"' if is_missing else ""
        hi_display = f'<span class="empty-tag">Missing Translation</span>' if is_missing else hi_val
        
        # Escape HTML
        en_val = en_val.replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
        hi_display = hi_display.replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>") if not is_missing else hi_display

        html_content += f"""
            <tr{row_class}>
                <td class="key-cell">{key}</td>
                <td class="en-cell">{en_val}</td>
                <td class="hi-cell">{hi_display}</td>
            </tr>"""

    html_content += """
        </tbody>
    </table>
    <footer>
        Generated by Antigravity AI Translator Tool
    </footer>
</body>
</html>
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Comparison report generated: {output_file}")

if __name__ == "__main__":
    generate_comparison_html(
        '/home/scion/Downloads/weblate/trilium-client-en.json',
        '/home/scion/Downloads/weblate/trilium-client-hi.json',
        '/home/scion/Downloads/weblate/comparison.html'
    )
