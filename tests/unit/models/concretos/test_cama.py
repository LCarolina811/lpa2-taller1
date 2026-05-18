"""
Pruebas unitarias para la clase Cama.
"""
import pytest
from models.concretos.cama import Cama


class TestCama:
    @pytest.fixture
    def cama_basica(self):
        return Cama("Cama Básica", "Madera", "Café", 300.0)

    @pytest.fixture
    def cama_completa(self):
        return Cama("Cama Premium", "Madera", "Blanco", 500.0,
                    tamaño="king", incluye_colchon=True, tiene_cabecera=True)

    def test_instanciacion_correcta(self, cama_basica):
        assert cama_basica.nombre == "Cama Básica"
        assert cama_basica.material == "Madera"
        assert cama_basica.precio_base == 300.0

    def test_tamaño_por_defecto(self, cama_basica):
        assert cama_basica.tamaño == "individual"

    def test_calcular_precio_individual(self, cama_basica):
        assert cama_basica.calcular_precio() == 300.0

    def test_calcular_precio_matrimonial(self):
        cama = Cama("Cama", "Madera", "Café", 300.0, tamaño="matrimonial")
        assert cama.calcular_precio() == 500.0

    def test_calcular_precio_queen(self):
        cama = Cama("Cama", "Madera", "Café", 300.0, tamaño="queen")
        assert cama.calcular_precio() == 700.0

    def test_calcular_precio_king(self):
        cama = Cama("Cama", "Madera", "Café", 300.0, tamaño="king")
        assert cama.calcular_precio() == 900.0

    def test_calcular_precio_con_colchon(self, cama_basica):
        cama = Cama("Cama", "Madera", "Café", 300.0, incluye_colchon=True)
        assert cama.calcular_precio() == 600.0

    def test_calcular_precio_con_cabecera(self):
        cama = Cama("Cama", "Madera", "Café", 300.0, tiene_cabecera=True)
        assert cama.calcular_precio() == 400.0

    def test_calcular_precio_completo(self, cama_completa):
        precio = cama_completa.calcular_precio()
        assert precio == 1500.0

    def test_tamaño_invalido_lanza_error(self, cama_basica):
        with pytest.raises(ValueError):
            cama_basica.tamaño = "extragrande"

    def test_obtener_descripcion(self, cama_basica):
        desc = cama_basica.obtener_descripcion()
        assert "Cama Básica" in desc
        assert "Madera" in desc