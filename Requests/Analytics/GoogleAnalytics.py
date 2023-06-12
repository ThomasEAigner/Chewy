class GoogleAnalytics:
    requests_list = []

    @staticmethod
    def google_analytics_found(self, request):
        GoogleAnalytics.requests_list.append(request)

    @staticmethod
    def clear_requests(self):
        GoogleAnalytics.requests_list.clear()

    # Add list parsing items here
