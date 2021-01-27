from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginationReview(PageNumberPagination):

    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):

        return Response({
            'links': {
                        'next': self.get_next_link(),
                        'previous': self.get_previous_link()
                        },
            'count_reviews': self.page.paginator.count,
            'count_items_page': self.page_size,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'result': data,
        })
