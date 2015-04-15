from django.test import TestCase
from django.contrib.auth.models import User
from model_mommy import mommy
from app.note.models import Note



class NoteTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='Ferdi', last_name='Ramdhon')

    def test_create_new_note(self):
        title = 'A new note'
        note = mommy.make(Note, title=title, user=self.user)
        self.assertEqual(note.__unicode__(), title)
