from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Hive, HiveNote


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
            <p><a href="/hives/" style="color: #856404; font-weight: bold;">🍯 View Your Hives 🍯</a></p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)


def hive_list(request):
    """Display a list of all hives."""
    hives = Hive.objects.all()
    return render(request, 'core/hive_list.html', {'hives': hives})


def hive_detail(request, hive_id):
    """Display details for a specific hive including its notes."""
    hive = get_object_or_404(Hive, id=hive_id)
    notes = hive.hivenote_set.all()
    return render(request, 'core/hive_detail.html', {'hive': hive, 'notes': notes})


def add_note(request, hive_id):
    """Add a new note to a hive."""
    hive = get_object_or_404(Hive, id=hive_id)
    
    if request.method == 'POST':
        note_text = request.POST.get('note_text', '').strip()
        if note_text:
            HiveNote.objects.create(hive=hive, note_text=note_text)
            messages.success(request, f'Note added to {hive.name}')
            return redirect('hive_detail', hive_id=hive.id)
        else:
            messages.error(request, 'Note text cannot be empty')
    
    return render(request, 'core/add_note.html', {'hive': hive})


def create_hive(request):
    """Create a new hive."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            hive = Hive.objects.create(name=name)
            messages.success(request, f'Hive "{hive.name}" created successfully')
            return redirect('hive_list')
        else:
            messages.error(request, 'Hive name cannot be empty')
    
    return render(request, 'core/create_hive.html')