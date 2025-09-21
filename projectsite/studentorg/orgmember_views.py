from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import OrgMember
from django.urls import reverse_lazy
from .forms import OrganizationForm
from django.db.models import Q

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmembers'
    template_name = 'orgmem_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(student__lastname__icontains=query) |
                Q(student__firstname__icontains=query) |
                Q(student__middlename__icontains=query) |
                Q(organization__name__icontains=query)
            )
        return qs

class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'orgmem_form.html'
    success_url = reverse_lazy('organization-member-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'orgmem_form.html'
    success_url = reverse_lazy('organization-member-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmem_del.html'
    success_url = reverse_lazy('organization-member-list')
