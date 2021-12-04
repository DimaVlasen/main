import operator
from dataclasses import dataclass
import json
import codecs


@dataclass
class Enterprise:
    code: int
    name: str


@dataclass
class EnterpriseActivity:
    code: int
    period: str
    commodity_circulation: float
    balance_income: float
    average_cost_main_components: float

    def __eq__(self, other):
        return self.code == other.rank and self.commodity_circulation == other.commodity_circulation

    def __lt__(self, other):
        return self.code < other.code


def print_enterprise_activity(enterprise_activity):
    '''print_enterprise_activity function prints
    "Курс гривні до валют іноземних країн"
    with names and values'''

    print("Код {code}, Період на 1.10 {period}, Період на 1.11 {commodity_circulation}, Період на 1.12,"
          " {balance_income} Рік {average_cost_main_components} "
          .format(code=enterprise_activity.code, period=enterprise_activity.period,
                  commodity_circulation=enterprise_activity.commodity_circulation,
                  balance_income=enterprise_activity.balance_income,
                  average_cost_main_components=enterprise_activity.average_cost_main_components))


# Json was made by TABULA https://tabula.technology
with codecs.open(r"C:\ICS-6_VlasDimawork\main\FinalProject\tabula-zad.json", encoding='utf-8',errors='ignore')as f:
    distros_dict = json.load(f)

data_array = []

# parse json to array of EnterpriseActivity
for distro in distros_dict:
    data_list = distro['data']

    for data in data_list:
        data_array.append(EnterpriseActivity(int(data[0]["text"]), str(data[1]["text"]),
                                             float(str(data[2]["text"]).replace(',', '.')),
                                             float(str(data[3]["text"]).replace(',', '.')),
                                             float(str(data[4]["text"]).replace(',', '.'))))

enterprises_array = [Enterprise(1, "1 англійський фунт стерлінг"), 
                     Enterprise(2, "10 бельгійських франків"),
                     Enterprise(3, "1 німецька марка"),
                     Enterprise(4, "1 голандський гульден"),
                     Enterprise(5, "1 канадський долар"),
                     Enterprise(6, "1 долар США")]
                     

class EfficiencyOfEnterprise:

    def __init__(self, name, period, commodity_circulation, balance_profit, average_annual_cost_of_fixed_assets):
        self.name = name  # Найменування валюти
        self.period = period  # Код валюти
        self.commodity_circulation = commodity_circulation  # Рік
        self.balance_profit = balance_profit  # Курс на 1.10

        # Курс на 1.11
        self.average_annual_cost_of_fixed_assets = average_annual_cost_of_fixed_assets

        # Курс на 1.12 
        self.return_of_assets = calculate_return_of_assets(commodity_circulation,
                                                           average_annual_cost_of_fixed_assets)

        # Курс на 1.12 рівень
        self.capital_intensity = calculate_capital_intensity(self.return_of_assets)

        # Рівень за три місяці
        self.profitability = calculate_profitability(balance_profit,
                                                     average_annual_cost_of_fixed_assets)


def calculate_return_of_assets(commodity_circulation, average_annual_cost_of_fixed_assets):
    return round(commodity_circulation / average_annual_cost_of_fixed_assets, 2)


def calculate_capital_intensity(return_of_assets):
    return round(1 / return_of_assets, 2)


def calculate_profitability(balance_profit, average_annual_cost_of_fixed_assets):
    return round(balance_profit / average_annual_cost_of_fixed_assets, 2)


efficiencyOfEnterprise = []

for data in data_array:
    efficiencyOfEnterprise.append(EfficiencyOfEnterprise(name=enterprises_array[data.code - 1].name, period=data.period,
                                                         commodity_circulation=data.commodity_circulation,
                                                         balance_profit=data.balance_income,
                                                         average_annual_cost_of_fixed_assets=
                                                         data.average_cost_main_components))

sorted_enterprise_efficiency_list = sorted(efficiencyOfEnterprise, key=operator.attrgetter("name"))