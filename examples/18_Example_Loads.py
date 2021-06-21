# -*- encoding: utf-8 -*-
"""
 Created by Ênio Viana at 15/05/2021
"""
from py_dss_interface.models.Example.ExampleBase import ExampleBase

dss = ExampleBase("13").dss

# Integer methods
print(45 * '=' + ' Integer Methods' + 45 * '=')
print(f'dss.loads_first(): {dss.loads_first()}')
print(f'dss.loads_next(): {dss.loads_next()}')
print(f'dss.loads_read_idx(): {dss.loads_read_idx()}')
print(f'dss.loads_write_idx(): {dss.loads_write_idx(1)}')
print(f'dss.loads_count(): {dss.loads_count()}')
print(f'dss.loads_read_class(): {dss.loads_read_class()}')
print(f'dss.loads_write_class(): {dss.loads_write_class(1)}')
print(f'dss.loads_read_class(): {dss.loads_read_class()}')
print(f'dss.loads_read_model(): {dss.loads_read_model()}')
print(f'dss.loads_write_model(): {dss.loads_write_model(2)}')
print(f'dss.loads_read_model(): {dss.loads_read_model()}')
print(f'dss.loads_read_num_cust(): {dss.loads_read_num_cust()}')
print(f'dss.loads_write_num_cust(): {dss.loads_write_num_cust(12)}')
print(f'dss.loads_read_num_cust(): {dss.loads_read_num_cust()}')
print(f'dss.loads_read_status(): {dss.loads_read_status()}')
print(f'dss.loads_write_status(): {dss.loads_write_status(1)}')
print(f'dss.loads_read_status(): {dss.loads_read_status()}')
print(f'dss.loads_read_is_delta(): {dss.loads_read_is_delta()}')
print(f'dss.loads_write_is_delta(): {dss.loads_write_is_delta(0)}')
print(f'dss.loads_read_is_delta(): {dss.loads_read_is_delta()}')

# String methods
print(45 * '=' + ' String Methods' + 45 * '=')
print(f'dss.loads_read_name(): {dss.loads_read_name()}')
print(f'dss.loads_write_name(): {dss.loads_write_name("634a")}')
print(f'dss.loads_read_name(): {dss.loads_read_name()}')
print(f'dss.loads_read_cvr_curve(): {dss.loads_read_cvr_curve()}')
# print(f'dss.loads_write_cvr_curve(): {dss.loads_write_cvr_curve("")}')
print(f'dss.loads_read_daily(): {dss.loads_read_daily()}')
# print(f'dss.loads_write_daily(): {dss.loads_write_daily("")}')
print(f'dss.loads_read_daily(): {dss.loads_read_daily()}')
print(f'dss.loads_read_duty(): {dss.loads_read_duty()}')
# print(f'dss.loads_write_duty(): {dss.loads_write_duty("12")}')
print(f'dss.loads_read_duty(): {dss.loads_read_duty()}')
print(f'dss.loads_read_spectrum(): {dss.loads_read_spectrum()}')
# print(f'dss.loads_write_spectrum(): {dss.loads_write_spectrum("")}')
print(f'dss.loads_read_spectrum(): {dss.loads_read_spectrum()}')
print(f'dss.loads_read_yearly(): {dss.loads_read_yearly()}')
# print(f'dss.loads_write_yearly(): {dss.loads_write_yearly("")}')
print(f'dss.loads_read_yearly(): {dss.loads_read_yearly()}')
print(f'dss.loads_read_growth(): {dss.loads_read_growth()}')
# print(f'dss.loads_write_growth(): {dss.loads_write_growth("")}')
print(f'dss.loads_read_growth(): {dss.loads_read_growth()}')

# Float methods
print(45 * '=' + ' Float Methods' + 45 * '=')
print(f'dss.loads_read_kw(): {dss.loads_read_kw()}')
print(f'dss.loads_write_kw(): {dss.loads_write_kw(123.1)}')
print(f'dss.loads_read_kw(): {dss.loads_read_kw()}')
print(f'dss.loads_read_kv(): {dss.loads_read_kv()}')
print(f'dss.loads_write_kv(): {dss.loads_write_kv(123.1)}')
print(f'dss.loads_read_kv(): {dss.loads_read_kv()}')
print(f'dss.loads_read_kvar(): {dss.loads_read_kvar()}')
print(f'dss.loads_write_kvar(): {dss.loads_write_kvar(123.1)}')
print(f'dss.loads_read_kvar(): {dss.loads_read_kvar()}')
print(f'dss.loads_read_pf(): {dss.loads_read_pf()}')
print(f'dss.loads_write_pf(): {dss.loads_write_pf(123.1)}')
print(f'dss.loads_read_pf(): {dss.loads_read_pf()}')
print(f'dss.loads_read_pct_mean(): {dss.loads_read_pct_mean()}')
print(f'dss.loads_write_pct_mean(): {dss.loads_write_pct_mean(123.1)}')
print(f'dss.loads_read_pct_mean(): {dss.loads_read_pct_mean()}')
print(f'dss.loads_read_pct_std_dev(): {dss.loads_read_pct_std_dev()}')
print(f'dss.loads_write_pct_std_dev(): {dss.loads_write_pct_std_dev(123.1)}')
print(f'dss.loads_read_pct_std_dev(): {dss.loads_read_pct_std_dev()}')
print(f'dss.loads_read_allocation_factor(): {dss.loads_read_allocation_factor()}')
print(f'dss.loads_write_allocation_factor(): {dss.loads_write_allocation_factor(123.1)}')
print(f'dss.loads_read_allocation_factor(): {dss.loads_read_allocation_factor()}')
print(f'dss.loads_read_c_factor(): {dss.loads_read_c_factor()}')
print(f'dss.loads_write_c_factor(): {dss.loads_write_c_factor(123.1)}')
print(f'dss.loads_read_c_factor(): {dss.loads_read_c_factor()}')
print(f'dss.loads_read_cvr_watts(): {dss.loads_read_cvr_watts()}')
print(f'dss.loads_write_cvr_watts(): {dss.loads_write_cvr_watts(123.1)}')
print(f'dss.loads_read_cvr_watts(): {dss.loads_read_cvr_watts()}')
print(f'dss.loads_read_cvr_vars(): {dss.loads_read_cvr_vars()}')
print(f'dss.loads_write_cvr_vars(): {dss.loads_write_cvr_vars(123.1)}')
print(f'dss.loads_read_cvr_vars(): {dss.loads_read_cvr_vars()}')
print(f'dss.loads_read_kva(): {dss.loads_read_kva()}')
print(f'dss.loads_write_kva(): {dss.loads_write_kva(123.1)}')
print(f'dss.loads_read_kva(): {dss.loads_read_kva()}')
print(f'dss.loads_read_kwh(): {dss.loads_read_kwh()}')
print(f'dss.loads_write_kwh(): {dss.loads_write_kwh(123.1)}')
print(f'dss.loads_read_kwh(): {dss.loads_read_kwh()}')
print(f'dss.loads_read_kwh_days(): {dss.loads_read_kwh_days()}')
print(f'dss.loads_write_kwh_days(): {dss.loads_write_kwh_days(123.1)}')
print(f'dss.loads_read_kwh_days(): {dss.loads_read_kwh_days()}')
print(f'dss.loads_read_r_neut(): {dss.loads_read_r_neut()}')
print(f'dss.loads_write_r_neut(): {dss.loads_write_r_neut(123.1)}')
print(f'dss.loads_read_r_neut(): {dss.loads_read_r_neut()}')
print(f'dss.loads_read_vmax_pu(): {dss.loads_read_vmax_pu()}')
print(f'dss.loads_write_vmax_pu(): {dss.loads_write_vmax_pu(123.1)}')
print(f'dss.loads_read_vmax_pu(): {dss.loads_read_vmax_pu()}')
print(f'dss.loads_read_vmin_emerg(): {dss.loads_read_vmin_emerg()}')
print(f'dss.loads_write_vmin_emerg(): {dss.loads_write_vmin_emerg(123.1)}')
print(f'dss.loads_read_vmin_emerg(): {dss.loads_read_vmin_emerg()}')
print(f'dss.loads_read_vmin_norm(): {dss.loads_read_vmin_norm()}')
print(f'dss.loads_write_vmin_norm(): {dss.loads_write_vmin_norm(123.1)}')
print(f'dss.loads_read_vmin_norm(): {dss.loads_read_vmin_norm()}')
print(f'dss.loads_read_vmin_pu(): {dss.loads_read_vmin_pu()}')
print(f'dss.loads_write_vmin_pu(): {dss.loads_write_vmin_pu(123.1)}')
print(f'dss.loads_read_vmin_pu(): {dss.loads_read_vmin_pu()}')
print(f'dss.loads_read_xfkva(): {dss.loads_read_xfkva()}')
print(f'dss.loads_write_xfkva(): {dss.loads_write_xfkva(123.1)}')
print(f'dss.loads_read_xfkva(): {dss.loads_read_xfkva()}')
print(f'dss.loads_read_x_neut(): {dss.loads_read_x_neut()}')
print(f'dss.loads_write_x_neut(): {dss.loads_write_x_neut(123.1)}')
print(f'dss.loads_read_x_neut(): {dss.loads_read_x_neut()}')
print(f'dss.loads_read_pct_series_rl(): {dss.loads_read_pct_series_rl()}')
print(f'dss.loads_write_pct_series_rl(): {dss.loads_write_pct_series_rl(123.1)}')
print(f'dss.loads_read_pct_series_rl(): {dss.loads_read_pct_series_rl()}')
print(f'dss.loads_read_rel_weight(): {dss.loads_read_rel_weight()}')
print(f'dss.loads_write_rel_weight(): {dss.loads_write_rel_weight(123.1)}')
print(f'dss.loads_read_rel_weight(): {dss.loads_read_rel_weight()}')


# Variant methods
print(45 * '=' + ' Variant Methods' + 45 * '=')
print(f'dss.loads_all_names(): {dss.loads_all_names()}')
print(f'dss.loads_read_zipv(): {dss.loads_read_zipv()}')
print(f'dss.loads_write_zipv(): {dss.loads_write_zipv("[1 2 3 4 5 6 7]")}')
print(f'dss.loads_read_zipv(): {dss.loads_read_zipv()}')
