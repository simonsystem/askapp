from django.test import TestCase
from .models import Question, Answer

class QuestionsTestCase(TestCase):
    def setUp(self):
        Question.objects.create(text="Wie spät ist es?")
        uhr = Question.objects.create(text="Wer hat an der Uhr gedreht?")
        uhr.answer_set.create(text="Ich.")
        uhr.answer_set.create(text="Niemand.")

    def test_questions_can_be_answered(self):
        zeit = Question.objects.get(text="Wie spät ist es?")
        zeit.answer_set.create(text="12.")
        zeit.save()
        self.assertEqual(zeit.answer_set.count(), 1)

    def test_answers_can_be_accepted(self):
        uhr = Question.objects.get(text="Wer hat an der Uhr gedreht?")
        ich = uhr.answer_set.get(text="Ich.")
        niemand = uhr.answer_set.get(text="Niemand.")
        niemand.is_accepted = True
        uhr.save()
        self.assertEqual(uhr.has_accepted_answer, True)
        self.assertEqual(niemand.is_accepted, True)
        ich.is_accepted = True
        uhr.save()
        self.assertEqual(niemand.is_accepted, False)
