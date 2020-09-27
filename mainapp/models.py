from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    """DB model for table 'Post'"""

    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["creation_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns absolute url for each instance of 'Post'"""
        return reverse("post", kwargs={"pk": self.pk})

    @classmethod
    def erase_upvotes(cls):
        """Sets upvotes to 0 for all instances of 'Post'"""
        for post in cls.objects.all():
            post.amount_of_upvotes = 0
            post.save()


class Comment(models.Model):
    """DB model for table 'Comment'"""

    author_name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    post_pk = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["creation_date"]

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        """Returns absolute url for each instance of 'Comment'"""
        return reverse("comment", kwargs={"pk": self.pk})
