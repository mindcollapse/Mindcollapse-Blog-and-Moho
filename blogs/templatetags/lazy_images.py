
from django import template

register = template.Library()

def lazy_images(value):
	for match in re.finditer('<img.*?class="lazy".*?>', value):
		replace_from = match.group(0)
		replace_to = match.group(0).replace('src=', 'src="/static/blog/grey.gif" data-original=')
		value = value.replace(replace_from, replace_to)

	return value

register.filter('lazy_images', lazy_images)
