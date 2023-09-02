from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HTMXModalCreateView(CreateView):
    success_message = None
    form_title = None
    url_name = None
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.url_name:
            context['url'] = reverse_lazy(self.url_name)
        else:
            context['url'] = reverse_lazy(f'{self.model.__name__.lower()}s:create')
        
        if self.form_title:
            context['form_title'] = self.form_title
        else:
            context['form_title'] = f'Add {self.model.__name__}'
        
        return context
    
    
    def form_valid(self, form):
        if self.success_message:
            success_message = self.success_message
        else:
            success_message = 'Added {obj}'
        
        self.object = form.save()
        messages.success(self.request, success_message.format(obj=str(self.object)))
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': f'{self.model.__name__.lower()}-created'
            },
        )


class HTMXModalUpdateView(UpdateView):
    success_message = None
    form_title = None
    url_name = None
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        
        if self.url_name:
            context['url'] = reverse_lazy(self.url_name, args=(pk,))
        else:
            context['url'] = reverse_lazy(f'{self.model.__name__.lower()}s:update', args=(pk,))
        
        if self.form_title:
            context['form_title'] = self.form_title
        else:
            context['form_title'] = f'Update {self.model.__name__}'

        return context
    
    
    def form_valid(self, form):
        if self.success_message:
            success_message = self.success_message
        else:
            success_message = 'Updated {obj}'
        
        self.object = form.save()
        messages.success(self.request, success_message.format(obj=str(self.object)))
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': f'{self.model.__name__.lower()}-{self.kwargs.get("pk")}-updated'
            },
        )


class HTMXModalDeleteView(DeleteView):
    success_message = None
    form_title = None
    url_name = None
    form_body = None
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        
        if self.url_name:
            context['url'] = reverse_lazy(self.url_name, args=(pk,))
        else:
            context['url'] = reverse_lazy(f'{self.model.__name__.lower()}s:delete', args=(pk,))
        
        if self.form_title:
            context['form_title'] = self.form_title
        else:
            context['form_title'] = f'Delete {self.model.__name__}'
        
        if self.form_body:
            context['form_body'] = self.form_body
        else:
            context['form_body'] = f'Are you sure you want to delete this {self.model.__name__.lower()}?'
        
        return context
    
    
    def form_valid(self, form):
        if self.success_message:
            success_message = self.success_message
        else:
            success_message = 'Deleted {obj}'
        
        self.object.delete()
        messages.success(self.request, success_message.format(obj=str(self.object)))
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': f'{self.model.__name__.lower()}-deleted'
            }
        )