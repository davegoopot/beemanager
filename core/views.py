from django.http import HttpResponse


def hello_world(request):
    """A simple Hello World view for bee management."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bee Manager</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff3cd;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #856404;
                text-align: center;
            }
            .bee-emoji {
                font-size: 2em;
                text-align: center;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐝 Welcome to Bee Manager 🐝</h1>
            <div class="bee-emoji">🍯🐝🌻</div>
            <p>Hello World! This is a simple Django application for managing bee hives.</p>
            <p>The bee management system is now running and ready to help you monitor your hives!</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)