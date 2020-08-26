# This file is created by Mr. Whitehat- 30 July 2020

from django.http import HttpResponse
from django.shortcuts import render
# def index(request):																# Personal_Navigator 										
# 	return HttpResponse('''<strong>Hello</strong><h1> Mr. Whitehat and</h1><a href="https://www.google.com"> Google.com </a>''')	

# Pipe_Line Laying:	
def index(request):
	return render(request,'index.html')#,param)

def analyze(request):
	djtext = request.POST.get('text',"")
	removepun = request.POST.get('removepunc','off')
	uppercase = request.POST.get('uppercase','off')
	lowercase = request.POST.get('lowercase','off')
	NewLineRemover = request.POST.get('NewLineRemover','off')
	extraspaceremover = request.POST.get('extraspaceremover','off')
	removenumber = request.POST.get('removenumber', 'off')
	charactorcounter = request.POST.get('charactorcounter','off')

	if djtext == "":
		params = {'heading': 'Error :( ', 'Success': 'Sorry', 'message': 'Text is not entered', 'color': 'danger'}
		return render(request, 'analyze.html', params)
		# goto: display()

	if uppercase == 'on' and lowercase == 'on':
		params = {'heading': 'Error :( ', 'Success': 'Sorry',
				  'message': 'Upper Case and Lower Case cannot perform together', 'color': 'danger'}
		return render(request, 'analyze.html', params)

	if removepun == 'on':
		punctuations='''`~!@#$%^&*()-_\|[]{};:'",<>./?'''
		analyzed=""
		for char in djtext:
			if char not in punctuations:
				analyzed += char
		params={'analyzed_text':analyzed,'heading':'Your analyzed text',
				'Success':'Success','message':'Your text has been analyzed','color':'success'}
		djtext = analyzed

	if uppercase=='on':
		analyzed=''
		for char in djtext:
			analyzed+=char.upper()

		params = {'analyzed_text': analyzed, 'heading': 'Your analyzed text',
					  'Success': 'Success', 'message': 'Your text has been analyzed', 'color': 'success'}
		djtext = analyzed

	if lowercase=='on':
		analyzed=''
		for char in djtext:
			analyzed+=char.lower()
		params = {'analyzed_text': analyzed, 'heading': 'Your analyzed text',
				  'Success': 'Success', 'message': 'Your text has been analyzed', 'color': 'success'}
		djtext = analyzed

	if NewLineRemover=='on':
		analyzed=""
		for char in djtext:
			if char != '\n' and char !='\r':
				analyzed+=char

		params = {'analyzed_text': analyzed, 'heading': 'Your analyzed text',
				 'Success': 'Success', 'message': 'Your text has been analyzed', 'color': 'success'}
		djtext = analyzed

	if extraspaceremover=='on':
		analyzed=""
		count=0
		for char in djtext:
			count+=1
		for index, char in enumerate(djtext):
			if not(index+1< count and djtext[index]==" " and djtext[index+1]==" "):
				analyzed+= char

		params = {'analyzed_text': analyzed, 'heading': 'Your analyzed text',
						  'Success': 'Success', 'message': 'Your text has been analyzed', 'color': 'success'}
		djtext = analyzed

	if removenumber == 'on':
		string = djtext
		numbers = '''1234567890'''
		for digit in string:
			if digit in numbers:
				string = string.replace(digit, "")
		print(string)

		analyzed = ""
		count = 0
		for char in string:
			count += 1
		for index, char in enumerate(string):
			if not (index + 1 < count and string[index] == " " and string[index + 1] == " "):
				analyzed += char

		print(analyzed)
		params = {'analyzed_text': analyzed, 'heading': 'Your analyzed text',
				  'Success': 'Success', 'message': 'Your text has been analyzed', 'color': 'success'}
		djtext = analyzed


	if charactorcounter=='on':
		count = 0
		for char in djtext:
			if(char =='\n'):
				count-=0
			else:
				count+=1

		params = {'pr':count,'str':'Number of Charactors: ','analyzed_text':djtext,
				  'heading': 'Your analyzed text','Success': 'Success',
				  'message': 'Your text has been analyzed', 'color': 'success'}
		# djtext = analyzed


	if removepun !='on'and uppercase !='on' and lowercase !='on' and NewLineRemover !='on' and extraspaceremover !='on' and removenumber != 'on' and charactorcounter !='on' :
		params={'heading':'Error :( ','Success':'Sorry','message':'Please select an operation','color':'danger'}

	return render(request, 'analyze.html', params)

def display(request):
	return render(request,'analyze.html',params)

def contact(request):
	return render(request,'contact.html')

def about(request):
	return render(request,'about.html')
