"""
Pruebas unitarias para la clase Silla.
"""
import pytest
from models.concretos.silla import Silla


class TestSilla:
    @pytest.fixture
    def silla_basica(self):
        return Silla("Silla Básica", "Madera", "Café", 50.0)

    @pytest.fixture
    def silla_oficina(self):
        return Silla("Silla Oficina", "Metal", "Negro", 100.0,
                     tiene_respaldo=True, material_tapizado="Cuero",
                     altura_regulable=True, tiene_ruedas=True)

    def test_instanciacion_correcta(self, silla_basica):
        assert silla_basica.nombre == "Silla Básica"
        assert silla_basica.material == "Madera"
        assert silla_basica.color == "Café"
        assert silla_basica.precio_base == 50.0

    def test_capacidad_siempre_uno(self, silla_basica):
        assert silla_basica.capacidad_personas == 1

    def test_calcular_precio_basico(self, silla_basica):
        precio = silla_basica.calcular_precio()
        assert precio > 0

    def test_calcular_precio_con_ruedas_y_altura(self, silla_oficina):
        precio = silla_oficina.calcular_precio()
        assert precio > 100.0

    def test_es_silla_oficina_true(self, silla_oficina):
        assert silla_oficina.es_silla_oficina() is True

    def test_es_silla_oficina_false(self, silla_basica):
        assert silla_basica.es_silla_oficina() is False

    def test_regular_altura_valida(self, silla_oficina):
        resultado = silla_oficina.regular_altura(70)
        assert "70" in resultado

    def test_regular_altura_sin_regulacion(self, silla_basica):
        resultado = silla_basica.regular_altura(70)
        assert "no tiene" in resultado.lower()

    def test_regular_altura_fuera_de_rango(self, silla_oficina):
        resultado = silla_oficina.regular_altura(200)
        assert "entre 40 y 100" in resultado

    def test_nombre_vacio_lanza_error(self):
        with pytest.raises(ValueError):
            silla = Silla("Silla", "Madera", "Café", 50.0)
            silla.nombre = ""

    def test_precio_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            silla = Silla("Silla", "Madera", "Café", 50.0)
            silla.precio_base = -10

    def test_obtener_descripcion(self, silla_basica):
        desc = silla_basica.obtener_descripcion()
        assert "Silla Básica" in desc
        assert "Madera" in desc