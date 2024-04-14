from django.contrib import messages

class FormErrorMessageMixin:
    def form_invalid(self, form):
        messages.error(self.request, 'Form submission failed. Please correct the errors below.', extra_tags='error')
        return super().form_invalid(form)