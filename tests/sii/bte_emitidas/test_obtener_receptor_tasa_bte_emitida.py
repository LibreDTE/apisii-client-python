#
# API Gateway: Cliente de API en Python - Pruebas Unitarias.
# Copyright (C) API Gateway <https://www.apigateway.cl>
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la GNU Lesser General Public License (LGPL) publicada
# por la Fundación para el Software Libre, ya sea la versión 3 de la Licencia,
# o (a su elección) cualquier versión posterior de la misma.
#
# Este programa se distribuye con la esperanza de que sea útil, pero SIN
# GARANTÍA ALGUNA; ni siquiera la garantía implícita MERCANTIL o de APTITUD
# PARA UN PROPÓSITO DETERMINADO. Consulte los detalles de la GNU Lesser General
# Public License (LGPL) para obtener una información más detallada.
#
# Debería haber recibido una copia de la GNU Lesser General Public License
# (LGPL) junto a este programa. En caso contrario, consulte
# <http://www.gnu.org/licenses/lgpl.html>.
#

import unittest
from os import getenv, remove as file_remove
from datetime import datetime
from apigatewaycl.api_client import ApiException
from apigatewaycl.api_client.sii.bte import BteEmitidas

class TestObtenerReceptorTasaBteEmitida(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.contribuyente_rut = getenv('TEST_CONTRIBUYENTE_IDENTIFICADOR', '').strip()
        contribuyente_clave = getenv('TEST_CONTRIBUYENTE_CLAVE', '').strip()
        cls.client = BteEmitidas(cls.contribuyente_rut, contribuyente_clave)
        cls.periodo = getenv('TEST_PERIODO', datetime.now().strftime("%Y%m")).strip()
        cls.receptor_rut = getenv('TEST_BTE_EMITIDAS_RECEPTOR_RUT', '').strip()

    # CASO 5: tasa de receptor
    def test_obtener_receptor_tasa_bte_emitida(self):
        if self.receptor_rut == '':
            print('test_receptor_tasa(): no probó funcionalidad.')
            return
        try:
            receptor_tasa = self.client.receptor_tasa(
                self.contribuyente_rut, self.receptor_rut
            )

            self.assertIsNotNone(receptor_tasa)

            if self.verbose:
                    print('test_receptor_tasa(): receptor_tasa', receptor_tasa)
        except ApiException as e:
            self.fail("ApiException: %(e)s" % {'e': e})
