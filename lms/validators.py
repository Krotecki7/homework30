from rest_framework.serializers import ValidationError

good_link = "https://www.youtube.com/"


def validate_link(value):
    if good_link not in value:
        raise ValidationError("Ваша ссылка является невалидной!")
