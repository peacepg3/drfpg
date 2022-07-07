from datetime import datetime
from rest_framework.pagination import PageNumberPagination

class serialobj():
    def __init__(self,name,email,date=None):
        self.name = name
        self.email = email
        self.date = date or datetime.now()

class PaginationView(PageNumberPagination):
    page_size = 3
    max_page_size = 9
    page_size_query_param = 'pg_page'

