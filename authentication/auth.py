from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


def require_login(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise AuthenticationFailed("User is not authenticated")
        return view_func(request, *args, **kwargs)

    return wrapper


def require_token_auth(view_func):
    def wrapper(request, *args, **kwargs):
        token_key = request.GET.get("token")  # Extract token from query string

        try:
            token = Token.objects.get(key=token_key)  # Retrieve token object
            user, _ = TokenAuthentication().authenticate_credentials(
                token_key
            )  # Authenticate user
        except (Token.DoesNotExist, AuthenticationFailed):
            raise AuthenticationFailed()  # Raise exception if authentication fails

        if user:
            request.user = user  # Set user in request object
            return view_func(
                request, *args, **kwargs
            )  # Call the original view function
        else:
            raise AuthenticationFailed()  # Raise exception if user is not authenticated

    return wrapper
