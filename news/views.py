from django.shortcuts import render
from django.views import View
from news.models import Story


class NewsView(View):
    def get(self, request):
        stories = Story.objects.order_by('-publication_date')[:3]
        context_dict = {'stories': stories}

        return render(request, 'news/index.html', context=context_dict)


class ShowMoreView(View):
    def get(self, request):
        results = int(request.GET['results']) + 3

        stories = Story.objects.order_by('-publication_date')[:results]
        context_dict = {'stories': stories}

        return render(request, 'news/list_stories.html', context=context_dict)
