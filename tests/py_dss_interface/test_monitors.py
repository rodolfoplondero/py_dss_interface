# -*- coding: utf-8 -*-
# @Time    : 8/26/2021 08:20 PM
# @Author  : Rodolfo Londero
# @Email   : rodolfpl@gmail.com
# @File    : test_monitors.py
# @Software: PyCharm


import os

import pytest

path = os.path.dirname(os.path.abspath(__file__))


class TestMonitors13Bus:

    @pytest.fixture(autouse=True)
    def _request(self, solve_snap_13bus):
        self.dss = solve_snap_13bus
        self.dss.text(
            "New Loadshape.1 npts=24 interval=1 mult=(0.18000001 0.19000000 0.23999999 0.33000001 0.38999999 0.41000000 0.64999998 1.23000002 1.88999999 1.88999999 1.96000004 1.98000002 1.45000005 1.62000000 1.88999999 1.79999995 1.78999996 1.19000006 0.80000001 0.66000003 0.51999998 0.40000001 0.28000000 0.23000000)")
        self.dss.loads_write_daily("1")
        self.dss.text("New monitor.m1 element=Transformer.XFM1 terminal=1 mode=0")
        self.dss.text(f"Set DataPath={path}")
        self.dss.text("Set maxcontrol=100")
        self.dss.text("Set maxiterations=100")
        self.dss.text("Set controlmode=off")
        self.dss.text("Set mode=daily stepsize=1.0h number=24")

        self.dss.solution_solve()

    # ===================================================================
    # Integer methods
    # ===================================================================
    def test_monitors_first(self):
        expected = 1
        actual = self.dss.monitors_first()
        assert expected == actual

    def test_monitors_next(self):
        expected = 0
        actual = self.dss.monitors_next()
        assert expected == actual

    def test_monitors_count(self):
        expected = 1
        actual = self.dss.monitors_count()
        assert expected == actual

    def test_monitors_reset(self):
        expected = 0
        actual = self.dss.monitors_reset()
        assert expected == actual

    def test_monitors_reset_all(self):
        expected = 0
        actual = self.dss.monitors_reset_all()
        assert expected == actual

    def test_monitors_sample(self):
        expected = 0
        actual = self.dss.monitors_sample()
        assert expected == actual

    def test_monitors_sample_all(self):
        expected = 0
        actual = self.dss.monitors_sample_all()
        assert expected == actual

    def test_monitors_save(self):
        expected = 0
        actual = self.dss.monitors_save()
        assert expected == actual

    def test_monitors_save_all(self):
        expected = 0
        actual = self.dss.monitors_save_all()
        assert expected == actual

    def test_monitors_process(self):
        expected = 0
        actual = self.dss.monitors_process()
        assert expected == actual

    def test_monitors_process_all(self):
        expected = 0
        actual = self.dss.monitors_process_all()
        assert expected == actual

    def test_monitors_file_version(self):
        # TODO: file_version returns diferent values each time
        expected = 0
        actual = self.dss.monitors_file_version()
        assert type(expected) == type(actual)

    def test_monitors_sample_count(self):
        expected = 24
        actual = self.dss.monitors_sample_count()
        assert expected == actual

    def test_monitors_record_size(self):
        expected = 16
        actual = self.dss.monitors_record_size()
        assert expected == actual

    def test_monitors_num_channels(self):
        expected = 16
        actual = self.dss.monitors_num_channels()
        assert expected == actual

    def test_monitors_read_terminal(self):
        expected = 1
        actual = self.dss.monitors_read_terminal()
        assert expected == actual

    def test_monitors_write_terminal(self):
        expected = 2
        self.dss.monitors_write_terminal(expected)
        actual = self.dss.monitors_read_terminal()
        assert expected == actual

    # ===================================================================
    # String methods
    # ===================================================================
    def test_monitors_file_name(self):
        expected = os.path.join(path, "IEEE13Nodeckt_Mon_m1_1.csv")
        actual = self.dss.monitors_file_name()
        assert expected.lower() == actual.lower()

    def test_monitors_read_name(self):
        expected = "m1"
        actual = self.dss.monitors_read_name()
        assert expected.lower() == actual.lower()

    def test_monitors_write_name(self):
        self.dss.text("New monitor.m2 element=Transformer.XFM1 terminal=2 mode=0")
        expected = "m2"
        self.dss.monitors_write_name(expected)
        actual = self.dss.monitors_read_name()
        assert expected.lower() == actual.lower()

    def test_monitors_read_element(self):
        expected = "transformer.xfm1"
        actual = self.dss.monitors_read_element()
        assert expected == actual

    def test_monitors_write_element(self):
        expected = "load.671"
        self.dss.monitors_write_element(expected)
        actual = self.dss.monitors_read_element()
        assert expected == actual

    # ===================================================================
    # Variant methods
    # ===================================================================
    def test_monitors_all_names(self):
        self.dss.text("New monitor.m2 element=Transformer.XFM1 terminal=2 mode=0")
        expected = ["m1", "m2"]
        actual = self.dss.monitors_all_names()
        assert expected == actual

    def test_monitors_byte_stream(self):
        expected = [1.0, 0.0, 2421.029296875, -2.5194942951202393, 2467.319091796875, -121.98504638671875,
                    2422.07373046875, 118.06017303466797, 0.0, 0.0, 82.16896057128906, -37.71780014038086,
                    61.92161178588867, -159.3227996826172, 63.10896682739258, 80.70452880859375, 19.873741149902344,
                    150.27825927734375, 2.0, 0.0, 2421.117919921875, -2.520747661590576, 2467.32275390625,
                    -121.9826889038086, 2421.857177734375, 118.05648040771484, 0.0, 0.0, 82.17206573486328,
                    -37.719139099121094, 61.91514205932617, -159.32041931152344, 63.12112808227539, 80.70069122314453,
                    19.88237953186035, 150.31826782226562, 3.0, 0.0, 2421.585693359375, -2.5253043174743652,
                    2467.283935546875, -121.97196960449219, 2420.87158203125, 118.03865814208984, 0.0, 0.0,
                    82.15995788574219, -37.723472595214844, 61.91516876220703, -159.3096923828125, 63.1425666809082,
                    80.68254852294922, 19.88970947265625, 150.36199951171875, 4.0, 0.0, 2422.457275390625,
                    -2.5332934856414795, 2467.200927734375, -121.95232391357422, 2419.06005859375, 118.00572967529297,
                    0.0, 0.0, 82.12516784667969, -37.73091506958008, 61.917884826660156, -159.29010009765625,
                    63.19671630859375, 80.64881134033203, 19.884477615356445, 150.48422241210938, 5.0, 0.0,
                    2423.020263671875, -2.53878116607666, 2467.15478515625, -121.93942260742188, 2417.873046875,
                    117.98429107666016, 0.0, 0.0, 82.11001586914062, -37.736122131347656, 61.918338775634766,
                    -159.27719116210938, 63.22242736816406, 80.6269760131836, 19.892608642578125, 150.53590393066406,
                    6.0, 0.0, 2423.222900390625, -2.540499210357666, 2467.1328125, -121.93495178222656,
                    2417.458740234375, 117.97672271728516, 0.0, 0.0, 82.09847259521484, -37.73767852783203,
                    61.91971969604492, -159.27273559570312, 63.23906707763672, 80.61915588378906, 19.886070251464844,
                    150.57598876953125, 7.0, 0.0, 2425.524658203125, -2.5623912811279297, 2466.93798828125,
                    -121.88257598876953, 2412.626220703125, 117.88941955566406, 0.0, 0.0, 82.0192642211914,
                    -37.758262634277344, 61.92387390136719, -159.22042846679688, 63.36859893798828, 80.5299072265625,
                    19.892793655395508, 150.85923767089844, 8.0, 0.0, 2431.141357421875, -2.616452693939209,
                    2466.50537109375, -121.75447082519531, 2400.76904296875, 117.67639923095703, 0.0, 0.0,
                    81.81747436523438, -37.80904006958008, 61.93586349487305, -159.09249877929688, 63.69696044921875,
                    80.31189727783203, 19.89999771118164, 151.58139038085938, 9.0, 0.0, 2437.585205078125,
                    -2.6805014610290527, 2466.105224609375, -121.60638427734375, 2387.002197265625, 117.4315185546875,
                    0.0, 0.0, 81.59091186523438, -37.869388580322266, 61.94626235961914, -158.944580078125,
                    64.0782699584961, 80.06120300292969, 19.92245101928711, 152.41769409179688, 10.0, 0.0,
                    2437.591796875, -2.6804535388946533, 2466.102294921875, -121.60631561279297, 2386.993896484375,
                    117.43134307861328, 0.0, 0.0, 81.58792877197266, -37.86931228637695, 61.94704818725586,
                    -158.94451904296875, 64.0814437866211, 80.06095886230469, 19.918373107910156, 152.42666625976562,
                    11.0, 0.0, 2438.275390625, -2.6874260902404785, 2466.06689453125, -121.59049987792969,
                    2385.5205078125, 117.4052963256836, 0.0, 0.0, 81.5654525756836, -37.87590789794922,
                    61.947669982910156, -158.9287109375, 64.12071228027344, 80.0343246459961, 19.923526763916016,
                    152.51138305664062, 12.0, 0.0, 2438.469482421875, -2.6894185543060303, 2466.05712890625,
                    -121.58600616455078, 2385.1015625, 117.39789581298828, 0.0, 0.0, 81.5594253540039,
                    -37.87779235839844, 61.94796371459961, -158.92420959472656, 64.13093566894531, 80.02677154541016,
                    19.925548553466797, 152.53237915039062,
                    13.0, 0.0, 2433.29296875, -2.6374106407165527, 2466.35595703125, -121.70528411865234,
                    2396.201904296875, 117.59481811523438, 0.0, 0.0, 81.73699188232422, -37.82870864868164,
                    61.94108963012695, -159.04339599609375, 63.82758331298828, 80.22830200195312, 19.8994083404541,
                    151.87060546875, 14.0, 0.0, 2434.937744140625, -2.653989553451538, 2466.25830078125,
                    -121.66732788085938, 2392.6767578125, 117.53215026855469, 0.0, 0.0, 81.68505859375,
                    -37.84440612792969, 61.942161560058594, -159.00546264648438, 63.918724060058594, 80.1642837524414,
                    19.913955688476562, 152.0662078857422, 15.0, 0.0, 2437.576171875, -2.680544137954712,
                    2466.1083984375, -121.60650634765625, 2387.01513671875, 117.43177032470703, 0.0, 0.0,
                    81.59464263916016, -37.869468688964844, 61.94562530517578, -158.94468688964844, 64.07337188720703,
                    80.06156158447266, 19.92755126953125, 152.40325927734375, 16.0, 0.0, 2436.714111328125,
                    -2.6715283393859863, 2466.149169921875, -121.62660217285156, 2388.8828125, 117.46477508544922, 0.0,
                    0.0, 81.61665344238281, -37.86086654663086, 61.9462776184082, -158.9647979736328, 64.0312728881836,
                    80.09513854980469, 19.91167449951172, 152.31838989257812, 17.0, 0.0, 2436.614501953125,
                    -2.670560121536255, 2466.155517578125, -121.62887573242188, 2389.094970703125, 117.46855163574219,
                    0.0, 0.0, 81.62095642089844, -37.859962463378906, 61.94585418701172, -158.96707153320312,
                    64.0246353149414, 80.0990219116211, 19.91246795654297, 152.3034210205078, 18.0, 0.0, 2430.763671875,
                    -2.612550973892212, 2466.527099609375, -121.76325988769531, 2401.58203125, 117.69087219238281, 0.0,
                    0.0, 81.82608032226562, -37.805301666259766, 61.93674087524414, -159.10130310058594,
                    63.678993225097656, 80.32662200927734, 19.8918514251709, 151.5443115234375, 19.0, 0.0,
                    2427.002197265625, -2.5759007930755615, 2466.80419921875, -121.84933471679688, 2409.54931640625,
                    117.83375549316406, 0.0, 0.0, 81.95330047607422, -37.77075958251953, 61.9310302734375,
                    -159.1873016357422, 63.466514587402344, 80.47271728515625, 19.874542236328125, 151.08175659179688,
                    20.0, 0.0, 2425.6396484375, -2.563122034072876, 2466.920166015625, -121.88020324707031,
                    2412.404052734375, 117.8852767944336, 0.0, 0.0, 82.00704956054688, -37.75883483886719,
                    61.926605224609375, -159.21810913085938, 63.38277816772461, 80.52552795410156, 19.880558013916016,
                    150.89466857910156, 21.0, 0.0, 2424.292236328125, -2.5503411293029785, 2467.033935546875,
                    -121.91083526611328, 2415.232177734375, 117.93634033203125, 0.0, 0.0, 82.05499267578125,
                    -37.74683380126953, 61.923648834228516, -159.24868774414062, 63.30552291870117, 80.57776641845703,
                    19.878847122192383, 150.72508239746094, 22.0, 0.0, 2423.138671875, -2.539484739303589,
                    2467.13525390625, -121.93701171875, 2417.64697265625, 117.98004150390625, 0.0, 0.0,
                    82.09647369384766, -37.736656188964844, 61.92090606689453, -159.2748260498047, 63.23932647705078,
                    80.62246704101562, 19.8782901763916, 150.57962036132812, 23.0, 0.0, 2421.988037109375,
                    -2.528700351715088, 2467.23876953125, -121.96309661865234, 2420.05126953125, 118.02362060546875,
                    0.0, 0.0, 82.1374740600586, -37.72654342651367, 61.918216705322266, -159.30087280273438,
                    63.17396545410156, 80.66703796386719, 19.877370834350586, 150.43624877929688, 24.0, 0.0,
                    2421.51708984375, -2.524174690246582, 2467.279296875, -121.97383880615234, 2421.039794921875,
                    118.04151916503906, 0.0, 0.0, 82.15107727050781, -37.722259521484375, 61.91755294799805,
                    -159.31161499023438, 63.15162658691406, 80.6852798461914, 19.87207794189453, 150.39059448242188]

        self.dss.monitors_save()

        actual = list()
        for i in self.dss.monitors_byte_stream().values.tolist():
            for j in i:
                actual.append(j)

        assert expected == actual

    def test_monitors_header(self):
        expected = [' V1', ' VAngle1', ' V2', ' VAngle2', ' V3', ' VAngle3', ' V4', ' VAngle4',
                    ' I1', ' IAngle1', ' I2', ' IAngle2', ' I3', ' IAngle3', ' I4', ' IAngle4\x00']
        actual = self.dss.monitors_header()
        assert expected == actual

    def test_monitors_dbl_hour(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        actual = self.dss.monitors_dbl_hour()
        assert expected == actual

    def test_monitors_dbl_freq(self):
        expected = [0.0]
        actual = self.dss.monitors_dbl_freq()
        assert expected == actual

    def test_monitors_channel(self):
        expected = [2421.03, 2421.12, 2421.59, 2422.46, 2423.02, 2423.22, 2425.52, 2431.14, 2437.59, 2437.59, 2438.28,
                    2438.47, 2433.29, 2434.94, 2437.58, 2436.71, 2436.61, 2430.76, 2427, 2425.64, 2424.29, 2423.14,
                    2421.99, 2421.52]
        # self.dss.monitors_save_all()
        actual = self.dss.monitors_channel(1)
        assert [round(value, 2) for value in actual] == [round(value, 2) for value in expected]

