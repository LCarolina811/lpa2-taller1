"""
Pruebas unitarias para la clase SofaCama.
"""
import pytest
from models.concretos.sofacama import SofaCama


class TestSofaCama:
    @pytest.fixture
    def sofacama_basico(self):
        return SofaCama("Sofá Cama Básico", "Tela", "Gris", 600)

    @pytest.fixture
    def sofacama_completo(self):
        return SofaCama("Sofá Cama Premium", "Cuero", "Negro", 900,
                        capacidad_personas=3, material_tapizado="Cuero",
                        tamaño_cama="king", incluye_colchon=True,
                        mecanismo_conversion="electrico")

    def test_instanciacion_correcta(self, sofacama_basico):
        assert sofacama_basico.nombre == "Sofá Cama Básico"
        assert sofacama_basico.material == "Tela"
        assert sofacama_basico.precio_base == 600

    def test_herencia_multiple(self, sofacama_basico):
        from models.concretos.sofa import Sofa
        from models.concretos.cama import Cama
        assert isinstance(sofacama_basico, Sofa)
        assert isinstance(sofacama_basico, Cama)

    def test_modo_inicial_sofa(self, sofacama_basico):
        assert sofacama_basico.modo_actual == "sofa"

    def test_convertir_a_cama(self, sofacama_basico):
        resultado = sofacama_basico.convertir_a_cama()
        assert sofacama_basico.modo_actual == "cama"
        assert "cama" in resultado.lower()

    def test_convertir_a_sofa(self, sofacama_basico):
        sofacama_basico.convertir_a_cama()
        resultado = sofacama_basico.convertir_a_sofa()
        assert sofacama_basico.modo_actual == "sofa"
        assert "sofá" in resultado.lower()

    def test_convertir_a_cama_ya_en_cama(self, sofacama_basico):
        sofacama_basico.convertir_a_cama()
        resultado = sofacama_basico.convertir_a_cama()
        assert "ya está" in resultado.lower()

    def test_convertir_a_sofa_ya_en_sofa(self, sofacama_basico):
        resultado = sofacama_basico.convertir_a_sofa()
        assert "ya está" in resultado.lower()

    def test_calcular_precio(self, sofacama_basico):
        precio = sofacama_basico.calcular_precio()
        assert precio > 600

    def test_calcular_precio_completo(self, sofacama_completo):
        precio = sofacama_completo.calcular_precio()
        assert precio > 900

    def test_obtener_capacidad_total(self, sofacama_basico):
        capacidad = sofacama_basico.obtener_capacidad_total()
        assert "como_sofa" in capacidad
        assert "como_cama" in capacidad

    def test_obtener_descripcion(self, sofacama_basico):
        desc = sofacama_basico.obtener_descripcion()
        assert "Sofá Cama Básico" in desc