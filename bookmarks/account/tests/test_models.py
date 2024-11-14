from account.models import Profile
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class ProfileModelTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.profile = Profile.objects.create(
            user=cls.user,
            date_of_birth='1996-12-11'
        )

    def test_verbose_name(self):
        field_verbose = {
            'user': 'User',
            'date_of_birth': 'Date of birth',
            'photo': 'Image'
        }
        for field, expected_value in field_verbose.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.profile._meta.get_field(field).verbose_name,
                    expected_value)

    def test_models_have_correct_object_names(self):
        profile = self.profile
        expected_object_name = f'Profile of {profile.user.username}'
        self.assertEqual(expected_object_name, str(profile))
