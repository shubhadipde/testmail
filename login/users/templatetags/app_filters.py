from django import template
from users.models import UserInfo

register = template.Library()

@register.filter(name = 'experiment')
def experiment(value):
	return value.title()


@register.filter(name = 'display_image')
def display_image(value):
	img = UserInfo.objects.get(email=value)
	return img.picture