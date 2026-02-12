import random
from itertools import chain

from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Admin, Menadzer, Registrovani, Galerija, Vest, Objekat, Rezervacija, Sto, Omiljeni, Iznajmljivanje
from django.contrib.auth import logout
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q


def login(request): #login logika - Pavle Perovic
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if Admin.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            return render(request, 'admin.html')
        elif Menadzer.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            return render(request, 'menadzer.html')
        elif Registrovani.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            return render(request, 'userIndex.html')
        else:
            poruka = "Pogresan username ili password"
            return render(request, 'login.html', {'poruka': poruka, 'template_name': 'login.html'})
    else:
        return render(request, 'login.html', {'template_name': 'login.html'})

def logout_view(request): #logout logika - Pavle Perovic
    logout(request) #logout radi i flush i modified = true
    return redirect('login') #skoci na pocetnu stranu

def register_render(request): #hendler za redirect - Pavle Perovic
    return render(request, 'register.html')

def register(request): #registracija korisnika - Pavle Perovic
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        datetime = request.POST.get('datetime')

        if username is None or password is None or first_name is None or last_name is None or number is None or gender is None or datetime is None:
            error = 'Neispravan unos!'
            return render(request, 'register.html', {'error': error})
        if username.strip() == '' or password.strip() == '' or first_name.strip() == '' or last_name.strip() == '' or number.strip() == '' or gender.strip() == '' or datetime.strip() == '':
            error = 'Sva polja moraju biti popunjena!'
            return render(request, 'register.html', {'error': error})
        #Obrada unique podataka.
        if Registrovani.objects.filter(username=username).exists():
            error = 'Username vec postoji!'
            return render(request, 'register.html', {'error': error})
        if Registrovani.objects.filter(brtelefona=number).exists():
            error = 'Broj telefona vec postoji!'
            return render(request, 'register.html', {'error': error})

        # Insert
        user = Registrovani(username=username, password=password, ime=first_name, prezime=last_name, brtelefona=number, pol=gender, datumrodjenja=datetime, pozpoeni=0, negpoeni=0)
        user.save()

        # Redirektujemo se na pocetnu stranicu
        return redirect('login')

    # ako metoda nije POST
    error = 'Metoda nije POST!'
    return render(request, 'register.html', {'error': error})

def pregledKorisnika(request): #popunjavanje tabele kod pregleda korisnika koji radi administrator - Pavle Perovic
    korisnici = Registrovani.objects.all()
    context = {'korisnici': korisnici}
    return render(request, 'pregledKorisnika.html', context)

def prikaziExplore(request): #Milica Banjac - renderovanje explore stranice sa svim objektima
    objekti = Objekat.objects.all()
    context = {'objekti': objekti}
    return render(request, 'explore.html',context)

def explore_render(request): #hendler za redirect - Milica Banjac
    return render(request, 'explore.html')

@require_http_methods(["POST"])
def prikaziStranicuObjekta(request,idobj): #Milica Banjac
    if request.method=="POST":
        objekat=get_object_or_404(Objekat,idobj=idobj)
        context = {'objekat': objekat}
        return render(request, 'stranicaObjekta.html', context)
    error='Metoda nije POST!'
    return render(request, 'register.html', {'error':error})



def registerRender(request): #Pavle Perovic - hendler za redirect
    return render(request, 'register.html')

def obrisiKorisnika(request, idrreg): #brisanje korisnika iz baze - Pavle Perovic
    korisnik = get_object_or_404(Registrovani, idrreg=idrreg)
    korisnik.delete()
    return redirect('pregledKorisnika')

def obrisiVest(request,idvest): #brisanje vesti iz baze - Marija Aleksic
    vest = get_object_or_404(Vest,idvest=idvest)
    vest.delete()
    return redirect('BrisanjeVesti')

def pregledRezervacijaIIznajmljivanja(request): #prikazivanje rezervacija i iznajmljivanja na stranici menadzera - Marija Aleksic
    username = request.session.get('username')
    menadzer = get_object_or_404(Menadzer, username=username)
    objekti = Objekat.objects.filter(idmen=menadzer.idmen)
    stolovi = Sto.objects.filter(idobj__in=list(objekti.values_list('idobj', flat=True)))
    sveRezervacije = Rezervacija.objects.filter(idsto__in=list(stolovi.values_list('idsto', flat=True)))
    unmarkedRezervacije = Rezervacija.objects.filter(status='unmarked')
    idUnmarked = unmarkedRezervacije.values_list('idrez', flat=True)
    rezervacije = sveRezervacije.filter(idrez__in=idUnmarked)
    svaIznajmljivanja = Iznajmljivanje.objects.filter(idobj__in=list(objekti.values_list('idobj', flat=True)))
    iznajmljivanja = svaIznajmljivanja.filter(status='unmarked')
    context = {'rezervacije': rezervacije, 'iznajmljivanja' : iznajmljivanja}
    return render(request, 'menadzerPregledRezervacija.html', context)

def markirajPozitivnoR(request, idrreg, idrez): #menadzer markira rezervaciju kao ostvarenu - Marija Aleksic
    korisnik = get_object_or_404(Registrovani, idrreg=idrreg)
    rezervacija = get_object_or_404(Rezervacija, idrez=idrez)
    rezervacija.status = 'ostvaren'
    rezervacija.save()
    poz = korisnik.pozpoeni
    poz = poz + 1
    korisnik.pozpoeni = poz
    korisnik.save()
    return redirect('pregledRezervacijaIIznajmljivanja')

def markirajNegativnoR(request, idrreg, idrez): #menadzer markira rezervaciju kao neostvarenu - Marija Aleksic
    korisnik = get_object_or_404(Registrovani, idrreg=idrreg)
    rezervacija = get_object_or_404(Rezervacija, idrez=idrez)
    rezervacija.status = 'neostvaren'
    rezervacija.save()
    neg = korisnik.negpoeni
    neg = neg + 1
    korisnik.negpoeni = neg
    korisnik.save()
    return redirect('pregledRezervacijaIIznajmljivanja')

def markirajPozitivnoI(request, idrreg, idizn): #menadzer markira izajmljivanje kao ostvareno - Marija Aleksic
    korisnik = get_object_or_404(Registrovani, idrreg=idrreg)
    rezervacija = get_object_or_404(Iznajmljivanje, idizn=idizn)
    rezervacija.status = 'ostvaren'
    rezervacija.save()
    poz = korisnik.pozpoeni
    poz = poz + 1
    korisnik.pozpoeni = poz
    korisnik.save()
    return redirect('pregledRezervacijaIIznajmljivanja')

def markirajNegativnoI(request, idrreg, idizn): #menadzer markira iznajmljivanje kao neostvareno - Marija Aleksic
    korisnik = get_object_or_404(Registrovani, idrreg=idrreg)
    rezervacija = get_object_or_404(Iznajmljivanje, idizn=idizn)
    rezervacija.status = 'neostvaren'
    rezervacija.save()
    neg = korisnik.negpoeni
    neg = neg + 1
    korisnik.negpoeni = neg
    korisnik.save()
    return redirect('pregledRezervacijaIIznajmljivanja')

def brisanjeVesti(request): #Slanje svih vesti za brisanje - Marija Aleksic
    vesti = Vest.objects.all()
    context = {'vesti': vesti}
    return render(request, 'BrisanjeVesti.html', context)

def prikazVesti(request): #prikaz vesti samo za testiranje trenutno - Pavle Perovic
    vesti = Vest.objects.all()
    context = {'vesti': vesti}
    return render(request, 'prikazVesti.html', context)

def formaDodajVesti(request): #pomocna za otvaranje stranice sa formom za dodavanje vesti - Pavle Perovic
    return render(request, 'FormaDodajVesti.html')

def dodajVesti(request): #Dodavanje vesti funkcionalnost - Pavle Perovic
    error = ''
    if request.method == 'POST':
        naslov = request.POST.get('naslov')
        tekst = request.POST.get('tekst')
        path = request.POST.get('path')
    if naslov is None or tekst is None or path is None:
        error = 'Neispravan unos!'
        return render(request, 'FormaDodajVesti.html', {'error': error})
    if naslov.strip() == '' or tekst.strip() == '' or path.strip() == '':
        error = 'Sva polja moraju biti popunjena!'
        return render(request, 'FormaDodajVesti.html', {'error': error})
    if Vest.objects.filter(naslov=naslov).exists():
        error = 'Vec postoji naslov za ovu vest!'
        return render(request, 'FormaDodajVesti.html', {'error': error})
    vest = Vest(naslov=naslov, tekst=tekst)
    vest.save()
    slika = Galerija(path=path, tipslike='v', idvest=vest.idvest)
    slika.save()
    return render(request, 'admin.html')
    # ako metoda nije POST
    error = 'Metoda nije POST!'
    return render(request, 'register.html', {'error': error})

def prikazProfila(request): #prikaz userProfile stranice - Marija Aleksic
    username = request.session.get('username')
    korisnik = get_object_or_404(Registrovani, username=username)
    popust=0
    context = {'korisnik': korisnik,
               'popust': popust}
    return render(request, 'userProfile.html', context)

def ostvariPopust(request): #ostvarivanje popusta funkcionalnost - Marija Aleksic
    username = request.session.get('username')
    korisnik = get_object_or_404(Registrovani, username=username)
    korisnik.pozpoeni=0
    korisnik.negpoeni=0
    korisnik.save()
    popust = random.randint(10000, 99999)
    context = {'korisnik': korisnik,
               'popust': popust}
    return render(request, 'userProfile.html', context)

from django.db.models import F, Count, Q


def prikaziSortiranExplore(request): #Natalija Bogdanovic - explore sortiran po ocenama

    objekti=Objekat.objects.annotate(c=F('ukocena') / F('brocena')).order_by('-c')
    context = {'objekti': objekti}
    return render(request, 'explore.html', context)

def belgrade(request):   #Natalija Bogdanovic - svi objekti koji se nalaze u Beogradu
    objekti=Objekat.objects.filter(grad='Beograd')
    gr = 'Beograd'
    context = {'objekti': objekti, 'gr': gr}
    return render(request, 'explore.html', context)

def nis(request):   #Natalija Bogdanovic - svi objekti koji  se nalaze u Nisu
    objekti=Objekat.objects.filter(grad='Nis')
    gr = 'Nis'
    context = {'objekti': objekti, 'gr': gr}
    return render(request, 'explore.html', context)

def noviSad(request):   #Natalija Bogdanovic - svi objekti koji se nalaze u Novom Sadu
    objekti=Objekat.objects.filter(grad='Novi Sad')
    gr = 'Novi Sad'
    context = {'objekti': objekti, 'gr': gr}
    return render(request, 'explore.html', context)

def pubs(request):   #Natalija Bogdanovic - svi objekti koji su pubovi
    objekti = Objekat.objects.filter(tipobj='pab')
    tip = 'pab'
    context = {'objekti': objekti, 'tip': tip}
    return render(request, 'explore.html', context)

def clubs(request):   #Natalija Bogdanovic - svi objekti koji su klubovi
    objekti = Objekat.objects.filter(tipobj='klub')
    tip = 'klub'
    context = {'objekti': objekti, 'tip': tip}
    return render(request, 'explore.html', context)

def restaurants(request):   #Natalija Bogdanovic - svi objekti koji su restorani
    objekti = Objekat.objects.filter(tipobj='restoran')
    tip = 'restoran'
    context = {'objekti': objekti, 'tip': tip}
    return render(request, 'explore.html', context)

def kuhinjaItalian(request):   #Natalija Bogdanovic - svi restorani sa italijanskom kuhinjom
    objekti = Objekat.objects.filter(tipkuhinje='italian')
    kuhinja = 'italian'
    context = {'objekti': objekti, 'kuhinja': kuhinja}
    return render(request, 'explore.html', context)

def kuhinjaSerbian(request):   #Natalija Bogdanovic - svi restorani sa srpskom kuhinjom
    objekti = Objekat.objects.filter(tipkuhinje='serbian')
    kuhinja = 'serbian'
    context = {'objekti': objekti, 'kuhinja': kuhinja}
    return render(request, 'explore.html', context)

def reviews(request):   #Natalija Bogdanovic - explore sortiran po broju rezervacija
    rezervacije = Rezervacija.objects.values('idobj').annotate(num_occurrences=Count('idobj')).order_by('-num_occurrences')

    # kreiranje liste jedinstvenih rezervacija za svaki IdObj
    unique_reservations = []
    ids = set()      #set koji se koristi za pracenje vec dodatih idobj kako bismo izbegli dupliciranje rezervacija

    for r in rezervacije:
        if r['idobj'] not in ids:   #ako objekat nije vec dodat u ids
            unique_reservations.append(Rezervacija.objects.filter(idobj=r['idobj']).first()) #dohvatamo sve rez odg obj i prvu dodajemo u listu
            ids.add(r['idobj']) #dodavanjem obj u set oznacavamo da je on odradjen

    context = {'rezervacije': unique_reservations}
    return render(request, 'reviews.html', context)

from django.http import JsonResponse
@require_http_methods(["POST"])
def add_favorites(request, idobj):
    if request.method != 'POST':
        return HttpResponseBadRequest('Samo POST zahtevi su podržani')

    username = request.session.get('username')

    try:
        user = Registrovani.objects.get(username=username)
    except Registrovani.DoesNotExist:
        return Http404('Morate biti registrovan korisnik.')

    omiljen_obj = Omiljeni.objects.filter(idrreg=user.idrreg, idobj=idobj).first()
    if omiljen_obj is None:
        omiljen_obj = Omiljeni(idrreg=user.idrreg, idobj=idobj)
        omiljen_obj.save()
        return HttpResponseBadRequest('Objekat je dodat u omiljene.')
    else:
        return HttpResponseBadRequest('Objekat je vec u omiljenima.')

@require_http_methods(["POST"])
def delete_favorites(request, idobj): #Milica Banjac - funkcionalnost brisanja objekta iz omiljenih korisniku
    if request.method != 'POST':
        return HttpResponseBadRequest('Samo POST zahtevi su podržani')

    username = request.session.get('username')

    try:
        user = Registrovani.objects.get(username=username)
    except Registrovani.DoesNotExist:
        return Http404('Morate biti registrovan korisnik.')

    omiljen_obj= Omiljeni.objects.filter(idrreg=user.idrreg,idobj=idobj).first()
    if(omiljen_obj!=None):
        omiljen_obj.delete()
        return HttpResponseBadRequest('Objekat je obrisan iz omiljenih.')
    else:
        return HttpResponseBadRequest('Objekat nije ni bio u omiljenima')

def prikaziOmiljene(request): #Milica Banjac - prikaz omiljenih
    username=request.session.get('username')
    korisnik = get_object_or_404(Registrovani, username=username)
    korisnik_id=korisnik.idrreg
    try:
        objekti_id = Omiljeni.objects.filter(idrreg=korisnik_id).values_list('idobj', flat=True)
        objekti = Objekat.objects.filter(idobj__in=objekti_id)
    except Omiljeni.DoesNotExist:
        objekti=[]
    context = {'objekti': objekti}
    return render(request, 'omiljeni.html',context)

@require_http_methods(["POST"])
def oceni_objekat(request,idobj): #Milica Banjac - funkcionalnost ocenjivanja objekta
    if request.method == "POST":
        objekat = get_object_or_404(Objekat, idobj=idobj)
        ocena = int(request.POST.get('rating'))
        objekat.ukocena+=ocena
        objekat.brocena+=1
        objekat.save()
        return HttpResponse("Objekat je ocenjen.")
    else:
        return HttpResponse("Došlo je do greške. Za ocenu objekta koristite POST metodu.")


@require_http_methods(["POST"])
def reservePlace(request,idobj):#Milica Banjac - funkcionalnost rezervisanja celog objekta
    if request.method == "POST":
        objekat = get_object_or_404(Objekat, idobj=idobj)
        context={
            'objekat':objekat
        }
        return render(request,'reservePlace.html',context)
    else:
        return HttpResponse("Došlo je do greške.")


def reservation(request,idobj):#Milica Banjac - logika samog iznajmljivanja objekta uz provere da li je slobodan
    if request.method == 'POST':
        datumPocetka = request.POST.get('date1')
        vremePocetka = request.POST.get('time1')
        datumKraja = request.POST.get('date2')
        vremeKraja = request.POST.get('time2')

        datumPocetka = datetime.strptime(datumPocetka, "%Y-%m-%d").date()
        vremePocetka = datetime.strptime(vremePocetka, "%H:%M").time()

        if ((datumPocetka < timezone.now().date()) | ((datumPocetka == timezone.now().date()) & (vremePocetka<timezone.now().time()))):
            return HttpResponse("Trazeni datum i vreme su u proslosti.")

        rezervacije=Rezervacija.objects.filter(datumpocetka=datumPocetka,vremepocetka=vremePocetka,idobj=idobj)
        if(rezervacije):
            return HttpResponse("Nazalost, objekat je zauzet.")

        iznajmljivanja=Iznajmljivanje.objects.filter(datumpocetka=datumPocetka,vremepocetka=vremePocetka,idobj=idobj)
        if (iznajmljivanja):
            return HttpResponse("Nazalost, objekat je zauzet.")

        rezervacije = Rezervacija.objects.filter(
            datumpocetka__lte=datumPocetka,
            vremepocetka__lt=vremeKraja,
            datumkraja__gte=datumPocetka,
            vremekraja__gte=vremePocetka,
            idobj=idobj,
            status='unmarked'
        )
        if (rezervacije):
            return HttpResponse("Nazalost, objekat je zauzet.")

        iznajmljivanja = Iznajmljivanje.objects.filter(
            datumpocetka__lte=datumPocetka,
            vremepocetka__lt=vremeKraja,
            datumkraja__gte=datumPocetka,
            vremekraja__gte=vremePocetka,
            idobj=idobj,
            status='unmarked'
        )
        if (iznajmljivanja):
            return HttpResponse("Nazalost, objekat je zauzet.")

        username=request.session.get('username')
        id=Registrovani.objects.get(username=username)
        idkor=id.idrreg
        iznajmljivanje=Iznajmljivanje(datumpocetka=datumPocetka,vremepocetka=vremePocetka,datumkraja=datumKraja,
                                      vremekraja=vremeKraja,status='unmarked',idobj=idobj,idrreg=idkor)
        iznajmljivanje.save()
        return HttpResponse('Uspesno iznajmljeno.')


def reserveTable(request,idobj):  #Natalija Bogdanovic - funkcionalnost rezervacije jednog stola
    objekat= get_object_or_404(Objekat, idobj=idobj)
    context={'objekat': objekat}
    return render(request,'reserveTable.html',context)

def raspoloziviStolovi(request,idobj):  #Natalija Bogdanovic - logika za filtriranje samo slobodnih stolova za izabrano vreme i datum
    error=''
    if request.method=='POST':
        datumPocetka = request.POST.get('date1')
        vremePocetka = request.POST.get('time1')
        datumKraja = request.POST.get('date2')
        vremeKraja = request.POST.get('time2')

        objekat=get_object_or_404(Objekat,idobj=idobj)
        #strptime fja pretvara string u odgovarajuci format datuma i vremena
        datumPocetka = datetime.strptime(datumPocetka, "%Y-%m-%d").date()
        vremePocetka = datetime.strptime(vremePocetka, "%H:%M").time()
        datumKraja = datetime.strptime(datumKraja, "%Y-%m-%d").date()
        vremeKraja = datetime.strptime(vremeKraja, "%H:%M").time()

        if ((datumPocetka < timezone.now().date()) | ((datumPocetka == timezone.now().date()) & (vremePocetka<timezone.now().time()))):
            error='Trazeno vreme rezervacije je u proslosti'
            context={'objekat':objekat, 'error':error}
            return render(request,'reserveTable.html',context)


        iznajmljivanja=Iznajmljivanje.objects.filter(
            datumpocetka__lte=datumPocetka,
            vremepocetka__lt=vremeKraja,
            datumkraja__gte=datumPocetka,
            vremekraja__gte=vremePocetka,
            idobj=idobj,
            status='unmarked'
        )
        if (iznajmljivanja):
            error='Nazalost, objekat je vec iznajmljen u ovo vreme'
            context={'objekat':objekat, 'error':error}
            return render(request, 'reserveTable.html', context)

        vecPostojiRezervacija=Rezervacija.objects.filter(
            datumpocetka__lte=datumPocetka,
            vremepocetka__lt=vremeKraja,
            datumkraja__gte=datumPocetka,
            vremekraja__gte=vremePocetka,
            status='unmarked'
        )
        vecRezervisaniStolovi=vecPostojiRezervacija.values_list('idsto', flat=True)  #jednodimenzionalna lista idjeva stolova za koje vec postoji rez (jednodim zbog flat u suprotnom lista tuplova)
        stoloviUObjektu=Sto.objects.filter(idobj=idobj)
        stolovi=stoloviUObjektu.exclude(idsto__in=vecRezervisaniStolovi)
        slobodniStolovi=Sto.objects.filter(idsto__in=stolovi)
        context={'slobodniStolovi':slobodniStolovi, 'datumPocetka': datumPocetka, 'vremePocetka': vremePocetka,
                 'datumKraja': datumKraja, 'vremeKraja': vremeKraja, 'objekat':objekat}
        return render(request,'pregledStolova.html',context)

def choseTable(request,datumPocetka,vremePocetka,datumKraja,vremeKraja): #Natalija Bogdanovic - cuvanje rezervisanog stola u bazu
    chosedTable = request.POST.get('stolovi')
    username = request.session.get('username')    #dohvatamo korisnicko ime iz sesije
    korisnik = get_object_or_404(Registrovani, username=username)
    idkor = korisnik.idrreg
    sto = Sto.objects.get(idsto=chosedTable)
    idobj = sto.idobj

    if request.method=='POST':
        datumPocetka = datetime.strptime(datumPocetka, "%Y-%m-%d").date()
        vremePocetka = datetime.strptime(vremePocetka, "%H:%M").time()

        datumKraja = datetime.strptime(datumKraja, "%Y-%m-%d").date()
        vremeKraja = datetime.strptime(vremeKraja, "%H:%M").time()

        rezervacije = Rezervacija.objects.filter(datumpocetka=datumPocetka, vremepocetka=vremePocetka, idobj=idobj)
        if (rezervacije):
            return HttpResponse("Nazalost, objekat je zauzet.")

        iznajmljivanja = Iznajmljivanje.objects.filter(datumpocetka=datumPocetka, vremepocetka=vremePocetka,
                                                       idobj=idobj)
        if (iznajmljivanja):
            return HttpResponse("Nazalost, objekat je zauzet.")

        rezervacije = Rezervacija.objects.filter(
            datumpocetka__lte=datumPocetka,
            vremepocetka__lte=vremePocetka,
            datumkraja__gte=datumPocetka,
            vremekraja__gt=vremePocetka,
            idobj=idobj,
            status='unmarked'
        )
        if (rezervacije):
            return HttpResponse("Nazalost, objekat je zauzet.")

        iznajmljivanja = Iznajmljivanje.objects.filter(
            datumpocetka__lte=datumPocetka,
            vremepocetka__lte=vremePocetka,
            datumkraja__gte=datumPocetka,
            vremekraja__gt=vremePocetka,
            idobj=idobj,
            status='unmarked'
        )
        if (iznajmljivanja):
            return HttpResponse("Nazalost, objekat je zauzet.")

        rez=Rezervacija(datumpocetka=datumPocetka,vremepocetka=vremePocetka, datumkraja=datumKraja,
                        vremekraja=vremeKraja,status='unmarked',idsto=chosedTable, idrreg=idkor, idobj=idobj)
        rez.save()
        return HttpResponse("Uspesno rezervisano")
