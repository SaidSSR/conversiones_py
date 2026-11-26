import pytest
import Conversion as con

def test_pulgadas_cm():
    assert con.centimetrosApulgadas(5.08) == 2
    assert con.pulgadasAcentimetros(2) == 5.08

def test_galonesALitros():
    assert round(con.galonesALitros(1), 2) == 3.79

def test_litrosAGalones():
    assert round(con.litrosAGalones(1), 2) == 0.26

