from apscheduler.schedulers.background import BackgroundScheduler
from .models import Post


def start():
    """Background task to set all upvotes to 0 each 1440 minutes (1 day)"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(Post.erase_upvotes, "interval", minutes=1440)
    scheduler.start()
