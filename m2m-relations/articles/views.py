from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().order_by('-published_at')
    for article in articles:
        article.scopes_sorted = sorted(
            article.scopes.all().select_related('tag'),
            key=lambda scope: (not scope.is_main, scope.tag.name)
        )
    context = {'object_list': articles}

    return render(request, template, context)
