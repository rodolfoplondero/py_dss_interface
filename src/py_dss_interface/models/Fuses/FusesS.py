# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes
from py_dss_interface.models.Base import Base


class FusesS(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        CStr FusesS(int32_t Parameter, CStr Argument);

    This interface returns a string with the result of the query according to the value of the variable Parameter,
    which can be one of the following.
    """

    def fuses_read_name(self):
        """Gets the name of the active fuse."""
        result = ctypes.c_char_p(self.dss_obj.FusesS(ctypes.c_int32(0), ctypes.c_int32(0)))
        return result.value.decode('ascii')

    def fuses_write_name(self, argument):
        """Sets the name of the active fuse."""
        result = ctypes.c_char_p(self.dss_obj.FusesS(ctypes.c_int32(1), argument.encode('ascii')))
        return result.value.decode('ascii')

    def fuses_read_monitored_obj(self):
        """Gets the name of the Monitored Object by the active fuse."""
        result = ctypes.c_char_p(self.dss_obj.FusesS(ctypes.c_int32(2), ctypes.c_int32(0)))
        return result.value.decode('ascii')

    def fuses_write_monitored_obj(self, argument):
        """Sets the name of the Monitored Object by the active fuse."""
        result = ctypes.c_char_p(self.dss_obj.FusesS(ctypes.c_int32(3), argument.encode('ascii')))
        return result.value.decode('ascii')

    def fuses_read_switched_obj(self):
        """Gets the full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj."""
        result = ctypes.c_char_p(self.dss_obj.FusesS(ctypes.c_int32(4), ctypes.c_int32(0)))
        return result.value.decode('ascii')

    def fuses_write_switched_obj(self, argument):
        """Sets the full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj."""
        result = ctypes.c_char_p(self.dss_obj.FusesS(ctypes.c_int32(5), argument.encode('ascii')))
        return result.value.decode('ascii')

    def fuses_read_tcc_curve(self):
        """Gets the name of the TCCcurve object that determines fuse blowing."""
        result = ctypes.c_char_p(self.dss_obj.FusesS(ctypes.c_int32(6), ctypes.c_int32(0)))
        return result.value.decode('ascii')

    def fuses_write_tcc_curve(self, argument):
        """Sets the name of the TCCcurve object that determines fuse blowing."""
        result = ctypes.c_char_p(self.dss_obj.FusesS(ctypes.c_int32(7), argument.encode('ascii')))
        return result.value.decode('ascii')
