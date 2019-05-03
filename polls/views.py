from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # 指定ListView模板中使用的list context的名字
    context_object_name = 'latest_question_list'
    # 大概是通过这个返回ListView 中使用的list(或者说是set?), 文档里还有直接定义queryset的方式

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    # 指定模板名字, 默认名字是<app name>/<model name>_<class name>.html
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) as e:
        return render(request, 'polls/detail.htnl', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # reverse 反向查找url?视图?
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
