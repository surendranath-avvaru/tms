from django.contrib.auth.models import User

from django.core.exceptions import PermissionDenied

def users_have_permission(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.has_perm('customers.can_update_authors'):
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrapper