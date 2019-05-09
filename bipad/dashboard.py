from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard
from jet.utils import get_admin_site_name
from jet.dashboard.models import UserDashboardModule

from incident.models import Incident


class IndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Select Language'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('English'), '/en/admin/'],
                [_('Nepali'), '/ne/admin/']
            ],
            column=0,
            order=0
        ))
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('Return to site'), '/'],
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ],
            column=0,
            order=1
        ))
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('auth.*',),
            column=0,
            order=2
        ))
        self.children.append(modules.AppList(
            _('Administration'),
            models=('auth.*',),
            column=1,
            order=0
        ))
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            10,
            column=1,
            order=1
        ))
        self.children.append(FollowupIncidents(
            _('Incomplete incidents'),
            10,
            column=1,
            order=2
        ))

    def get_or_create_module_models(self, user):
        module_models = []

        i = 0

        for module in self.children:
            column = module.column if module.column is not None else i % self.columns
            order = module.order if module.order is not None else int(i / self.columns)

            obj, created = UserDashboardModule.objects.get_or_create(
                title=module.title,
                app_label=self.app_label,
                user=user.pk,
                module=module.fullname(),
                column=column,
                order=order,
                settings=module.dump_settings(),
                children=module.dump_children()
            )
            module_models.append(obj)
            i += 1

        return module_models

    def load_modules(self):
        module_models = self.get_or_create_module_models(self.context['request'].user)

        loaded_modules = []

        for module_model in module_models:
            module_cls = module_model.load_module()
            if module_cls is not None:
                module = module_cls(model=module_model, context=self.context)
                loaded_modules.append(module)

        self.modules = loaded_modules


class FollowupIncidents(modules.DashboardModule):
    title = _('Needs Followup')
    template = 'followup_incident.html'
    limit = 25
    include_list = None
    exclude_list = None
    user = None

    def __init__(self, title=None, limit=10, **kwargs):
        kwargs.update({'limit': limit})
        super().__init__(title, **kwargs)

    def settings_dict(self):
        return {
            'limit': self.limit,
            'include_list': self.include_list,
            'exclude_list': self.exclude_list,
            'user': self.user
        }

    def load_settings(self, settings):
        self.limit = settings.get('limit', self.limit)
        self.include_list = settings.get('include_list')
        self.exclude_list = settings.get('exclude_list')
        self.user = settings.get('user', None)

    def init_with_context(self, context):
        qs = Incident.objects.filter(
            need_followup=True,
        )

        self.children = qs[:int(self.limit)]
