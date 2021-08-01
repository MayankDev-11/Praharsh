from django.shortcuts import render, HttpResponse
from core.models import Job,JobInfo,applicant

def services(request):
    return render(request,'pages/services.html')
    
def about(request):
    return render(request,'pages/about.html')

def jobs(request):
    jobs = Job.objects.order_by('-pub_date') 
    data = {'jobs': jobs}
    return render(request,'pages/jobs.html',data)

def jobPage(request,slug):
    job = Job.objects.get(slug=slug)
    jobInfo = JobInfo.objects.get(job=job)

    context = {
        'job':job,
        'jobInfo':jobInfo
        }
    return render(request,'pages/job-page.html',context)

def applyPage(request,slug):
    job = Job.objects.get(slug=slug)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        city = request.POST['city']
        description = request.POST['description']
        image = request.POST['image']
        experience = request.POST['experience']
        
        apply = applicant(first_name=first_name,last_name=last_name,mobile=phone,email=email,city=city,description=description,resume=image,experience=experience,job=job)
        apply.save()

    context = {
        'job':job
    }
    return render(request,'pages/apply.html',context)