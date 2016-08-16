from django.db import models


class BlogPost(models.Model):
    description = models.TextArea()
    who_created = models.CharField(max_length=35)
    when_created = models.DateField()
    who_updated = models.CharField(max_length=35)
    when_updated = models.DateField()

    def __str__(self):
        return ("{}.  {} - {}.  {} - {}.".format(self.description, self.who_created, self.who_updated, self.who_updated, self.when_updated))

    #
    # rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # timestamp = models.DateTimeField('date rated')
    #
