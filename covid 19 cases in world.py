from covid import Covid
#for using this script firstly run (pip install covid) in your shell/console
covid=Covid()

def covid_worldwide():
    print("total_active_cases :",covid.get_total_active_cases())
    print("total_confirmed_cases :",covid.get_total_confirmed_cases())
    print("total_recovered_cases :",covid.get_total_recovered())
    print("total_deaths :",covid.get_total_deaths())

covid_worldwide()
