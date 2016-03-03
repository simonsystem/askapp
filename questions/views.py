from django.shortcuts import render
from .models import Question

def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    answers = question.answer_set.all()

    return render(request, "question.html", {"question": question, "answers": answers})
