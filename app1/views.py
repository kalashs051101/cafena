from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from .forms import *
# Create your views here.


def app1(request):
    return HttpResponse('this is app1')


def index(request):
    
    return render(request,'index.html')
      

  
    '''
    if(request.method=="POST"):
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        obj=registration_data.objects.create(name=name,age=age,email=email,pass1=pass1,pass2=pass2)
        obj.save()
        return redirect('dashboard')
    '''
#BUT DONT USE THIS METHOD BECAUSE DJANGO GIVES OWN USER METHOD WHICH HAVE ALREADY GIVEN DATA
    '''
    if(request.method=="POST"):
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if (pass1==pass2):
            obj=registration_data.objects.create(name=name,age=age,email=email)
            obj.save() 

            return redirect('dashboard')
            # return HttpResponse('okk')
        else:
            return HttpResponse('sorry, password not match')

    return render(request,'registration.html')
    '''

    #THUS WE USE THIS METHOD IN DJANGO -- make_pass
'''
def registration_page(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        # age=request.POST['age']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if(pass1==pass2):
            data=User.objects.create(username=name,email=email,password=make_password(pass1))
            data.save()
            return redirect('llogin')
            
            #print('working......')
            #return HttpResponse('okkk')
    return render(request,'index.html')


'''
def registration_page(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            # Check if the email is already in use
            if User.objects.filter(email=email).exists():
                return render(request, 'index.html', {'error': 'Email already exists. Please choose another email.'})
            
            # Create the user
            user = User.objects.create(username=name, email=email, password=make_password(pass1))
            user.save()
            return redirect('index')
        else:
            # error = 'Passwords do not match.'
            return HttpResponse('Passwords do not match')

            # return render(request, 'index.html', {'error':error})
    
    return render(request, 'index.html')





def llogin(request):
    if(request.method=="POST"):
        nname=request.POST['name']
        ppass1=request.POST['pass1']
        user=authenticate(username=nname,password=ppass1)  # (obj.name==name and obj.pass==pass)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'login.html')

    # return HttpResponse('this is registration_page')

def dashboard(request):
    all_data=User.objects.all()
    return render(request,'dashboard.html',{'all_data':all_data})


def delete_data(request,id):
    obj=User.objects.get(id=id)
    obj.delete()
    return redirect('dashboard')

def update_data(request,id):

    if(request.method=="POST"):
        name=request.POST['name']
        # age=request.POST['age']
        Email=request.POST['email']
        passs1=request.POST['pass1']
        passs2=request.POST['pass2']
        

        if passs1==passs2:
            User.objects.filter(id=id).update(username=name,email=Email,password=make_password(passs1))
            return redirect('index')
        else:
            return HttpResponse('password not correct')

    obj=User.objects.get(id=id)
    return render(request,'update.html',{'obj':obj})



    # logout(request)
    # return redirect('start_login')

    # return render(request,'login.html')
    # return HttpResponse('this is login')

#def newone(request):
 #   return render(request,'index.html')


def logoutt(request):
    logout(request)
    #return HttpResponse('this is logout')
    return render(request,'index.html')
     
'''
def forgot_p(request,name):
    data=User.objects.get(username=name)
    if request.method=="POST":
        uname=request.POST['nn']
        passwrd1=request.POST['P1']
        passwrd2=request.POST['P2']
        if uname==data.username:
            if passwrd1==passwrd2:
                User.set_password(passwrd1)

                return redirect('llogin')
            else:
                return HttpResponse('Password not match')
    return render(request,"forget.html")
        
'''
'''
def abcs(request):
    if request.method=="POST":
        name=request.POST['abc']
        return render(request,'forget.html',{'name':name})
'''



# Imaginary function to handle an uploaded file.


def upload_data(request,id):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        upload_model.objects.create(file=uploaded_file)
        return redirect('Blogg')
 
    return render(request, 'upload.html')
    # if request.method == 'POST':
    #     form = uploader_file_form(request.POST, request.FILES)
 
    #     if form.is_valid():
    #         form.save()
    #         return redirect('Blogg')
    # else:
    #     form = uploader_file_form()
    # return render(request, 'upload.html', {'form': form})


def Blogg(request):
    fileshow = upload_model.objects.all()
    return render(request, 'Blog.html',{'fileshow': fileshow})
    