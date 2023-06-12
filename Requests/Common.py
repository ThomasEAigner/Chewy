#Requests would be where all of the checks for api requests made by the GUI would be found.  I have common here to
#process the requests as the come in and then pass them to the right script

from playwright.sync_api import sync_playwright
import Requests.Analytics.GoogleAnalytics as Google
import Requests.Analytics.Segment as Segment

GoogleAnalyticsURL = 'https://www.google-analytics.com/collect'
SegmentURL = 'https://sioa.chewy.com'


class CommonAnalytics:
    @staticmethod
    def request_process(request):
        if request.url.find(GoogleAnalyticsURL) > -1:
            Google.google_analytics_found(request)
        if request.url.find(SegmentURL) > -1:
            Segment.segment_analytics_found(request)


