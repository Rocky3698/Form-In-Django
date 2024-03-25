from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST.get('userName')
        email=request.POST.get('email')
        return render(request,'indexb.html',{'name':name,'email':email})
    return render(request,'indexb.html')