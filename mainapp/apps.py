from django.apps import AppConfig


class MainappConfig(AppConfig):
    name = "mainapp"

    def ready(self):
        """
        Initialization of a background task to set all upvotes to 0
        each 1440 minutes (1 day)
        """
        from . import updater

        updater.start()
