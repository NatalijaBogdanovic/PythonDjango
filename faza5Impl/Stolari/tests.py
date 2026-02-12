from django.shortcuts import get_object_or_404
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
import Stolari.views as views
from Stolari import models
import json
#
#
# class TestViews(TestCase):
#     def test_explore_view(self):
#         # Get the URL for the explore view
#         url = reverse('explore')
#
#         # Send a GET request to the explore view
#         response = self.client.get(url)
#
#         # Check that the response has a status code of 200 (OK)
#         self.assertEqual(response.status_code, 200)
#
#         # Check that the response uses the correct template
#         self.assertTemplateUsed(response, 'explore.html')
#
#         # Check that the objects are present in the response context
#         objekti = response.context['objekti']
#         self.assertEqual(len(objekti), 5)

class UrlsTest(SimpleTestCase):
    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertEqual(resolve(url).view_name, 'admin:index')

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.login)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logout_view)

    def test_register_render_url(self):
        url = reverse('register_render')
        self.assertEqual(resolve(url).func, views.register_render)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.register)

    def test_pregledKorisnika_url(self):
        url = reverse('pregledKorisnika')
        self.assertEqual(resolve(url).func, views.pregledKorisnika)

    def test_brisanjeVesti_url(self):
        url = reverse('BrisanjeVesti')
        self.assertEqual(resolve(url).func, views.brisanjeVesti)

    def test_obrisiVest_url(self):
        url = reverse('obrisiVest', args=[1])
        self.assertEqual(resolve(url).func, views.obrisiVest)

    def test_obrisiKorisnika_url(self):
        url = reverse('obrisiKorisnika', args=[1])
        self.assertEqual(resolve(url).func, views.obrisiKorisnika)

    def test_prikazVesti_url(self):
        url = reverse('prikazVesti')
        self.assertEqual(resolve(url).func, views.prikazVesti)

    def test_formaDodajVesti_url(self):
        url = reverse('formaDodajVesti')
        self.assertEqual(resolve(url).func, views.formaDodajVesti)

    def test_dodajVesti_url(self):
        url = reverse('dodajVesti')
        self.assertEqual(resolve(url).func, views.dodajVesti)

    def test_explore_render_url(self):
        url = reverse('explore_render')
        self.assertEqual(resolve(url).func, views.explore_render)

    def test_prikaziExplore_url(self):
        url = reverse('prikaziExplore')
        self.assertEqual(resolve(url).func, views.prikaziExplore)

    def test_prikaziStranicuObjekta_url(self):
        url = reverse('prikaziStranicuObjekta', args=[1])
        self.assertEqual(resolve(url).func, views.prikaziStranicuObjekta)

    def test_prikaziSortiranExplore_url(self):
        url = reverse('prikaziSortiranExplore')
        self.assertEqual(resolve(url).func, views.prikaziSortiranExplore)

    def test_belgrade_url(self):
        url = reverse('belgrade')
        self.assertEqual(resolve(url).func, views.belgrade)

    def test_nis_url(self):
        url = reverse('nis')
        self.assertEqual(resolve(url).func, views.nis)

    def test_noviSad_url(self):
        url = reverse('noviSad')
        self.assertEqual(resolve(url).func, views.noviSad)

    def test_clubs_url(self):
        url = reverse('clubs')
        self.assertEqual(resolve(url).func, views.clubs)

    def test_pubs_url(self):
        url = reverse('pubs')
        self.assertEqual(resolve(url).func, views.pubs)

    def test_restaurants_url(self):
        url = reverse('restaurants')
        self.assertEqual(resolve(url).func, views.restaurants)

    def test_kuhinjaItalian_url(self):
        url = reverse('italian')
        self.assertEqual(resolve(url).func, views.kuhinjaItalian)

    def test_kuhinjaSerbian_url(self):
        url = reverse('serbian')
        self.assertEqual(resolve(url).func, views.kuhinjaSerbian)

    def test_reviews_url(self):
        url = reverse('reviews')
        self.assertEqual(resolve(url).func, views.reviews)

    def test_add_favorites_url(self):
        url = reverse('add_favorites', args=[1])
        self.assertEqual(resolve(url).func, views.add_favorites)

    def test_delete_favorites_url(self):
        url = reverse('delete_favorites', args=[1])
        self.assertEqual(resolve(url).func, views.delete_favorites)

    def test_prikaziOmiljene_url(self):
        url = reverse('prikaziOmiljene')
        self.assertEqual(resolve(url).func, views.prikaziOmiljene)

    def test_oceni_objekat_url(self):
        url = reverse('oceni_objekat', args=[1])
        self.assertEqual(resolve(url).func, views.oceni_objekat)

    def test_markirajPozitivnoR_url(self):
        url = reverse('markirajPozitivnoR', args=[1, 1])
        self.assertEqual(resolve(url).func, views.markirajPozitivnoR)

    def test_markirajNegativnoR_url(self):
        url = reverse('markirajNegativnoR', args=[1, 1])
        self.assertEqual(resolve(url).func, views.markirajNegativnoR)

    def test_markirajPozitivnoI_url(self):
        url = reverse('markirajPozitivnoI', args=[1, 1])
        self.assertEqual(resolve(url).func, views.markirajPozitivnoI)

    def test_markirajNegativnoI_url(self):
        url = reverse('markirajNegativnoI', args=[1, 1])
        self.assertEqual(resolve(url).func, views.markirajNegativnoI)

    def test_pregledRezervacijaIIznajmljivanja_url(self):
        url = reverse('pregledRezervacijaIIznajmljivanja')
        self.assertEqual(resolve(url).func, views.pregledRezervacijaIIznajmljivanja)

    def test_reservePlace_url(self):
        url = reverse('reservePlace', args=[1])
        self.assertEqual(resolve(url).func, views.reservePlace)

    def test_reservation_url(self):
        url = reverse('reservation', args=[1])
        self.assertEqual(resolve(url).func, views.reservation)

    def test_reserveTable_url(self):
        url = reverse('reserveTable', args=[1])
        self.assertEqual(resolve(url).func, views.reserveTable)

    def test_raspoloziviStolovi_url(self):
        url = reverse('raspoloziviStolovi', args=[1])
        self.assertEqual(resolve(url).func, views.raspoloziviStolovi)

    def test_choseTable_url(self):
        url = reverse('choseTable', args=['2023-06-12', '10:00', '2023-06-12', '12:00'])
        self.assertEqual(resolve(url).func, views.choseTable)

    def test_prikazProfila_url(self):
        url = reverse('prikazProfila')
        self.assertEqual(resolve(url).func, views.prikazProfila)

    def test_ostvariPopust_url(self):
        url = reverse('ostvariPopust')
        self.assertEqual(resolve(url).func, views.ostvariPopust)

from unittest import TestCase

class ModelsTest(TestCase):

    def setUp(self):
        self.admin = models.Admin.objects.create(username='adminn', password='password')
        self.galerija1 = models.Galerija.objects.create(path='/path/to/image.jpg', tipslike='C', idobj=6, idvest=None)
        self.iznajmljivanje = models.Iznajmljivanje.objects.create(datumpocetka='2023-06-01', vremepocetka='10:00:00',
                                                            datumkraja='2023-06-02', vremekraja='10:00:00',
                                                            status='unmarked', idobj=1, idrreg=1)
        self.objekat1 = models.Objekat.objects.create(naziv='testObjekat',adresa='adresa',grad='beograd',tipobj='r',tipkuhinje='i',ukocena=50,brocena=5,opis='opis',idmen=2)
        self.registrovani = models.Registrovani(pozpoeni=15, negpoeni=5)
        self.rezervacija = models.Rezervacija.objects.create(datumpocetka='2023-06-01', vremepocetka='10:00:00',
                                                      datumkraja='2023-06-02', vremekraja='10:00:00',
                                                      status='unmarked', idsto=1,
                                                      idrreg=1, idobj=1)
        self.tip = models.Tip.objects.create(naziv='TestTip')
        # Create a test instance of the Sto model
        self.sto = models.Sto.objects.create(idobj=1, idtip=self.tip.idtip)

    def test_srednja_ocena(self):
        ocena = self.objekat1.srednja_ocena()
        self.assertEqual(ocena,10)

    def test_dohvTip(self):
        expected_result = self.tip.naziv

        # Call the dohvTip method on the test instance
        actual_result = self.sto.dohvTip()

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)

    def test_dovoljnoPoena(self):
        expected_result = 1
        # Call the dovoljnoPoena method on the test instance
        actual_result = self.registrovani.dovoljnoPoena()
        # Assert that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)

    def test_galerija_model(self):
        self.assertEqual(self.galerija1.path, '/path/to/image.jpg')
        self.assertEqual(self.galerija1.tipslike, 'C')
        self.assertEqual(self.galerija1.idobj, 6)
        self.assertIsNone(self.galerija1.idvest)

    def test_admin_model(self):
        self.assertEqual(self.admin.username, 'adminn')
        self.assertEqual(self.admin.password, 'password')

    def test_get_user_name_Iznajmljivanje(self):
        user_name = self.iznajmljivanje.getUserName()
        registrovani = get_object_or_404(models.Registrovani, idrreg=1)
        self.assertEqual(user_name, registrovani.ime)

    def test_get_user_last_name_Iznajmljivanje(self):
        user_last_name = self.iznajmljivanje.getUserLastName()
        registrovani = get_object_or_404(models.Registrovani, idrreg=1)
        self.assertEqual(user_last_name, registrovani.prezime)

    def test_getUserName(self):
        expected_result = 'Pera'

        # Call the getUserName method on the test instance
        actual_result = self.rezervacija.getUserName()

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)

    def test_getUserLastName(self):
        expected_result = 'Peric'

        # Call the getUserLastName method on the test instance
        actual_result = self.rezervacija.getUserLastName()

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)

    def test_getObjectName(self):
        expected_result = 'Insolita'

        # Call the getObjectName method on the test instance
        actual_result = self.rezervacija.getObjectName()

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)



