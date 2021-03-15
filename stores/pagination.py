# api-small-business/stores/pagination.py
from rest_framework.pagination import LimitOffsetPagination


class HeaderLimitOffsetPagination(LimitOffsetPagination):
    # Overrides the value assigned to the max_limit class attribute with 10
    max_limit = 10 