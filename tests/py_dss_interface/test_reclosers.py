# -*- coding: utf-8 -*-
# @Time     : 09/07/2021 02:16 AM
# @Author   : Rodolfo Londero
# @Email    : rodolfopl@gmail.com
# @File     : test_reclosers.py
# @Software : VSCode

import pytest


class TestReclosers13Bus:

    @pytest.fixture(scope='function')
    def dss(self, solve_snap_13bus):
        dss = solve_snap_13bus
        dss.text(r"New Recloser.cb1 MonitoredObj=Line.650632 "
                      r"MonitoredTerm=1  "
                      r"NumFast=4       "
                      r"PhaseFast=Ext_Inv "
                      r"PhaseDelayed=Ext_Inv "
                      r"PhaseTrip=800 "
                      r"TDPhFast=1 "
                      r"TDPhDelayed=1 "
                      r"PhaseInst=2400 "
                      r"GroundFast=Ext_Inv "
                      r"GroundDelayed=Ext_Inv "
                      r"GroundTrip=800 "
                      r"TDGrFast=1 "
                      r"TDGrDelayed=1 "
                      r"GroundInst=1200 "
                      r"Shots=4 "
                      r"RecloseIntervals=(0.5, 2, 2, )")
        dss.solution_solve()
        dss.reclosers_write_name('cb1')

        return dss

    # ===================================================================
    # Integer methods
    # ===================================================================
    def test_reclosers_count(self, dss):
        dss.text(r"New 'Recloser.cb2' MonitoredObj=Line.684611 "
                      r"MonitoredTerm=2 "
                      r"NumFast=4 "
                      r"PhaseFast=Ext_Inv "
                      r"PhaseDelayed=Ext_Inv "
                      r"PhaseTrip=800 "
                      r"TDPhFast=1 "
                      r"TDPhDelayed=1 "
                      r"PhaseInst=2400 "
                      r"GroundFast=Ext_Inv "
                      r"GroundDelayed=Ext_Inv "
                      r"GroundTrip=800 "
                      r"TDGrFast=1 "
                      r"TDGrDelayed=1 "
                      r"GroundInst=1200 "
                      r"Shots=4 "
                      r"RecloseIntervals=(0.5, 2, 2, )")
        expected = 2
        actual = dss.reclosers_count()
        assert actual == expected

    def test_reclosers_first(self, dss):
        expected = 1
        actual = dss.reclosers_first()
        assert actual == expected

    def test_reclosers_next(self, dss):
        dss.text(r"New 'Recloser.cb2' MonitoredObj=Line.684611 "
                      r"MonitoredTerm=2 "
                      r"NumFast=4 "
                      r"PhaseFast=Ext_Inv "
                      r"PhaseDelayed=Ext_Inv "
                      r"PhaseTrip=800 "
                      r"TDPhFast=1 "
                      r"TDPhDelayed=1 "
                      r"PhaseInst=2400 "
                      r"GroundFast=Ext_Inv "
                      r"GroundDelayed=Ext_Inv "
                      r"GroundTrip=800 "
                      r"TDGrFast=1 "
                      r"TDGrDelayed=1 "
                      r"GroundInst=1200 "
                      r"Shots=4 "
                      r"RecloseIntervals=(0.5, 2, 2, )")
        expected = 2
        dss.reclosers_first()
        actual = dss.reclosers_next()
        assert actual == expected

    def test_reclosers_read_monitored_term(self, dss):
        expected = 1
        actual = dss.reclosers_read_monitored_term()
        assert actual == expected

    def test_reclosers_write_monitored_term(self, dss):
        expected = 2
        dss.reclosers_write_monitored_term(expected)
        actual = dss.reclosers_read_monitored_term()
        assert actual == expected

    def test_reclosers_read_switched_term(self, dss):
        expected = 1
        actual = dss.reclosers_read_switched_term()
        assert actual == expected

    def test_reclosers_write_switched_term(self, dss):
        expected = 2
        dss.reclosers_write_switched_term(expected)
        actual = dss.reclosers_read_switched_term()
        assert actual == expected

    def test_reclosers_read_num_fast(self, dss):
        expected = 4
        actual = dss.reclosers_read_num_fast()
        assert actual == expected

    def test_reclosers_write_num_fast(self, dss):
        expected = 1
        dss.reclosers_write_num_fast(expected)
        actual = dss.reclosers_read_num_fast()
        assert actual == expected

    def test_reclosers_read_shots(self, dss):
        expected = 4
        actual = dss.reclosers_read_shots()
        assert actual == expected

    def test_reclosers_write_shots(self, dss):
        expected = 3
        dss.reclosers_write_shots(expected)
        actual = dss.reclosers_read_shots()
        assert actual == expected

    def test_reclosers_open(self, dss):
        expected = 0
        actual = dss.reclosers_open()
        assert actual == expected

    def test_reclosers_close(self, dss):
        expected = 0
        actual = dss.reclosers_close()
        assert actual == expected

    def test_reclosers_read_idx(self, dss):
        expected = 1
        actual = dss.reclosers_read_idx()
        assert actual == expected

    def test_reclosers_write_idx(self, dss):
        dss.text(r"New 'Recloser.cb2' MonitoredObj=Line.684611 "
                      r"MonitoredTerm=2 "
                      r"NumFast=4 "
                      r"PhaseFast=Ext_Inv "
                      r"PhaseDelayed=Ext_Inv "
                      r"PhaseTrip=800 "
                      r"TDPhFast=1 "
                      r"TDPhDelayed=1 "
                      r"PhaseInst=2400 "
                      r"GroundFast=Ext_Inv "
                      r"GroundDelayed=Ext_Inv "
                      r"GroundTrip=800 "
                      r"TDGrFast=1 "
                      r"TDGrDelayed=1 "
                      r"GroundInst=1200 "
                      r"Shots=4 "
                      r"RecloseIntervals=(0.5, 2, 2, )")
        expected = 2
        dss.reclosers_write_idx(expected)
        actual = dss.reclosers_read_idx()
        assert actual == expected

    # ===================================================================
    # Float methods
    # ===================================================================
    def test_reclosers_read_phase_trip(self, dss):
        expected = 800
        actual = dss.reclosers_read_phase_trip()
        assert actual == expected

    def test_reclosers_write_phase_trip(self, dss):
        expected = 700
        dss.reclosers_write_phase_trip(expected)
        actual = dss.reclosers_read_phase_trip()
        assert actual == expected

    def test_reclosers_read_phase_inst(self, dss):
        expected = 2400
        actual = dss.reclosers_read_phase_inst()
        assert actual == expected

    def test_reclosers_write_phase_inst(self, dss):
        expected = 1200
        dss.reclosers_write_phase_inst(expected)
        actual = dss.reclosers_read_phase_inst()
        assert actual == expected

    def test_reclosers_read_ground_trip(self, dss):
        expected = 800
        actual = dss.reclosers_read_ground_trip()
        assert actual == expected

    def test_reclosers_write_ground_trip(self, dss):
        expected = 700
        dss.reclosers_write_ground_trip(expected)
        actual = dss.reclosers_read_ground_trip()
        assert actual == expected

    def test_reclosers_read_ground_inst(self, dss):
        expected = 1200
        actual = dss.reclosers_read_ground_inst()
        assert actual == expected

    def test_reclosers_write_ground_inst(self, dss):
        expected = 1900
        dss.reclosers_write_ground_inst(expected)
        actual = dss.reclosers_read_ground_inst()
        assert actual == expected

    # ===================================================================
    # String methods
    # ===================================================================
    def test_reclosers_read_name(self, dss):
        expected = 'cb1'
        actual = dss.reclosers_read_name()
        assert actual == expected

    def test_reclosers_write_name(self, dss):
        dss.text(r"New 'Recloser.cb2' MonitoredObj=Line.684611 "
                      r"MonitoredTerm=2 "
                      r"NumFast=4 "
                      r"PhaseFast=Ext_Inv "
                      r"PhaseDelayed=Ext_Inv "
                      r"PhaseTrip=800 "
                      r"TDPhFast=1 "
                      r"TDPhDelayed=1 "
                      r"PhaseInst=2400 "
                      r"GroundFast=Ext_Inv "
                      r"GroundDelayed=Ext_Inv "
                      r"GroundTrip=800 "
                      r"TDGrFast=1 "
                      r"TDGrDelayed=1 "
                      r"GroundInst=1200 "
                      r"Shots=4 "
                      r"RecloseIntervals=(0.5, 2, 2, )")
        expected = 'cb2'
        dss.reclosers_write_name(expected)
        actual = dss.reclosers_read_name()
        assert actual == expected

    def test_reclosers_read_monitored_obj(self, dss):
        expected = 'line.650632'
        actual = dss.reclosers_read_monitored_obj()
        assert actual == expected

    def test_reclosers_write_monitored_obj(self, dss):
        expected = 'line.684652'
        dss.reclosers_write_monitored_obj(expected)
        actual = dss.reclosers_read_monitored_obj()
        assert actual == expected

    def test_reclosers_read_switched_obj(self, dss):
        expected = 'line.650632'
        actual = dss.reclosers_read_switched_obj()
        assert actual == expected

    def test_reclosers_write_switched_obj(self, dss):
        expected = 'line.684652'
        dss.reclosers_write_switched_obj(expected)
        actual = dss.reclosers_read_switched_obj()
        assert actual == expected

    # ===================================================================
    # Variant methods
    # ===================================================================
    def test_reclosers_all_names(self, dss):
        dss.text(r"New 'Recloser.cb2' MonitoredObj=Line.684611 "
                      r"MonitoredTerm=2 "
                      r"NumFast=4 "
                      r"PhaseFast=Ext_Inv "
                      r"PhaseDelayed=Ext_Inv "
                      r"PhaseTrip=800 "
                      r"TDPhFast=1 "
                      r"TDPhDelayed=1 "
                      r"PhaseInst=2400 "
                      r"GroundFast=Ext_Inv "
                      r"GroundDelayed=Ext_Inv "
                      r"GroundTrip=800 "
                      r"TDGrFast=1 "
                      r"TDGrDelayed=1 "
                      r"GroundInst=1200 "
                      r"Shots=4 "
                      r"RecloseIntervals=(0.5, 2, 2, )")
        expected = ['cb1', 'cb2']
        actual = dss.reclosers_all_names()
        assert actual == expected

    def test_reclosers_reclose_intervals(self, dss):
        expected = [0.5, 2, 2]
        actual = dss.reclosers_reclose_intervals()
        assert actual == expected
