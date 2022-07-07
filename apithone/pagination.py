from rest_framework.pagination import CursorPagination

class MyPagination(CursorPagination):
    page_size = 2
    page_size_query_param = 'page'
    max_page_size = 9
    ordering = 'artist'
