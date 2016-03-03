from django.db import models

"""
Model holding the question with a set of answers. One can be the accepted answer.
"""
class Question(models.Model):
    text = models.TextField(max_length=1000)
    accepted_answer = models.ForeignKey("Answer", null=True, blank=True, related_name="+")

    """
    Extra validation of current model instance.
    """
    def clean(self):
        if self.accepted_answer.question.pk is not self.pk:
            raise ValidationError("Accepted answer does not answer this question")
    """
    Returns true if one of all answers is acccepted, false otherwise.
    """
    @property
    def has_accepted_answer(self):
        return self.accepted_answer is not None

    """
    Returns a list of all questions without accepted answers.
    """
    @classmethod
    def get_unanswered_questions(cls):
        return cls.objects.filter(accepted_answer__isnull=True)

    def __str__(self):
        return self.text[:20]

"""
Model holding the answer to a corresponding question.
"""
class Answer(models.Model):
    text = models.TextField(max_length=1000)
    question = models.ForeignKey("Question")

    """
    Returns true if this answer is marked as accepted, false otherwise.
    """
    def _get_accepted(self):
        return self.question.has_accepted_answer and self.question.accepted_answer.pk is self.pk

    """
    Change this answers accepted state.
    """
    def _set_accepted(self, val):
        self.question.accepted_answer = self if val else None

    """
    Combined getter and setter to a property.
    """
    is_accepted = property(_get_accepted, _set_accepted)

    def __str__(self):
        return self.text[:20]
