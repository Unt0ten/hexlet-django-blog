from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        name = reverse('article', kwargs={'article_id': 42, 'tags': 'python'})
        return redirect(name)


def index(request, tags='python', article_id=42):
    return render(
        request, 'article/index.html',
        context={'article_id': article_id, 'tags': tags}
        )
