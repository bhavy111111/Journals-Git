from django import forms

from .models import Journal
from django.utils import timezone
class JournalForm(forms.ModelForm):
	publish  = forms.CharField(widget = forms.SelectDateWidget , initial = timezone.now)

	class Meta:
		model = Journal
		fields=(
				'title',
				'text_field',
				'image',
				'publish'
				)