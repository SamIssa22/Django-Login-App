from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestap):
        return {
            text_type(user.pk) + text_type(timestap)

        }


generate_token = TokenGenerator()
