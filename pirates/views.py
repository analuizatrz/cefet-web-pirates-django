from django.shortcuts import render
from django.views import View
from .models import Tesouro

class ListaTesourosView(View):
	def get(self, request):
		return render(request, 'lista_tesouros.html', None)