from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'code': 200,
            'meta': {
                'page': self.page.number,
                'per_page': self.page_size,
                'pages': self.page.paginator.num_pages,
                'count': self.page.paginator.count,
            },
            'data': data
        })
