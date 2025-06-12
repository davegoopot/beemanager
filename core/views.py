from django.shortcuts import render


def home_page(request):
    """Display a list of hives for the beekeeper."""
    # Sample hive data - in a real application this would come from the database
    hives = [
        {"id": 1, "name": "Hive 1", "status": "Active"},
        {"id": 2, "name": "Hive 2", "status": "Active"},
        {"id": 3, "name": "Hive 3", "status": "Active"},
    ]
    
    context = {
        'hives': hives,
        'total_hives': len(hives),
    }
    
    return render(request, 'core/home.html', context)