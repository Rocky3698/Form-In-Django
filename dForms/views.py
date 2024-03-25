from django.shortcuts import render
from dForms.forms import contactForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            # file=form.cleaned_data['file']
            # with open('./dForms/upload/' + file.name, 'wb+') as desination:
            #     for chunk in file.chunks():
            #         desination.write(chunk)
            print(form.cleaned_data)
            
    else:
        form=contactForm()
    return render(request,'index.html',{'form':form})
