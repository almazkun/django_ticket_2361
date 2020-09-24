from django.views.generic import ListView, DetailView

from main.models import Author, Book, BookImage

# Create your views here.
class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"
    

class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.filter(author=self.object, book_image__isnull=False)
        context["books"] = books
        return context
