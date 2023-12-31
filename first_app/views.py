from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello I am from views.py!"}
    return render(request, 'index.html',context=my_dict)

def calculadora(request):
    return render(request, 'Calculadora_Compl.html')

def form_Produto_view(request):
    form = forms.FormProduto()
    if request.method == 'POST':
        form = forms.FormProduto(request.POST)
        if form.is_valid():
            print("Formulário Validado com Sucesso")
            print ("Nome"+form.cleaned_data['name'])
            print ("Quantidade" +str(form.cleaned_data['quantidade']))
            print ("Cor" +form.cleaned_data['cor'])
    return render(request, 'forms_simples.html', {'form':form})

def cadastro_produto(request):
    form = forms.ProdutoForm()
    if request.method == 'POST':
        form = forms.ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Erro ao Gravar")
    
    return render(request, 'forms_simples.html', {'form':form})

def users(request):
    form = forms.ProdutoForm()

    if request.method == "POST":
        form = forms.Produto(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Erro Formulário Inválido")

    return render(request, 'appTwo/user.html', {'form':form})
