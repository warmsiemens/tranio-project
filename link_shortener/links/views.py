from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.views.generic import ListView
from .forms import AddLinkForm
from .models import Link


class AddLinkView(FormView):
    form_class = AddLinkForm
    template_name = 'links/link_add.html'

    def form_valid(self, form):
        link, created = Link.objects.get_or_create(full_link=form.cleaned_data['full_link'])
        shortened_link = link.shortened_link
        return self.render_to_response(
            self.get_context_data(form=form, shortened_link=shortened_link)
        )


class RedirectLinkView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        shortened_link = kwargs['shortened_link']
        url_obj = get_object_or_404(Link, shortened_link=shortened_link)

        url_obj.count_of_clicks += 1
        url_obj.save(update_fields=['count_of_clicks'])

        return url_obj.full_link


class StatsView(ListView):
    model = Link
    template_name = 'links/link_stats.html'
    context_object_name = "links"
