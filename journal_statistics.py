"""A mini django model ...."""

from django.db import models
from django.utils import timezone


class Hit(models.Model):

	PAGEVIEW = 'PV'
	DOWNLOAD = 'DL'
	ACTIONS = (
		(PAGEVIEW, 'Article web page view'),
		(DOWNLOAD, 'Article download'),
	)

	publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)
	ip_address = models.GenericIPAddressField()
	user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL, null=True, blank=True)
	action = models.CharField(max_length=2, choices=ACTIONS)


class Publication(models.Model):

	title = models.CharField(max_length=200)
	journal = models.ForeignKey('Journal', on_delete=models.CASCADE)


class Journal(models.Model):
	"""A Journal Model"""
	title = models.CharField(max_length=200)

	def get_journal_statistics(self):
		"""GEts statistics on journal"""
		page_view_hits = Hit.objects.filter(publication__journal=self, action='PV')
		download_hits = Hit.objects.filter(publication__journal=self, action='DL')
		return {
			f'{self.id}': {
				'total_views': page_view_hits,
				'total_downloads': download_hits
			}
		}
