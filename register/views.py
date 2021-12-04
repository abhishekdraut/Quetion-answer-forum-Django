from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth,messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        user=auth.authenticate(username=username1,password=password1)
        print("user OBjects",user)
        if user is not None:
            auth.login(request, user)
            print("loged in")
            return redirect('home')

        else:
            print("wrong Cred!!")    

    return (render(request,'login.html'))

def logout(request):
    auth.logout(request)
    return redirect('home')
def home(request):
    return render(request,'home.html')


    
def register(request):
    if request.method == 'POST':
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        userame=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1==password2:
            if User.objects.filter(username=userame).exists():
                print("username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("usrname Taken")
                return redirect('register')
            elif userame =="":
                print('username field should not be empty')   
                return redirect('register')
            elif email =="":
                print('email field should not be empty')   
                return redirect('register')
            elif firstname =="":
                print('name fields should not be empty')   
                return redirect('register') 
            elif lastname =="":
                print('name fields should not be empty')   
                return redirect('register')       
                    
            else:    
                user=User.objects.create_user(username=userame,password=password1,first_name=firstname,last_name=lastname,email=email)
                user.save()
                print("user craeted")
                return redirect('login')




    return (render(request, 'register.html'))