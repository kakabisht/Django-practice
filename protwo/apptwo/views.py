from django.shortcuts import render
from apptwo.forms import NewUserForm
# Create your views here.


def index(request):
    return render(request,'apptwo/index.html')
        
def help(request):
    helpdict={'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html',context=helpdict)

def users(request):
    form=NewUserForm()

    if request.method == "POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("Saved")
            return index(request)

        else:
            print("Form is Invalid")
    
    return render(request,'apptwo/users.html',{'form':form})
        
