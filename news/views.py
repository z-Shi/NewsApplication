from django.shortcuts import render
from django.views import View


class NewsView(View):
    def get(self, request):
        stories = Story.objects.order_by('-publication_date')
        context_dict = {'stories': stories}

        return render(request, 'news/index.html', context=context_dict)
