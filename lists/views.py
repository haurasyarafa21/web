from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
	komen='yey, waktunya berlibur'
#	if Item.objects.count()==0:
#		komen='yey, waktunya berlibur'
#	elif Item.objects.count()<5:
#		komen='sibuk, tapi santai'
#	else: 
#		komen='oh tidak'	
	return render(request, 'home.html', {'komen': komen}
	)

def view_list(request, list_id):
#	komen= Item.objects.get(id=list_id)
	if Item.objects.filter(list_id=list_id).count()==0:	
		komen='yey, waktunya berlibur'
	elif Item.objects.filter(list_id=list_id).count()<5:
		komen='sibuk, tapi santai'
	else:
		komen='oh tidak'

	list_ = List.objects.get(id=list_id)
#	comment = Item.objects.get(id=list_id)
	return render(request, 'list.html', {'list': list_, 'komen': komen})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
