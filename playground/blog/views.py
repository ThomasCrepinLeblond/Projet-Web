
 
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Membres, Equipement

def post_list(request):
    membres = Membres.objects.all()
    equipements = Equipement.objects.all
    return render(request, 'blog/post_list.html', {'membres': membres, 'equipements': equipements})

def post_detail(request, id_membre):
    membre = get_object_or_404(Membres, id_membre = id_membre)
    return render(request, 'blog/post_detail.html', {'Membre': membre})

"""
suite du travail mais qui ne marche pas pour l'instant
def post_list(request):
    membre = Membres.objects.all()
    return render(request,'blog/post_list.html', {'Membre': membre})
 
def post_detail(request, id_membre):
    membre = get_object_or_404(Membres, id_membre=id_membre)
    form=MoveForm()
    if form.is_valid():
        ancien_lieu = get_object_or_404(Equipement, id_equip=membre.lieu.id_equip)
        ancien_lieu.disponibilite = "libre"
        ancien_lieu.save()
        form.save()
        nouveau_lieu = get_object_or_404(Equipement, id_equip=membre.lieu.id_equip)
        nouveau_lieu.disponibilite = "occupé"
        nouveau_lieu.save()
        return redirect('post_detail', id_membre=id_membre)
    else:
        form = MoveForm()
        return render(request,
                  'playground/post_detail.html',
                  {'Membre': membre, 'lieu': ancien_lieu, 'form': form})"""