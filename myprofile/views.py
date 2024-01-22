from django.shortcuts import render
from myprofile import models
from myprofile.models import Contact
from django.contrib import messages
# Create your views here.


def contact(request):
    if request.method=="POST":
      print('post')
      name=request.POST.get('name')
      email=request.POST.get('email')
      content=request.POST.get('content')
      number=request.POST.get('number')
      print(name,email,number,content)

      if len(name)>1 and len(name)<38:
        pass
      else:
        messages.error(request,'lenght of name shoud be greater then 2 and less then 30 words')
        return render(request,'home.html')
    
      if len(email)>1 and len(email)<38:
        pass
      else:
        messages.error(request,'Invalid email try again')
        return render(request,'home.html')
    
      if len(number)>1 and len(name)<10:
        pass
      else:
        messages.error(request,'Invalid Number try Again')
        return render(request,'home.html')
      ins=models.Contact(name=name,email=email,content=content,number=number)
      ins.save()
      messages.success(request,'thank you for contacting me ||your msg have been saved ')
      print("data has beem saved to database")
      print("te request is no pass")
    
    return render(request,'home.html')
    
    