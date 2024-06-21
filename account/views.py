from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


@permission_classes([IsAuthenticatedOrReadOnly])
@authentication_classes(
    [
        JWTAuthentication,
    ]
)
class Verification(APIView):

    def get(
        self,
        request: Request,
        *args,
    ) -> Response:
        return Response(
            request,
            "Authentication is now valid!",
        )
