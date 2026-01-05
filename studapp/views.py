from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from .models import usermodel


#def index(request):
   # return render(request,'base.html')

def enroll_student(request):
    if "user_id" not in request.session:
        return redirect('login')
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_students')
    else:
        form = StudentForm()
    return render(request, 'form.html', {'form': form})

#def show_students(request):
    #students = Student.objects.all()
    #return render(request, 'show.html', {'students': students})

def delete_student(request, id):
    student = Student.objects.filter(id=id).first()
    if student:
        student.delete()
    return redirect('show_students')

def edit_student(request, id):
    student = Student.objects.filter(id=id).first()
    if not student:
        return redirect('show_students')

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'form.html', {'form': form, 'student': student})

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            user=usermodel.objects.get(username=username,password=password)
            request.session["user_id"]=user.id
            return redirect('enroll_student')
        except usermodel.DoesNotExist:
         return render(request,'login.html',{'error': 'Invalid credentials'})
    return render(request,'login.html')

def show_students(request):
    if "user_id" not in request.session:
        return redirect("login")
    students=Student.objects.all()
    return render(request,'show.html',{'students':students})

def logout(request):
    request.session.flush()
    return redirect('login')

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if usermodel.objects.filter(username=username).exists():
            return render(request,'register.html',{'error':'user already exists'})
        usermodel.objects.create(username=username,password=password)
        return redirect('login')
    return render(request,'register.html')
        






# Create your views here.
