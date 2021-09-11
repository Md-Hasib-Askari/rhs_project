from dashboard.models import HeaderInfo, SideBarBanner, UsefulLink
from feed_post.models import NoticeBoard

# Header Data for all views
header_data = HeaderInfo.objects.all().last()

# Banner Image
sidebar_banner = SideBarBanner.objects.all().last()

# Notice Board
notices = NoticeBoard.objects.all()[::-1]
notices = notices[:5]

# Useful link
links = UsefulLink.objects.all()

context = {
    'header_data': header_data,
    'sidebar_banner': sidebar_banner, 
    'notices': notices,
    'links': links, 
}