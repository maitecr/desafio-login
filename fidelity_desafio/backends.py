from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                raise ValueError("Senha inválida")
        except ObjectDoesNotExist:
            raise ValueError("E-mail inexistente")
        except ValueError as e:
            raise e