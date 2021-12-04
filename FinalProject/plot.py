import matplotlib.pyplot as plt
from convert_efficiency_to_json import dict_of_data_for_plot

title_list = ['Рік', 'Курс на 1.10',
              'Курс на 1.11',
              'Курс на 1.12',
              'Курс на 1.12 рівень',
              'Рівень за три місяці']

dict_of_values_for_plots = {}

for key, val in dict_of_data_for_plot.items():
    for val_key, val_value in val.items():
        try:
            dict_of_values_for_plots[val_key].append(val_value)
        except:
            dict_of_values_for_plots[val_key] = [val_value]

styles = ['b--', 'k', 'r--','b--', 'k', 'r--']
line_width = ['1', '5', '2','1', '5', '2']
for final_key, final_val in dict_of_values_for_plots.items():
    if final_key != 'period':

        for id, val in enumerate(dict_of_values_for_plots[final_key]):
            plt.plot(val, styles[id], linewidth=line_width[id], alpha=0.7)

        plt.title(title_list[0])
        title_list.pop(0)
        plt.legend(['1 англійський фунт стерлінг', '10 бельгійських франків','1 німецька марка','1 голандський гульден','1 канадський долар','1 долар США'])
        plt.savefig(final_key, dpi=200)
        plt.clf()