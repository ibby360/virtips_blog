from category.models import Category

def cat_links(request):
    links = Category.objects.all()
    return dict(links=links)