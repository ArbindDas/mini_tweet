from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/home.html')



def about(request):
    context = {
        'tech_stack': [
            {'icon': '🐍', 'name': 'Python',   'role': 'Language'},
            {'icon': '🦄', 'name': 'Django',   'role': 'Backend'},
            {'icon': '🎨', 'name': 'Tailwind', 'role': 'Styling'},
            {'icon': '🗄️', 'name': 'SQLite',   'role': 'Database'},
        ],
        'features': [
            'Post short tweets',
            'View public feed',
            'Edit your tweets',
            'Delete your tweets',
            'User authentication',
            'Clean responsive UI',
        ],
    }
    return render(request, 'core/about.html', context)



def contact(request):
    return render(request, 'core/contact.html')

def search(request):
    q = request.GET.get('q', '').strip()
    tweets = Tweet.objects.filter(content__icontains=q).order_by('-created_at') if q else []
    return render(request, 'search.html', {'tweets': tweets, 'query': q})