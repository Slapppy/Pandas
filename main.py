import pandas as pd

data = pd.read_excel('test.xlsx', skipfooter=1)
df_reestr = data
df_reestr.columns = ['object_name', 'section', 'rev', 'pole_num', 'quantity', 'elevation', 'pole_code', 'corner',
                     'pole_pile',
                     'prop_pile', 'pole_pile_over', 'pole_pile_under', 'pole_pile_sum', 'prop_pile_over',
                     'prop_pile_under', 'prop_pile_sum', 'setting', 'v_cps', 'v_cpr', 'tsg', 'temp',
                     'depth_paint_pole', 'depth_paint_prop', 'gtm_rev', 'temp_mitter', 'tss', 'temp_2',
                     'term_stab_rev', 'term_stab', 'pole_pile_mass', 'prop_pile_mass']
section_num = 5
df_order_pile = df_reestr[(df_reestr['section'] == section_num)]
pole_pile_list = df_reestr['pole_pile'].unique()
prop_pile_list = df_reestr['prop_pile'].unique()
pile_list = []
for i in pole_pile_list:
    if i in pile_list:
        continue
    else:
        pile_list.append(i)
for x in prop_pile_list:
    if x in pile_list:
        continue
    else:
        pile_list.append(x)


def calc_pile(pile, pile_under):
    if pile > 4:
        result = pile_under + 0.5
        return result
    else:
        result = pile + pile_under
        return result


pile_list = [y for y in pile_list if y == y]
for pile in pile_list:
    pole_pile_diam = df_reestr[(df_reestr['pole_pile'] == pile) & (df_reestr['section'] == section_num)]
    if len(pole_pile_diam) > 0:
        pole_pile_diam['result'] = pole_pile_diam.apply(
            lambda row: calc_pile(row['pole_pile_over'], row['pole_pile_under']), axis=1)
        print(pole_pile_diam)
