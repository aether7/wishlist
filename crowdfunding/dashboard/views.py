from django.views.generic import TemplateView,ListView
from deseos.models import Lista

class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self,**kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class MisProyectosView(ListView):
    model = Lista
    template_name = "mis_proyectos.html"

    def get_context_data(self,**kwargs):
        context = super(MisProyectosView, self).get_context_data(**kwargs)
        context["mis_proyectos"] = self.model.objects.all()
        return context

class MiPerfilView(TemplateView):
    template_name = "mi_perfil.html"

dashboard = DashboardView.as_view()
mis_proyectos = MisProyectosView.as_view()
mi_perfil = MiPerfilView.as_view()
