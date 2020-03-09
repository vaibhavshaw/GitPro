from django.shortcuts import render
from django.http import HttpResponse
from .forms import RepoForm
from django.views import View
from .GithubAPIfetch import GitHubAPIFetch

# Create your views here.


class Home(View):

    def get(self, request, *args, **kwargs):
        form = RepoForm()
        context = {
            'form': form
        }
        return render(request, 'gitrepo/home.html', context)

    def post(self, request, *args, **kwargs):
        form = RepoForm(request.POST)
        context = {
            'form': form
        }
        template = 'gitrepo/home.html'
        if form.is_valid():
            Organisation_name = form.cleaned_data.get('organisation')
            top_N_repo = form.cleaned_data.get('N')
            top_M_committees = form.cleaned_data.get('M')
            APIObject = GitHubAPIFetch()
            repos, repo_all = APIObject.get_top_N_repo(
                Organisation_name, top_N_repo, top_M_committees)
            context = {
                'repos': repos,
                'repo_all': repo_all,
                'top_N_repo': min(top_N_repo, 5),
                'top_M_committees': min(top_M_committees, 5)
            }
            template = 'gitrepo/data.html'
        return render(request, template, context)
