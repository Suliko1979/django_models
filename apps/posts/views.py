from django.shortcuts import render

# Create your views here.
def post_detail(request):

    return render(request=request, template_name='pages/post_detail.html'),