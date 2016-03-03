from django.db import models

"""
Model holding the question with a set of answers. One can be the accepted answer.
"""
class Question(models.Model):
    text = models.TextField(max_length=1000)
    accepted_answer = models.ForeignKey("Answer", null=True, blank=True, related_name="+")

    """
    Returns true if one of all answers is acccepted, false otherwise.
    """
    def has_accepted_answer(self):
        return accepted_answer is not None

    """
    Returns a list of all questions without accepted answers.
    """
    @classmethod
    def get_unanswered_questions(cls):
        return cls.objects.filter(accepted_answer=None)

    def __str__(self):
        return self.text[:20]

"""
Model holding the answer to a corresponding question.
"""
class Answer(models.Model):
    text = models.TextField(max_length=1000)
    question = models.ForeignKey("Question", null=True)

    """
    Returns true if this answer is marked as accepted, false otherwise.
    """
    def is_accepted(self):
        return self.question.has_accepted_answer(self) and self.question.accepted_answer.pk is this.pk

    """
    Mark this answer as accepted.
    """
    def set_accepted(self):
        self.question.accepted_answer = self
        self.question.save()

    def __str__(self):
        return self.text[:20]
