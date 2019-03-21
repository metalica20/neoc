from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard
from jet.utils import get_admin_site_name


class IndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        self.available_children.append(modules.LinkList)
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
            order=0
        ))
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('auth.*',),
            column=0,
            order=0
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
