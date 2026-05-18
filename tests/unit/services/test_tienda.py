"""
Pruebas unitarias para la clase TiendaMuebles.
"""
import pytest
from unittest.mock import Mock
from services.tienda import TiendaMuebles
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.composicion.comedor import Comedor


class TestTiendaMuebles:
    @pytest.fixture
    def tienda(self):
        return TiendaMuebles("Tienda Test")

    @pytest.fixture
    def silla(self):
        return Silla("Silla Test", "Madera", "Café", 50.0)

    @pytest.fixture
    def mesa(self):
        return Mesa("Mesa Test", "Madera", "Café", 200.0)

    def test_instanciacion_correcta(self, tienda):
        assert tienda.nombre == "Tienda Test"

    def test_nombre_por_defecto(self):
        tienda = TiendaMuebles()
        assert tienda.nombre == "Mueblería OOP"

    def test_agregar_mueble(self, tienda, silla):
        resultado = tienda.agregar_mueble(silla)
        assert "exitosamente" in resultado.lower()

    def test_agregar_mueble_none(self, tienda):
        resultado = tienda.agregar_mueble(None)
        assert "error" in resultado.lower()

    def test_buscar_muebles_por_nombre(self, tienda, silla):
        tienda.agregar_mueble(silla)
        resultados = tienda.buscar_muebles_por_nombre("Silla")
        assert len(resultados) == 1

    def test_buscar_muebles_nombre_vacio(self, tienda):
        resultados = tienda.buscar_muebles_por_nombre("")
        assert resultados == []

    def test_filtrar_por_precio(self, tienda, silla, mesa):
        tienda.agregar_mueble(silla)
        tienda.agregar_mueble(mesa)
        resultados = tienda.filtrar_por_precio(0, 100)
        assert len(resultados) >= 1

    def test_filtrar_por_material(self, tienda, silla):
        tienda.agregar_mueble(silla)
        resultados = tienda.filtrar_por_material("Madera")
        assert len(resultados) == 1

    def test_filtrar_por_material_vacio(self, tienda):
        resultados = tienda.filtrar_por_material("")
        assert resultados == []

    def test_aplicar_descuento_valido(self, tienda):
        resultado = tienda.aplicar_descuento("sillas", 10)
        assert "10%" in resultado

    def test_aplicar_descuento_invalido(self, tienda):
        resultado = tienda.aplicar_descuento("sillas", 0)
        assert "error" in resultado.lower()

    def test_realizar_venta(self, tienda, silla):
        tienda.agregar_mueble(silla)
        venta = tienda.realizar_venta(silla, "Juan")
        assert "precio_final" in venta
        assert venta["cliente"] == "Juan"

    def test_realizar_venta_mueble_no_disponible(self, tienda, silla):
        resultado = tienda.realizar_venta(silla)
        assert "error" in resultado

    def test_obtener_estadisticas(self, tienda, silla):
        tienda.agregar_mueble(silla)
        stats = tienda.obtener_estadisticas()
        assert stats["total_muebles"] == 1

    def test_generar_reporte_inventario(self, tienda, silla):
        tienda.agregar_mueble(silla)
        reporte = tienda.generar_reporte_inventario()
        assert "REPORTE" in reporte

    def test_agregar_comedor(self, tienda):
        mock_comedor = Mock(spec=Comedor)
        mock_comedor.nombre = "Comedor Mock"
        resultado = tienda.agregar_comedor(mock_comedor)
        assert "exitosamente" in resultado.lower()

    def test_agregar_comedor_none(self, tienda):
        resultado = tienda.agregar_comedor(None)
        assert "error" in resultado.lower()

    def test_realizar_venta_con_descuento(self, tienda):
        s = Silla("Silla Mock", "Madera", "Café", 100.0)
        tienda.agregar_mueble(s)
        tienda.aplicar_descuento("sillas", 10)
        venta = tienda.realizar_venta(s, "Pedro")
        assert venta["descuento"] == 10.0
        assert venta["precio_final"] < 100.0