from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime

from .models import Question


def create_question(questionText, days):
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question(questionText=questionText, pubDate=time)
    question.save()
    return question


class QuestionModelTest(TestCase):
    # when a future question created, should return false.
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pubDate=time)
        self.assertIs(future_question.was_published_recently(), False)

    # when a old question created, it should return false.
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1)
        old_question = Question(pubDate=time)
        self.assertIs(old_question.was_published_recently(), False)

    # when a new question was created within 1 day, method was_published_recently should return true.
    def test_was_published_recently_with_new_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        new_question = Question(pubDate=time)
        self.assertIs(new_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    # if no questions, some messages should show up.
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # the index view only shows questions of past.
    def test_only_show_past_question(self):
        create_question(questionText='Past question.', days=-30)
        create_question(questionText='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])


class QuestionDetailViewTests(TestCase):
    # for questions in future, client should'nt access them.
    def test_future_question(self):
        future_question = create_question(questionText='Future question.', days=30)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # for a question published in the past, client can see it.
    def test_past_question(self):
        past_question = create_question(questionText='Past question', days=-30)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.questionText)


class QuestionResultsViewTests(TestCase):
    # check the server connection is ok.
    def test_url_connection(self):
        question = create_question('Question Results', days=-25)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class QuestionVoteViewTests(TestCase):
    # check the server connection is ok.
    def test_url_connection(self):
        question = create_question('Question Results', days=-25)
        url = reverse('polls:vote', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
