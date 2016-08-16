from django.db import models


class BlogPost(models.Model):
    description = models.TextField()
    who_created = models.CharField(max_length=35)
    when_created = models.DateTimeField(auto_now_add=True)
    who_updated = models.CharField(max_length=35)
    when_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ("{}.  {} - {}.  {} - {}.".format(self.description, self.who_created, self.who_updated, self.who_updated, self.when_updated))

    #
    # rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # timestamp = models.DateTimeField('date rated')
    #
