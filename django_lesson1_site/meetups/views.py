from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # return  HttpResponse('Hello World')
    meetups = [
        {'title': 'The First', 'location': 'Bahamas', 'slug': 'a-first-meetup'},
        {'title': 'The Second', 'location': 'Hawaii', 'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'my_meetups': meetups
        })

def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A first meetup', 
        'description': 
        'Its the first meetup. Yeeeeeyyyy!'
        }
    return render(request,'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']    
        } )