from django.template.loader import render_to_string

class Helper:
    @staticmethod
    def render_to_string(template_name, context=None, request=None, using=None) -> str:
        return render_to_string(template_name, context, request, using)