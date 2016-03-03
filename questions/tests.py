from django.test import TestCase
from .models import Question, Answer

class QuestionsTestCase(TestCase):
    def setUp(self):
        Question.objects.create(text="Wer hat an der Uhr gedreht?")
        Question.objects.create(text="Wie spät ist es?")

    def test_questions_can_be_answered(self):
        """Animals that can speak are correctly identified"""
        uhr = Question.objects.get(text="Wer hat an der Uhr gedreht?")
        uhr.answer_set.create(text="Ich.")
        uhr.save()
    def test_answers_can_be_accepted(self):
        """Animals that can speak are correctly identified"""
        uhr = Question.objects.get(text="Wer hat an der Uhr gedreht?")
        uhr.answer_set.create(text="Niemand.")
        uhr.answer_set.get(text="Niemand.").is_accepted = True
        uhr.save()