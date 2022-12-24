from django.shortcuts import render,redirect
from multiprocessing import context
from .models import Artikel,Kategori,Info
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
import requests
def is_creator(user):
    if user.groups.filter(name='Creator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Creator').exists():
        request.session['is_creator'] = 'creator'
    
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    } 
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.all()
    context = {
        'title' : 'dashboard',
        'artikel': artikel,
    }
    return render(request, template_name, context)

def info(request):
    template_name = "back/tabel_berita.html"
    artikel = Info.objects.all()
    context = {
        'title' : 'dashboard',
        'artikel': artikel,
    }
    return render(request, template_name, context)


@login_required
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'dashboard',
        'list_user' : list_user
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kat = Kategori.objects.get(nama=kategori)
      
        #simpan produk karena ada relasi ke tabel kategori 
        Artikel.objects.create(
            nama = nama,
            judul = judul,
            body = body,
            kategori = kat,
        )
        return redirect (artikel)
    context = {
        'title':'Tambah Artikel',
        'kategori':kategori,

    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'View Artikel',
        'artikel' :artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request ,id ):
    template_name = 'back/edit_artikel.html'
    kategori = Kategori.objects.all()
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kat = Kategori.objects.get(nama=kategori)

        #input Kategori Dulu
        

        #simpan produk karena ada relasi ke tabel kategori 
        a.nama = nama
        a.judul = judul
        a.body = body
        a.kategori = kat
        a.save() 
        return redirect(artikel)
    context = {
        'title':'Edit Artikel',
        'kategori':kategori,
        'artikel' : artikel,

    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request,id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

def sinkron_info(request):
	url = "https://newsapi.org/v2/top-headlines?country=id&apiKey=dc045a8f7399442b8d20d4b80f8b7cd3"
	data = requests.get(url).json()
	for d in data['articles']:
		cek_berita = Info.objects.filter(title=d['title'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.title=d['title']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Info.objects.create(
				title = d['title'],
                author = d['author'],
				description = d['description'],
				link = d['url'],
				isodate = d['publishedAt'],
				image = d['urlToImage'],
                content = d['content'],
			)
	return redirect(info)

# @login_required
# def artikel(request):
#     url = "https://newsapi.org/v2/top-headlines?country=id&apiKey=dc045a8f7399442b8d20d4b80f8b7cd3"

#     data = requests.get(url).json()
    

#     a = data['articles']
#     nama = []
#     judul = []
#     desc = []
#     link = []
#     isi = []
#     tanggal = []
#     image = []

#     for i in range(len(a)):
#         f = a[i]
#         judul.append(f['title'])
#         nama.append(f['author'])
#         desc.append(f['description'])
#         link.append(f['url'])
#         isi.append(f['content'])
#         tanggal.append(f['publishedAt'])
#         image.append(f['urlToImage'])
        


#     mylist = zip(nama,judul,desc,link,isi,tanggal,image)
#     context ={'mylist':mylist}

#     return render(request,'back/tabel_artikel.html',context)