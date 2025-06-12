from django.http import HttpResponse


def home_page(request):
    """Display a list of hives for the beekeeper."""
    # Sample hive data - in a real application this would come from the database
    hives = [
        {"id": 1, "name": "Hive 1", "status": "Active"},
        {"id": 2, "name": "Hive 2", "status": "Active"},
        {"id": 3, "name": "Hive 3", "status": "Active"},
    ]
    
    hive_html = ""
    for hive in hives:
        hive_html += f'<div class="hive-item"><strong>{hive["name"]}</strong> - Status: {hive["status"]}</div>'
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bee Manager</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff3cd;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #856404;
                text-align: center;
            }}
            .bee-emoji {{
                font-size: 2em;
                text-align: center;
                margin: 20px 0;
            }}
            .hive-list {{
                margin: 20px 0;
            }}
            .hive-item {{
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                background-color: #f8f9fa;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐝 Bee Manager 🐝</h1>
            <div class="bee-emoji">🍯🐝🌻</div>
            <h2>Hive List</h2>
            <div class="hive-list">
                {hive_html}
            </div>
            <p>Total hives: {len(hives)}</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)