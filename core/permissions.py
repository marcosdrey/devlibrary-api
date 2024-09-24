from rest_framework.permissions import BasePermission


class GlobalDefaultPermission(BasePermission):
    def has_permission(self, request, view):
        model_perm_codename = self.__get_model_perm_codename(
            method=request.method,
            view=view
        )
        if not model_perm_codename:
            return False
        return request.user.has_perm(model_perm_codename)

    def __get_model_perm_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_word(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_action_word(self, method):
        method_codenames = {
            'GET': 'view',
            'HEAD': 'view',
            'OPTIONS': 'view',
            'POST': 'add',
            'PATCH': 'change',
            'PUT': 'change',
            'DELETE': 'delete'
        }
        return method_codenames.get(method, '')
