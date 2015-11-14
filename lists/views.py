from django.core.exceptions import ValidationError
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
	if Item.objects.filter(list_id=list_id).count()==0:	
		komen='yey, waktunya berlibur'
	elif Item.objects.filter(list_id=list_id).count()<5:
		komen='sibuk, tapi santai'
	else:
		komen='oh tidak'

	list_ = List.objects.get(id=list_id)
	error = None
	if request.method == 'POST':
		try:
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect('/lists/%d/' % (list_.id,))
		except ValidationError:
			error = "You can't have an empty list item"

	return render(request, 'list.html', {'list': list_, 'error': error, 'komen': komen})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect('/lists/%d/' % (list_.id,))

