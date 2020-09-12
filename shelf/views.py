from django.shortcuts import render
from .models import Book
from rest_framework.viewsets import ModelViewSet
# from .serializer import BookSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework import viewsets

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# -------------------ViewSets and its outputs-------------------

# viewsets.ViewSet  --  only api-token-auth
# viewsets.ReadOnlyModelViewSet -- only list and retrieve
# viewsets.GenericViewSet -- only get_queryset() and get_object() --- Example Given Below
# viewsets.ModelViewSet -- all methods and get_queryset() and get_object()


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    permission_classes = (IsAuthenticated,) 
    print(permission_classes)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

from .serializer import BookSerializer
# from rest_framework.decorators import action
class BookOperations(viewsets.ModelViewSet):
    # pass
    # lookup_field = 'book_qty'    # u can change the lookup_field to any field of model.
    # lookup_value_regex = '[0-9]{4}'   # regx for better url
    queryset = Book.objects.all()
    # print('-----------views------------------------')
    # print(queryset)
    # print('-----------------------------------')
    serializer_class = BookSerializer
    # print(serializer_class.__dict__)
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, *args, **kwargs):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(args)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@')
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


#detail = False will not ask any input. This function will give all the entries of books.
    # @action(methods=['get'], detail=False, url_path='extra_action_get_all_url', url_name='extra_action_get_all_url')
    # def extra_action(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


# ---------------For generating pdf------

write_to_pdf = '''Users often choose poor passwords. To help mitigate this problem,
                  Django offers pluggable password validation. 
                  You can configure multiple password validators at 
                    the same time. A few validators are included in Django,'''

def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    # p.drawAlignedString(text=write_to_pdf,x=60,y=820)

    p.drawCentredString(text=write_to_pdf, x=60, y=820,)


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


# ----------------Extra ViewSet for extra root-------------------

class Extra_api_root(viewsets.ModelViewSet):
    model = Book
    queryset = Book.objects.all()
    # serializer_class = BookSerializer


# url_path = books/(?P<pk>[^/.]+)/extra_action_url/$' [name='Books-extra-action']>


from rest_framework import mixins

# class CreateListViewSet(mixins.CreateModelMixin,
#                         mixins.ListModelMixin,
#                         viewsets.GenericViewSet):
#     queryset =
#     serializer_class =
#     permission_classes =
#     authentication_classes =
#     model =
#
#     def get_queryset(self):
#         pass
#
#     def get_object(self):
#         pass

# def hello(req):
#     return HttpResponse('AAAAA')
#



# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'
#
#     @action(detail=True)
#     def group_names(self, request, pk=None):
#         """
#         Returns a list of all the group names that the given
#         user belongs to.
#         """
#         user = self.get_object()
#         groups = user.groups.all()
#         return Response([group.name for group in groups])


