from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')

	komen = ''
	if Item.objects.count()==0:
		komen='yey, waktunya berlibur'
	elif Item.objects.count()<5:
		komen='sibuk, tapi santai'
	else: 
		komen='oh tidak'	
	
	items = Item.objects.all()
	return render(request, 'home.html', {'komen': komen})

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})
