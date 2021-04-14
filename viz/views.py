from django.views.generic import TemplateView

class GaitVisualizationView(TemplateView):
    template_name = "viz/gait_visualization.html"
