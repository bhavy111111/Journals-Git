from django.shortcuts import render,get_object_or_404,reverse,redirect
from .models import Journal
from .forms import JournalForm
from django.utils import timezone
 # Create your views here.

def journals_all(request):
	#When you have to retreive the objects or contents from the database
	#journals = Journal.objects.all().order_by('-timestamp')
	journals = Journal.objects.filter(publish__lte = timezone.now())
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

def journal_new(request):
	form = JournalForm(request.POST or None , request.FILES or None)
	#Will check whether is form valid or not
	if form.is_valid():
		#commit = False , wont save directly into db but will save into instance object
		instance = form.save(commit=False)
		#Will save instance object permanently to database
		instance.save()
		return redirect('Journals:all')
	context={
		'title':'New Form',
		'form': form
	}

	return render(request , 'journal_new.html',context)

def journals_edit(request,input_id):
	journal = get_object_or_404(Journal, id = input_id)
	form = JournalForm(request.POST or None , request.FILES or None , instance = journal)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("Journals:byId" ,input_id= instance.id)

	context={
			"title":"Edit Journal",
			"form":form
	}

	return render(request , 'journal_edit.html' , context)

