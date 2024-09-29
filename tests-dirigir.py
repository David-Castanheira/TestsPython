import pytest
from controllers.dirigir import dirigir

def test_apto_para_dirigir():
    assert dirigir(18, 's') == 'Está apto para dirigir'

def test_nao_apto_para_dirigir():
    assert dirigir(25, 'n') == 'Não está apto para dirigir'

def test_idade_insuficiente_para_dirigir():
    assert dirigir(2, 's') == 'Não tem idade suficiente'
