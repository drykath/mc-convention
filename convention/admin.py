from django.contrib import admin

from . import get_convention_model

Convention = get_convention_model()


class ConventionListFilter(admin.SimpleListFilter):
    """
    Specialized admin list filter for models with links to the
    Convention object. Assumes the name of the field is 'convention',
    which is probably a pretty safe assumption for most of the MCFC
    apps.

    By default the "current" convention is selected, and the filter
    allows the admin to select between conventions shown. Which is to
    say it doesn't have an "All" option anymore. Fix that if needed.
    """
    title = 'Convention'
    parameter_name = 'convention'

    def lookups(self, request, model_admin):
        queryset = Convention.objects.all()
        return queryset.values_list('pk', 'name').order_by('pk')

    def choices(self, changelist):
        curr_con_pk = Convention.objects.current().pk
        for lookup, title in self.lookup_choices:
            yield {
                'selected': (self.value() == str(lookup)) or (self.value() is None and lookup == curr_con_pk),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(convention=self.value())
        else:
            return queryset.filter(convention=Convention.objects.current())


admin.site.register(Convention)
