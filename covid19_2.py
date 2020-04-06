
import pandas as pd
import matplotlib.pyplot as plt

# read file
df_lex = pd.read_csv('data/state_lex_2020-03-27.csv', index_col=0)
df_lex_ny = df_lex.loc[['NY']].transpose().reset_index()
df_lex_ny.columns = ['abbr', 'travel_history_ny']
df_case = pd.read_csv('data/time_series_covid19_confirmed_US.csv')
df_case = df_case.groupby('Province_State')[['4/5/20']].sum().reset_index()
df_case.columns = ['State', 'case']
df_pop = pd.read_csv('data/us_population.csv')
df_pop = df_pop[['State', 'Pop']]
df_case = pd.merge(df_case, df_pop, on='State')
df_abbr = pd.read_csv('data/US_state_abbr.csv')
df_case = pd.merge(df_case, df_abbr, on='State')
df = pd.merge(df_case, df_lex_ny, on='abbr')
df['traveled_pop'] = df['Pop']*df['travel_history_ny']
df = df[['Pop', 'traveled_pop', 'case', 'State', 'abbr']]
