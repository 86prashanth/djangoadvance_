# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 
from . import models
from django.template.loader import render_to_string

#Creating a class based view
# class GeneratePdf(View):
#      def get(self, request, *args, **kwargs):
         
#         # getting the template
#         pdf = html_to_pdf('invoice/result.html')
         
#          # rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')
    
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        data = models.Employees.objects.all().order_by('first_name')
        open('temp.html', "w").write(render_to_string('invoice/result.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('invoice/result4.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')