import unittest

class registro:
    try:
        def registro(self,usuario,edad):
            usuario=input("Nombre")
            edad=input("Edad")
            assert isinstance(edad, object)
            return {"usuario:":usuario,"apellido":usuario+"lwong","edad:":edad}
    except Exception:
        print("ERROR")


class NotificationsTestCase(unittest.TestCase):
    try:

        def test_user_repository(self):
            users=registro()
            user=users.registro("lwong","20")

            self.assertEquals("Luis A. Wong Q.",user['apellido'])
    except Exception:
        print("ERROR")


if __name__ == '__main__':
        unittest.main()