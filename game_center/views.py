from django.shortcuts import render
from django.http import HttpResponse
from game_center.models import Category
from game_center.models import Page
from game_center.models import Score
from game_center.models import Game
from game_center.forms  import CategoryForm
from game_center.forms  import PageForm
from game_center.forms  import ScoreForm


# Create your views here.
def index(request):
    Score_list = Score.objects.order_by('-score')[:5]

    
    context_dict = {'score': Score_list}

    return render(request,'game_center/index.html', context_dict)

def about(request):
    return render(request,'game_center/about.html')
def game(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ScoreForm()

    return render(request,'game_center/web05/index.html',{'form': form})

    

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    context_dict['category_name_slug']=category_name_slug
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    context_dict['category_name_slug']=category_name_slug
    return render(request, 'game_center/category.html', context_dict)

def add_category(request):
    # A HTTP POST?

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'game_center/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try: 
            cat = Category.objects.get(slug=category_name_slug)

    except Category.DoesNotExist:
           cat = None 
           

    if request.method == 'POST':
            
            form = PageForm(request.POST)
            
            if form.is_valid():
                if cat:
                    page = form.save(commit=False)
                    page.category = cat
                    page.views = 0
                    page.save()
                    # probably better to use a redirect here.
                return category(request, category_name_slug)
            else:
                print form.errors
    else:
        form = PageForm()
        
    context_dict = {'form':form, 'category': cat}     
    return render(request, 'game_center/add_page.html', context_dict)

def addscore(request):
    # A HTTP POST?

    if request.method == 'POST':
        form = ScoreForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ScoreForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'game_center/addscore.html', {'form': form})
