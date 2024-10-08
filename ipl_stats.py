import numpy as np
import pandas as pd

# df = pd.read_csv('/Users/kunalkoshta/Desktop/Campux_X_DS/datas/Fifa Worldcup 2022 - Sheet1.csv')
# teams = df[['Team','On Target']].value_counts()

ipl = pd.read_csv('/Users/kunalkoshta/Desktop/Campux_X_DS/datas/IPL_Matches_2008_2022.csv')
ipl['Team1'] = ipl['Team1'].str.replace('Delhi Daredevils','Delhi Capitals')
ipl['Team1'] = ipl['Team1'].str.replace('Kings XI Punjab','Punjab Kings')
ipl['Team1'] = ipl['Team1'].str.replace('Rising Pune Supergiants','Rising Pune Supergiant')
ipl['Team2'] = ipl['Team2'].str.replace('Delhi Daredevils','Delhi Capitals')
ipl['Team2'] = ipl['Team2'].str.replace('Kings XI Punjab','Punjab Kings')
ipl['Team2'] = ipl['Team2'].str.replace('Rising Pune Supergiants','Rising Pune Supergiant')

# no_result = ipl['City'][ipl['WinningTeam'].isna()]

def point_table(season):
    year = ipl[ipl['Season']==season]
    teams = pd.DataFrame((year['Team1'].value_counts()+year['Team2'].value_counts()))
    teams.reset_index(inplace=True)
    teams.rename(columns={'index':'TeamName','count':'MatchesPlayed'},inplace=True)
    teams.set_index('TeamName',inplace=True)
    teams.sort_values(by='MatchesPlayed',inplace=True)
    match_win = dict.fromkeys(teams.index,0)
    points = dict.fromkeys(teams.index,0)
    no_result = dict.fromkeys(teams.index,0)
    for i,j,k in zip(year['Team1'],year['Team2'],year['WinningTeam']):
        if i==k:
            match_win[i]+=1
            points[i]+=2
        elif j==k:
            match_win[j]+=1
            points[j]+=2
        elif year['WinningTeam'].isna():
            # print(year['WinningTeam'])
            match_win[i]+=0
            points[i]+=1
            match_win[j]+=0
            points[j]+=1
        
    teams['MatchesWon']=match_win.values()
    teams['NoResult']=no_result.values()
    teams['Points']=points.values()
    teams.sort_values(['Points','TeamName'],ascending=[False,True],inplace=True)
    # print(teams.head(2))
    teams['Seasonposition']=[str(i) for i in range(1,11)]
    winner = year['WinningTeam'][year['MatchNumber']=='Final'].values[0]
    runner  = year['WinningTeam'][year['MatchNumber']=='Qualifier 2'].values[0]
    teams.at[winner,'Seasonposition']='Winner'
    teams.at[runner,'Seasonposition']='Runner'
    # print(year['WinningTeam'][year['MatchNumber']=='Final'].values)
    print(teams)
    
point_table('2022')


