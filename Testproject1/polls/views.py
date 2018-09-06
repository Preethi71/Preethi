from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	l = []
	if request.method=='GET':
		# return render(request,"home1.html")
		return render(request,"home2.html")
	if request.method=='POST':
		# l.append(request.POST.get("Title"))
		# l.append(request.POST.get("Firstname"))
		# l.append(request.POST.get("Lastname"))
		# l.append(request.POST.get("Phonenumber"))
		# l.append(request.POST.get("Email id"))
		# l.append(request.POST.get("DOB"))
		# l.append(request.POST.get("Address"))
		# print(l)
		# data = {}
		# data.update({'Title1':l[0]})
		# data.update({'Firstname':l[1]})
		# data.update({'Lastname':l[2]})
		# data.update({'Phonenumber':l[3]})
		# data.update({'Emailid':l[4]})
		# data.update({'Dob':l[5]})
		# data.update({'Address':l[6]})

		# if (l[0]=='' and l[1]=='' and l[2]=='' and l[3]=='' and l[4]=='' and l[5]=='' and l[6]):
		# 	return render(request,'home1.html',{'title1':'*please enter the title','firstname':'*please enter firstname','lastname':'*please enter lastname','phonenumber':'*please enter phonenumber','emailid':'*please enter emailid','address':'*please enter  address'})
		# if (l[0]==''):
		# 	data['title1'] = ('*please enter the title')
		# if (l[1]==''):
		# 	data['firstname'] = ('*please enter the firstname')
		# if (l[2]==''):
		# 	data['lastname'] = ('*please enter the lastname')
		# if (l[3]==''):
		# 	data['phonenumber'] = ('*please enter the phonenumber')
		# if (l[4]==''):
		# 	data['emailid'] = ('*please enter the Email id')
		# if (l[5]==''):
		# 	data['dob'] = ('*please enter the DOB')	
		# if (l[6]==''):
		# 	data['address'] = ('*please enter the address')		
		# elif (l[0]!='' and l[1]!='' and l[2]!='' and l[3]!='' and l[4]!='' and l[5]!='' and l[6]!=''):
		# 	# student.objects.create(s_title=l[0],s_Fname = l[1], s_Lname = l[2], s_pno=l[3], s_emailid=l[4], s_dob=l[5],s_addr=l[6]) 
		# 	return HttpResponse("form submitted succesfully ")
		# else:
		# 	return HttpResponse("unable to submit the form")
		return render(request,'home2.html')
	