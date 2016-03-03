from django.shortcuts import render, get_object_or_404
from .models import Question

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()

    return render(request, "question.html", {
        "question": question, "answers": answers
    })
