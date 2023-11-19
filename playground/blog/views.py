
 
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Membre, Equipement
from .forms import MoveForm
from django.db.models import Q

"""def post_list(request):
    membres = Membre.objects.all()
    equipements = Equipement.objects.all
    return render(request, 'blog/post_list.html', {'membres': membres, 'equipements': equipements})

def post_detail(request, id_membre):
    membre = get_object_or_404(Membre, id_membre = id_membre)
    return render(request, 'blog/post_detail.html', {'Membre': membre})"""


"""def post_list(request):
    membre = Membre.objects.all()
    equipement = Equipement.objects.all()
    return render(request,'blog/post_list.html', {'membre': membre},{'equipement': equipement})"""
 
def post_detail(request, id_membre):
    membre = get_object_or_404(Membre, id_membre=id_membre)
    ancien_lieu = membre.lieu
    if request.method == 'POST':
        nouveau_lieu = get_object_or_404(Equipement, id_equip=membre.lieu.id_equip)
        form = MoveForm(request.POST, instance=membre)
        if form.is_valid():
            change_etat_lieu(ancien_lieu,nouveau_lieu)
            membre.lieu = nouveau_lieu
            change_etat_membre(id_membre)
            form.save()
            membre.save()
            message = "Modification réalisée avec succés"
        else :
            message = "Ce lieu est déjà occupé, la modification est impossible"
        return redirect('post_list')
    else:
        form = MoveForm(instance = membre)
        message = ''
    return render(request,'blog/post_detail.html',{'membre': membre,'message': message,'form': form})

def change_etat_membre(id_membre):
    membre = membre = get_object_or_404(Membre, id_membre=id_membre)
    if membre.etat == 'Occupé' :
        if membre.lieu == 'Salon' :
            membre.etat = 'Repos'
            membre.save()
    if membre.etat == "Repos":
        if membre.lieu != 'Salon':
            membre.etat = 'Occupé'
            membre.save()

def change_etat_lieu(ancienlieu, nouveaulieu):
    if ancienlieu.id_equip != 'Salon':
        ancienlieu.disponibilite = 'Libre'
        ancienlieu.save()
    if nouveaulieu.id_equip != 'Salon':
        nouveaulieu.disponibilte = 'Occupé'
        nouveaulieu.save()





def post_list(request):
    membres = Membre.objects.exclude(id_membre__isnull=True)
    equipements = Equipement.objects.filter(id_equip__isnull = False)
    occupants = {}
    for equipement in equipements :
        tmp = Membre.objects.filter(lieu__id_equip = equipement.id_equip).first()
        if tmp is not None:
            occupants[equipement.id_equip]=tmp.id_membre
        return render(request,'blog/post_list.html', {'membres':membres,'equipements':equipements,'occupants':occupants})
    