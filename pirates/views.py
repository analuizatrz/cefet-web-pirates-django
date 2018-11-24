from django.shortcuts import render
from django.views import View
from django.db.models import F, ExpressionWrapper, DecimalField
from .models import Tesouro

class ListaTesourosView(View):
	def get(self, request):
		tesouros = Tesouro.objects\
					.annotate(\
						total=ExpressionWrapper(F('preco')*F('quantidade'),\
                        output_field=DecimalField(max_digits=10,\
                                                    decimal_places=2,\
                                                    blank=True)\
                                                )\
                    ).all()
		return render(request, 'lista_tesouros.html', {'tesouros': tesouros})