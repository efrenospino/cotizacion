from django.test import TestCase
from app1.models import Empleado
from django.contrib.auth.models import User

class EmpleadoTestCase(TestCase):

    def setUp(self):
        u1 = User.objects.create(first_name = 'Vladimir', last_name = 'Hernandez',
            username = 'vhernandez', email = 'vhernandez@juniorclubsa.co',
            password = '123', is_superuser = False, is_staff = True)
        u2 = User.objects.create(first_name = 'Sebastian', last_name = 'Viera',
            username = 'sviera', email = 'sviera@juniorclubsa.co',
            password = '123', is_superuser = False, is_staff = True)
        Empleado.objects.create(identificacion = 12345664, idTipoId = 1,
            user = u1)

    #Implementacion de prueba unitaria
    def test_user_empleado(self):
        empleado1 = Empleado.objects.get(identificacion=12345664)
        self.assertEqual(empleado1.user.first_name, "Vladimir")
