from rest_framework.permissions import BasePermission
from items_app.requesters.authrequester import AuthRequester
from items_app.requesters.requester import Requester

# просматривать информацию обо всех пользователях, удалять может только админ
# просматривать информацию о конкретном пользователе может он сам и админ

class BaseAuthPermission(BasePermission):
    def _get_token_from_request(self, request):
        return Requester().get_token_from_request(request)


class CustomerAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        r = AuthRequester()
        response, status_code = r.get_user_info(r.get_token_from_request(request))
        auth_json = r.get_data_from_response(response)
        print(auth_json)

        return int(view.kwargs[view.lookup_url_kwarg]) == auth_json['id'] or auth_json['is_superuser']


class IsSuperuser(BaseAuthPermission):
    def has_permission(self, request, view):
        token = self._get_token_from_request(request)
        if token is None:
            return False
        return AuthRequester().is_superuser(token)


class IsAuthenticated(BaseAuthPermission):
    def has_permission(self, request, view):
        token = self._get_token_from_request(request)
        print()
        if token is None:
            return False
        return AuthRequester().is_token_valid(token)[1]


class IsAppTokenCorrect(BaseAuthPermission):
    def has_permission(self, request, view):
        token = self._get_token_from_request(request)
        if token is None:
            return False
        view.app_access_token = token
        return AuthRequester().app_verify_token(token)[1]
