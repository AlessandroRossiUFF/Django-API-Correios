from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem, TodoCep

import xml.etree.ElementTree as ET
import requests

first_time = True

# Create your views here.
def todoView(request):
  global first_time
  all_todo_items = TodoItem.objects.all()
  if (first_time):
     # new_item = TodoItem(content = "build a cool app on replit.com")
     # new_item.save()
     # novo_item = TodoCep(content = "risos")
     # new_item.save()
      first_time = False
  return render(request, 'index.html', 
  {'all_items': all_todo_items})

def cepView(request):
  global first_time
  all_todo_ceps = TodoCep.objects.all()
  if (first_time):
     # new_item = TodoItem(content = "build a cool app on replit.com")
     # new_item.save()
      novo_item = TodoCep(content = "risos")
      novo_item.save()
      first_time = False
  return render(request, 'index.html', 
  {'all_ceps': all_todo_ceps})

def addTodo(request):

  response = requests.get('https://viacep.com.br/ws/{}/json/'.format(28920046))  #28920046
  dados_cep = response.json()
  dados_cep['logradouro']  

  cep = request.POST['contents']

  resp = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?nCdEmpresa=08082650&sDsSenha=564321&sCepOrigem=70002900&sCepDestino={}&nVlPeso=1&nCdFormato=1&nVlComprimento=20&nVlAltura=30&nVlLargura=20&sCdMaoPropria=n&nVlValorDeclarado=0&sCdAvisoRecebimento=n&nCdServico=04510&nVlDiametro=0&StrRetorno=xml&nIndicaCalculo=3'.format(cep)
  url = resp
  header = { 'Accept': 'application/xml' }
  r = requests.get(url, headers=header)
  tree =  ET.ElementTree(ET.fromstring(r.content))
  root = tree.getroot()
  filtro = "*"
  i = 0
  txt = ""
  for child in root.iter(filtro):
      if(i==3):
        txt = child.text
      i+=1
  ##new_item = TodoCEP(content = request.POST['content'])
  new_item = TodoItem(content = txt)
 # new_cpf = TodoCPF(content = request.POST['content'])
 # new_item = TodoItem(content = dados_cep['logradouro'])
  new_item.save()
  price=TodoItem(content = txt)
  price.save()
  return HttpResponseRedirect('/')


def addCep(request):
  novo_item = TodoCep(content = request.POST['content'])
  novo_item.save()
  return HttpResponseRedirect('/')


def deleteTodo(request, todo_id):
  item_to_delete = TodoItem.objects.get(id=todo_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')

def coverImage(request):
    image_data = open("./todo/app.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def get_cep(request):
  new_item = TodoItem(content = request.POST['contents'])
  return new_item