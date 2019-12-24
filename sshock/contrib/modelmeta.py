from django.db.models import Q
from sshock.contrib import get_master_user


def filter_queryset_visibility(request, qs):
    """
        Filters all Entrys with the correct Visibility settings
    :param request:  current Request
    :param qs: Queryset that should be filterd; Model must have LinkedToMeta and VisiblieToMeta
    :return queryset: Queryset with all matching data
    """
    user = request.user
    return qs.filter(Q(created_by__in=[user, get_master_user()]) | Q(organizational_visibileity=True, organization__in=[user.organization]) | Q(global_visibility=True) )