# -*- coding: utf-8 -*-
# @Time    : 7/31/2021 16:54 PM
# @Author  : Rodolfo Londero
# @Email   : rodolfpl@gmail.com
# @File    : test_lines.py
# @Software: PyCharm

import platform
import pytest


class TestLines13Bus:

    @pytest.fixture(scope='function')
    def dss(self, solve_snap_13bus):
        dss = solve_snap_13bus
        dss.lines_write_name('650632')

        return dss

    # ===================================================================
    # Integer methods
    # ===================================================================
    def test_lines_first(self, dss):
        expected = 1
        actual = dss.lines_first()
        assert actual == expected

    def test_lines_next(self, dss):
        expected = 2
        actual = dss.lines_next()
        assert actual == expected

    def test_lines_read_phases(self, dss):
        expected = 3
        actual = dss.lines_read_phases()
        assert actual == expected

    def test_lines_write_phases(self, dss):
        expected = 2
        dss.lines_write_phases(2)
        actual = dss.lines_read_phases()
        assert actual == expected

    def test_lines_num_cust(self, dss):
        expected = 0
        actual = dss.lines_num_cust()
        assert actual == expected

    def test_lines_parent(self, dss):
        expected = 0
        actual = dss.lines_parent()
        assert actual == expected

    def test_lines_count(self, dss):
        expected = 12
        actual = dss.lines_count()
        assert actual == expected

    def test_lines_read_units(self, dss):
        expected = 5
        actual = dss.lines_read_units()
        assert actual == expected

    def test_lines_write_units(self, dss):
        expected = 3
        dss.lines_write_units(expected)
        actual = dss.lines_read_units()
        assert actual == expected

    # ===================================================================
    # String methods
    # ===================================================================
    def test_lines_read_name(self, dss):
        expected = '650632'
        actual = dss.lines_read_name()
        assert actual == expected

    def test_lines_write_name(self, dss):
        expected = '632670'
        dss.lines_write_name(expected)
        actual = dss.lines_read_name()
        assert actual == expected

    def test_lines_read_bus1(self, dss):
        expected = 'rg60.1.2.3'
        actual = dss.lines_read_bus1()
        assert actual == expected

    def test_lines_write_bus1(self, dss):
        expected = '670.1'
        dss.lines_write_bus1(expected)
        actual = dss.lines_read_bus1()
        assert actual == expected

    def test_lines_read_bus2(self, dss):
        expected = '632.1.2.3'
        actual = dss.lines_read_bus2()
        assert actual == expected

    def test_lines_write_bus2(self, dss):
        expected = '670.1'
        dss.lines_write_bus2(expected)
        actual = dss.lines_read_bus2()
        assert actual == expected

    def test_lines_read_linecode(self, dss):
        expected = 'mtx601'
        actual = dss.lines_read_linecode()
        assert actual == expected

    def test_lines_write_linecode(self, dss):
        expected = '723'
        dss.lines_write_linecode(expected)
        actual = dss.lines_read_linecode()
        assert actual == expected

    def test_lines_read_geometry(self, dss):
        expected = ''
        actual = dss.lines_read_geometry()
        assert actual == expected

    def test_lines_write_geometry(self, dss):

        dss.text(
            "New WireData.1/0_ACSR Rac=0.646847 Runits=km GMRac=0.13589  GMRUnits=cm Radius=0.50546 Radunits=cm Normamps=260  Emergamps=260")
        dss.text("New LineGeometry.1PH-x4_ACSRx4_ACSR  nconds=2  nphases=1 "
                      " cond=1  wire=1/0_ACSR x=-0.1524 h=10.5156 units=m "
                      " cond=2  wire=1/0_ACSR x=0.1524  h=8.2296  units=m "
                      " reduce=y ")

        expected = '1PH-x4_ACSRx4_ACSR'.lower()
        dss.lines_write_geometry(expected)
        actual = dss.lines_read_geometry()
        assert actual == expected

    def test_lines_read_spacing(self, dss):
        expected = ""
        actual = dss.lines_read_spacing()
        assert actual == expected

    def test_lines_write_spacing(self, dss):
        dss.text("new LineSpacing.500 nconds=4 nphases=3 units=ft x=[-4 -1 3 0] h=[28 28 28 24]")
        expected = "500"
        dss.lines_write_spacing(expected)
        actual = dss.lines_read_spacing()
        assert actual == expected

    # ===================================================================
    # Float methods
    # ===================================================================
    def test_lines_read_length(self, dss):
        expected = 2000
        actual = dss.lines_read_length()
        assert actual == expected

    def test_lines_write_length(self, dss):
        expected = 150
        dss.lines_write_length(expected)
        actual = dss.lines_read_length()
        assert actual == expected

    def test_lines_read_r1(self, dss):

        dss.text("New linecode.Sequences nphases=3 "
                      "r1=0.3489 x1=0.426198 r0=0.588811 x0=1.29612 "
                      "c1=10.4308823411236  c0=4.48501282215346  "
                      "units=km baseFreq=60 normamps=310  emergamps=310  "
                      "faultrate=0.1 pctperm=20 repair=3")

        dss.text("New line.MyLine linecode=Sequences length=1")
        dss.lines_write_name('MyLine')

        expected = 0.3489
        actual = dss.lines_read_r1()
        assert actual == expected

    def test_lines_write_r1(self, dss):
        dss.text("New linecode.Sequences nphases=3 "
                      "r1=0.3489 x1=0.426198 r0=0.588811 x0=1.29612 "
                      "c1=10.4308823411236  c0=4.48501282215346  "
                      "units=km baseFreq=60 normamps=310  emergamps=310  "
                      "faultrate=0.1 pctperm=20 repair=3")

        dss.text("New line.MyLine linecode=Sequences length=1")
        dss.lines_write_name('MyLine')

        expected = 0.1
        dss.lines_write_r1(expected)
        actual = dss.lines_read_r1()
        assert actual == expected

    def test_lines_read_x1(self, dss):
        dss.text("New linecode.Sequences nphases=3 "
                      "r1=0.3489 x1=0.426198 r0=0.588811 x0=1.29612 "
                      "c1=10.4308823411236  c0=4.48501282215346  "
                      "units=km baseFreq=60 normamps=310  emergamps=310  "
                      "faultrate=0.1 pctperm=20 repair=3")

        dss.text("New line.MyLine linecode=Sequences length=1")
        dss.lines_write_name('MyLine')

        expected = 0.426198
        actual = dss.lines_read_x1()
        assert actual == expected

    def test_lines_write_x1(self, dss):
        dss.text("New linecode.Sequences nphases=3 "
                      "r1=0.3489 x1=0.426198 r0=0.588811 x0=1.29612 "
                      "c1=10.4308823411236  c0=4.48501282215346  "
                      "units=km baseFreq=60 normamps=310  emergamps=310  "
                      "faultrate=0.1 pctperm=20 repair=3")

        dss.text("New line.MyLine linecode=Sequences length=1")
        dss.lines_write_name('MyLine')

        expected = 0.12
        dss.lines_write_x1(expected)
        actual = dss.lines_read_x1()
        assert actual == expected

    def test_lines_read_c1(self, dss):
        if platform.architecture()[0] == "64bit":
            expected = 0.0006439393939393939
            actual = dss.lines_read_c1()
            assert actual == expected
        else:
            assert True

    def test_lines_write_c1(self, dss):
        expected = 0.1
        dss.lines_write_c1(expected)
        actual = dss.lines_read_c1()
        assert expected == pytest.approx(actual)

    def test_lines_read_r0(self, dss):
        if platform.architecture()[0] == "64bit":
            expected = 3.378787878787879e-05
            actual = dss.lines_read_r0()
            assert actual == expected
        else:
            assert True

    def test_lines_write_r0(self, dss):
        expected = 2.5
        dss.lines_write_r0(expected)
        actual = dss.lines_read_r0()
        assert actual == expected

    def test_lines_read_x0(self, dss):
        if platform.architecture()[0] == "64bit":
            expected = 7.664772727272727e-05
            actual = dss.lines_read_x0()
            assert actual == expected
        else:
            assert True

    def test_lines_write_x0(self, dss):
        expected = 0.12
        dss.lines_write_x0(expected)
        actual = dss.lines_read_x0()
        assert round(actual, 2) == expected

    def test_lines_read_c0(self, dss):
        if platform.architecture()[0] == "64bit":
            expected = 0.0003030303030303031
            actual = dss.lines_read_c0()
            assert actual == expected
        else:
            assert True

    def test_lines_write_c0(self, dss):
        expected = 0.1
        dss.lines_write_c0(expected)
        actual = dss.lines_read_c0()
        assert expected == pytest.approx(actual)

    def test_lines_read_norm_amps(self, dss):
        expected = 400
        actual = dss.lines_read_norm_amps()
        assert actual == expected

    def test_lines_write_norm_amps(self, dss):
        expected = 500
        dss.lines_write_norm_amps(expected)
        actual = dss.lines_read_norm_amps()
        assert actual == expected

    def test_lines_read_emerg_amps(self, dss):
        expected = 600
        actual = dss.lines_read_emerg_amps()
        assert actual == expected

    def test_lines_write_emerg_amps(self, dss):
        expected = 500
        dss.lines_write_emerg_amps(expected)
        actual = dss.lines_read_emerg_amps()
        assert actual == expected

    def test_lines_read_rg(self, dss):
        expected = 0.01805
        actual = dss.lines_read_rg()
        assert actual == expected

    def test_lines_write_rg(self, dss):
        expected = 0.1
        dss.lines_write_rg(expected)
        actual = dss.lines_read_rg()
        assert actual == expected

    def test_lines_read_xg(self, dss):
        expected = 0.155081
        actual = dss.lines_read_xg()
        assert actual == expected

    def test_lines_write_xg(self, dss):
        expected = 0.1
        dss.lines_write_xg(expected)
        actual = dss.lines_read_xg()
        assert actual == expected

    def test_lines_read_rho(self, dss):
        expected = 100
        actual = dss.lines_read_rho()
        assert actual == expected

    def test_lines_write_rho(self, dss):
        expected = 0.1
        dss.lines_write_rho(expected)
        actual = dss.lines_read_rho()
        assert actual == expected

    def test_lines_read_season_rating(self, dss):
        expected = 400
        actual = dss.lines_read_season_rating()
        assert actual == expected

    # ===================================================================
    # Variant methods
    # ===================================================================
    def test_lines_all_names(self, dss):
        expected = ['650632', '632670', '670671', '671680', '632633', '632645', '645646', '692675', '671684', '684611',
                    '684652', '671692']
        actual = dss.lines_all_names()
        assert actual == expected

    def test_lines_read_rmatrix(self, dss):
        if platform.architecture()[0] == "64bit":
            expected = [6.5625e-05,
                        2.9545454545454545e-05,
                        2.9924242424242424e-05,
                        2.9545454545454545e-05,
                        6.392045454545455e-05,
                        2.9071969696969698e-05,
                        2.9924242424242424e-05,
                        2.9071969696969698e-05,
                        6.46590909090909e-05]
            actual = dss.lines_read_rmatrix()
            assert actual == expected
        else:
            assert True

    # TODO
    # def test_lines_write_rmatrix(self, dss):
    #     if platform.architecture()[0] == "64bit":
    #         expected = [1.3569, 0.4591, 0.0, 0.4591, 1.3471, 0.0, 0.0, 0.0, 0.0]
    #         dss.lines_write_rmatrix("[1.3569 | 0.4591 1.3471]")
    #         actual = dss.lines_read_rmatrix()
    #         assert actual == expected
    #     else:
    #         assert True

    def test_lines_read_xmatrix(self, dss):
        if platform.architecture()[0] == "64bit":
            expected = [0.00019278409090909093,
                        9.50189393939394e-05,
                        8.022727272727272e-05,
                        9.50189393939394e-05,
                        0.0001984469696969697,
                        7.289772727272727e-05,
                        8.022727272727272e-05,
                        7.289772727272727e-05,
                        0.00019598484848484847]
            actual = dss.lines_read_xmatrix()
            assert actual == expected
        else:
            assert True

    def test_lines_write_xmatrix(self, dss):
        if platform.architecture()[0] == "64bit":
            expected = [1.3569, 0.4591, 0.0, 0.4591, 1.3471, 0.0, 0.0, 0.0, 0.0]
            dss.lines_write_xmatrix("[1.3569 | 0.4591 1.3471]")
            actual = dss.lines_read_xmatrix()
            assert actual == expected
        else:
            assert True

    def test_lines_read_yprim(self, dss):
        if platform.architecture()[0] == "64bit":
            expected = [1.1451220523783032,
                        -3.3006005308153297,
                        -0.48585754602498915,
                        1.22029123063551,
                        -0.2660589098474314,
                        0.912216808259467,
                        -1.1451220523783032,
                        3.300600730734862,
                        0.48585754602498915,
                        -1.2202912734754099,
                        0.2660589098474314,
                        -0.9122168510993669,
                        -0.48585754602498915,
                        1.22029123063551,
                        1.0027111809933547,
                        -3.1276449753401,
                        -0.12630483115283336,
                        0.6967002366036674,
                        0.48585754602498915,
                        -1.2202912734754099,
                        -1.0027111809933547,
                        3.1276451752596324,
                        0.12630483115283336,
                        -0.6967002794435673,
                        -0.2660589098474314,
                        0.912216808259467,
                        -0.12630483115283336,
                        0.6967002366036674,
                        0.8867184358481344,
                        -2.95059355831667,
                        0.2660589098474314,
                        -0.9122168510993669,
                        0.12630483115283336,
                        -0.6967002794435673,
                        -0.8867184358481344,
                        2.9505937582362023,
                        -1.1451220523783032,
                        3.300600730734862,
                        0.48585754602498915,
                        -1.2202912734754099,
                        0.2660589098474314,
                        -0.9122168510993669,
                        1.1451220523783032,
                        -3.3006005308153297,
                        -0.48585754602498915,
                        1.22029123063551,
                        -0.2660589098474314,
                        0.912216808259467,
                        0.48585754602498915,
                        -1.2202912734754099,
                        -1.0027111809933547,
                        3.1276451752596324,
                        0.12630483115283336,
                        -0.6967002794435673,
                        -0.48585754602498915,
                        1.22029123063551,
                        1.0027111809933547,
                        -3.1276449753401,
                        -0.12630483115283336,
                        0.6967002366036674,
                        0.2660589098474314,
                        -0.9122168510993669,
                        0.12630483115283336,
                        -0.6967002794435673,
                        -0.8867184358481344,
                        2.9505937582362023,
                        -0.2660589098474314,
                        0.912216808259467,
                        -0.12630483115283336,
                        0.6967002366036674,
                        0.8867184358481344,
                        -2.95059355831667]
            actual = dss.lines_read_yprim()
            assert actual == expected
        else:
            assert True

    # TODO understand it
    def test_lines_write_yprim(self, dss):
        assert True
        # if platform.architecture()[0] == "64bit":
        #     expected = [1.3569, 0.4591, 0.0, 0.4591, 1.3471, 0.0, 0.0, 0.0, 0.0]
        #     dss.lines_write_yprim("[1.3569 | 0.4591 1.3471]")
        #     actual = dss.lines_read_yprim()
        #     assert actual == expected
        # else:
        #     assert True
