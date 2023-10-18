#from django.views.generic import TemplateView
from django.views.generic import TemplateView
from birthday.models import Birthday

class HomePage(TemplateView):
    # В атрибуте template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница.
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['total_count'] = Birthday.objects.count()
        return context
    