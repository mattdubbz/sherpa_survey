from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from survey.models import CustomerSatisfactionSurvey as Survey


class SurveyPageTests(SimpleTestCase):

    def test_survey_page_status_code(self):
        response = self.client.get('survey/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('survey'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('survey'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'survey.html')


class CustomerSatisfactionSurveyTest(TestCase):
    def setUp(self):
        self.survey = Survey.objects.create(
            amenities_score=5,
            activities_scorey=5,
            room_score=5,
            atmosphere_score=5,
            staff_score=5,
            service_score=5,
            overall_score=5,
            improve_text='Good improvement text',
            comments='Good comments text'
        )

    def test_survey_content(self):
        self.assertEqual(f'{self.survey.amenities_score}', '5')
        self.assertEqual(f'{self.survey.improve_text}',
                         'Good improvement text')
        self.assertEqual(f'{self.survey.comments}', 'Good comments text')

    def test_survey_view(self):
        response = self.client.get(reverse('survey'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'How would you rate the amenities?')
        self.assertTemplateUsed(response, 'survey.html')

    def test_survey_create_view(self):
        response = self.client.post(reverse('survey'), {
            'amenities_score': 5,
            'activities_score': 5,
            'room_score': 5,
            'atmosphere_score': 5,
            'staff_score': 5,
            'service_score': 5,
            'overall_score': 5,
            'improve_text': 'Good improvement text',
            'comments': 'Good comments text'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Good improvement text')
        self.assertContains(response, 'Good comments text')
