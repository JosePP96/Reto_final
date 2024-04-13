import unittest
from app import create_app
from app import db
from app.models import Data

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configurar la aplicación para pruebas
        self.app = create_app("test")
        self.client = self.app.test_client()

        # Configurar la base de datos para pruebas
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        # Limpiar la base de datos después de cada prueba
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_data(self):
        # Prueba de creación de un nuevo dato en la base de datos
        response = self.client.post("/data", json={"name": "Test Data"})
        self.assertEqual(response.status_code, 200)

        # Verificar que el dato se haya creado correctamente
        with self.app.app_context():
            data = Data.query.filter_by(name="Test Data").first()
            self.assertIsNotNone(data)

    def test_get_all_data(self):
        # Prueba de obtención de todos los datos de la base de datos
        response = self.client.get("/data")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_delete_data(self):
    # Crear un dato en la base de datos para eliminarlo después
        with self.app.app_context():
        # Crear y agregar la instancia data a la sesión
            data = Data(name="Delete Test Data")
            db.session.add(data)
            db.session.commit()

        # Prueba de eliminación de un dato de la base de datos
            response = self.client.delete(f"/data/{data.id}")
            self.assertEqual(response.status_code, 200)

        # Verificar que el dato se haya eliminado correctamente
        with self.app.app_context():
            deleted_data = Data.query.get(data.id)
            self.assertIsNone(deleted_data)

if __name__ == "__main__":
    unittest.main()