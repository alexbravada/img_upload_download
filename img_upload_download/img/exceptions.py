class NotEvenPagination(Exception):
    def __str__(self):
        return "Pagination count must be a even number"
