from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    page_size= 2
    page_query_param= 'page_size'