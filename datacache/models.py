from django.db import models

# Create your models here.

class LQFB(models.Model):

	name = models.CharField(ax_length=255)
	issueCreated = models.DateField()
	issueHalfFrozen = models.DateField()
	currentDraftContent = models.TextField()
	agreed = models.BooleanField()
	issueVoteNow = models.IntegerField()
	satisfiedInformedSupporterCount = models.IntegerField()
	positive_votes = models.IntegerField()
	rank = models.IntegerField()
	issueState = models.CharField(max_length=255)
	currentDraftCreated = models.DateField()

    class Meta:
        verbose_name = _('LQFB')
        verbose_name_plural = _('LQFBs')

    def __unicode__(self):
        pass
    