from django.shortcuts import render,get_object_or_404
from .models import Journal
 # Create your views here.

def journals_all(request):
	#When you have to retreive the objects or contents from the database
	journals = Journal.objects.all().order_by('-timestamp')
	#journalss = Journal.objects.order_by('create_date')

	# When you have to pass data from frontend to backend that data is called context

	context={
		'title': 'All',
		'journals':journals
	}
	# When you have to display context back to user

	return render(request , "journals_all.html" , context)

def journals_by_id(request , input_id):
	journals  = get_object_or_404(Journal , id = input_id)

	context = {
		'title':'All',
		'journals':journals
	}

	return render(request , 'journals_by_id.html',context)