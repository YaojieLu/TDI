
import pandas as pd

# read files
df_16 = pd.read_table('PartD_Prescriber_PUF_NPI_16.txt')
df_17 = pd.read_table('PartD_Prescriber_PUF_NPI_17.txt')

# average number of beneficiaries per provider in 2017
print(df_17['bene_count'].mean())

# the median, in days, of the distribution of this value across all providers in 2017
print((df_17['total_day_supply']/df_17['total_claim_count']).median())

# the standard deviation of the fraction of drug claims that are for brand-name drugs in 2017
df_17_2 = df_17[['specialty_description', 'total_claim_count', 'brand_claim_count']].dropna()
df_17_3 = df_17_2.groupby(['specialty_description'])[['total_claim_count', 'brand_claim_count']].sum()
df_17_3['fraction'] = df_17_3['brand_claim_count']/df_17_3['total_claim_count']
print(df_17_3['fraction'][df_17_3['total_claim_count']>=1000].std())

# the difference between the largest and smallest ratios
df_17_2 = df_17.groupby(['nppes_provider_state'])[['opioid_bene_count', 'antibiotic_bene_count']].sum()
df_17_2['ratio'] = df_17_2['opioid_bene_count']/df_17_2['antibiotic_bene_count']
print(df_17_2['ratio'].max()-df_17_2['ratio'].min())

# Pearson correlation coefficient
df_17_2 = df_17[['total_claim_count', 'total_claim_count_ge65', 'lis_claim_count']].dropna()
df_17_2['fraction_65'] = df_17_2['total_claim_count_ge65']/df_17_2['total_claim_count']
df_17_2['fraction_lis'] = df_17_2['lis_claim_count']/df_17_2['total_claim_count']
print(df_17_2['fraction_65'].corr(df_17_2['fraction_lis']))

# largest ratio
df_17['ave_len_opioid_pres'] = df_17['opioid_day_supply']/df_17['opioid_claim_count']
df_17_2 = df_17.groupby(['nppes_provider_state', 'specialty_description']).agg({'ave_len_opioid_pres':['count', 'mean']}).reset_index()
df_17_2.columns = ['state', 'specialty', 'count', 'ave_len']
df_17_2 = df_17_2[df_17_2['count']>=100]
df_17_3 = df_17.groupby(['specialty_description'])['ave_len_opioid_pres'].mean()
df_17_2['ratio'] = df_17_2.apply(lambda row: row['ave_len']/df_17_3.loc[row['specialty']], axis=1)
print(df_17_2['ratio'].max())

# average inflation rate
df_16_2 = df_16[['npi', 'total_drug_cost', 'total_day_supply']].dropna()
df_16_2['ave_cost_16'] = df_16['total_drug_cost']/df_16['total_day_supply']
df_17_2 = df_17[['npi', 'total_drug_cost', 'total_day_supply']].dropna()
df_17_2['ave_cost_17'] = df_17['total_drug_cost']/df_17['total_day_supply']
df = pd.merge(df_16_2[['npi', 'ave_cost_16']], df_17_2[['npi', 'ave_cost_17']], on='npi')
df['inflation'] = (df['ave_cost_17']-df['ave_cost_16'])/df['ave_cost_16']*100
print(df['inflation'].mean())

# the largest such fraction, when considering specialties with at least 1000 proviers in 2016
df_16_2, df_17_2 = df_16.copy(), df_17.copy()
df_16_2.rename(columns={'specialty_description':'16'}, inplace=True)
df_17_2.rename(columns={'specialty_description':'17'}, inplace=True)
df = pd.merge(df_16_2[['npi', '16']], df_17_2[['npi', '17']], on='npi')
df['change'] = df['16']!=df['17']
df2 = df.groupby(['16']).agg({'change':['count', 'mean']}).reset_index()
df2.columns = ['16', 'count', 'fraction']
df2 = df2[df2['count']>=1000]
#df3 = df[['16', '17']][df['16'].isin(df2[df2['fraction']==1]['16'].tolist())].drop_duplicates()
print(df2['fraction'][df2['fraction']<1].max())