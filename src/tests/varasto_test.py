import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_2 = Varasto(-5, -5)
        self.varasto_3 = Varasto(1, 5)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_nollaa_tilavuuden(self):
        self.assertAlmostEqual(self.varasto_2.tilavuus, 0)

    def test_konstruktori_nollaa_saldon(self):
        self.assertAlmostEqual(self.varasto_2.saldo, 0)

    def test_saldo_ylittaa_tilavuuden_konstruktorissa(self):
        # Jos annettu saldo ylittää tilavuuden, pitäisi saldon vähentyä vastaamaan tilavuutta
        self.assertAlmostEqual(self.varasto_3.saldo, self.varasto_3.tilavuus)

    def test_lisaa_negatiivinen_maara(self):
        nyk_maara = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(-5)
        uusi_maara = self.varasto.paljonko_mahtuu()
        self.assertAlmostEqual(nyk_maara, uusi_maara)

    def test_lisaa_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(50)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_negatiivinen_maara(self):
        saatu_maara = self.varasto_3.ota_varastosta(-5)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_ota_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(3)
        varaston_saldo = self.varasto.saldo
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, varaston_saldo)

    def test_varaston_str(self):
        # self.varasto saa vain tilavuuden eikä saldoa, joten pitäisi tulostaa 0 saldo ja tilaa 10
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
