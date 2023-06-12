class Segment:
    requests_list = []

    @staticmethod
    def segment_found(self, request):
        Segment.requests_list.append(request)

    @staticmethod
    def clear_requests(self):
        Segment.requests_list.clear()

    # Add list parsing items here
