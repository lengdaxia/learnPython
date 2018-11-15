# encoding:utf-8

import pandas as pd
import math
import csv
import random
import numpy as numpy
from sklearn import liear_model
from sklearn.model_selection import cross_val_score


# base vals
base_elo = 1600
team_elos = {}
team_stats = {}
X = []
y = []
folder = 'data'


def init_data(Mstat,Ostat,Tstat):
    new_m = Mstat.drop(['Rk','Arena'],axis=1)
    new_o = Ostat.drop(['Rk','G','MP'],axix=1)
    new_t = Tstat.drop(['Rk','G','MP'],axix=1)

    team_stats1 = pd.merge(new_m,new_t,how='left',on='Team')
    team_stats2 = pd.merge(team_stats1,new_t,how='left',on='Team')
    return team_stats1.set_index('Team',inplace=False,drop=True)

def get_elo(team):
    try:
        return team_elos[team]
    except:
        team_elos[team] = base_elo
        return team_elos[team]

def cal_elo(win_team,lose_team):
    winner_rank = get_elo(win_team)
    loser_rank = get_elo(lose_team)


    rand_diff = winner_rank - loser_rank
    exp = (rand_diff * -1)/400
    odds = 1/(1+math.pow(10,exp))

    if winner_rank < 2100:
        k = 32
    elif: winner_rank >= 2100 and winner_rank < 2400:
        k = 24
    else:
        k = 16

    new_winner_rank = round(winner_rank + (k *(1-odds)))
    new_loser_rank = round(loser_rank + ( k * (1-odds)))

    return new_winner_rank,new_loser_rank


def build_dataset(all_data):
    print('build_dataset..')
    X = []
    skip = 0
    for index,row in all_data.iterrows():
        Wteam = row['WTeam']
        Lteam = row['LTeam']

        team1_elo = get_elo(Wteam)
        team2_elo = get_elo(Lteam)

        # 
        if row['WLoc'] == 'H':
            team1_elo += 100
        else:
            team2_elo += 100

        team1_features = [team1_elo]
        team2_features = [team2_elo]

        for key,value in team_stats.loc[Wteam].items():
            team2_features.append(value)
        for key, value in team_stats.loc[Lteam].iteritems():
            team2_features.append(value)

        # 将两支队伍的特征值随机的分配在每场比赛数据的左右两侧
        # 并将对应的0/1赋给y值
        if random.random() > 0.5:
            X.append(team1_features + team2_features)
            y.append(0)
        else:
            X.append(team2_features + team1_features)
            y.append(1)

        if skip == 0:
            print('X',X)
            skip = 1

        # 根据这场比赛的数据更新队伍的elo值
        new_winner_rank, new_loser_rank = calc_elo(Wteam, Lteam)
        team_elos[Wteam] = new_winner_rank
        team_elos[Lteam] = new_loser_rank

    return np.nan_to_num(X), y

if __name__ == '__main__':
    Mstat = pd.read_csv(folder + '/15-16Miscellabeous_Stat.csv')
    Ostst = pd.read_csv(folder+'/15-160pponent_Per_Game_Stat_csv')
    Tstat = pd.read_csv(folder + '/15-16Team_Per_Game_Stat.csv')

    team_stats = init_data(Mstat,Ostst,Tstat)

    result_data = pd.read_csv(folder + '/2015-1016_result.csv')
    X,y = build_dataset(result_data)

    # 训练网络模型
    print('Fitting on %d game samples..' % len(X))

    model = linear_model.LogisticRegression()
    model.fit(X,y)

    # 利用10折交叉验证计算训练正确率
    print('Doing cross_validation')
    print(cross_val_score(model,X,y,cv=10,scoring='accuracy',n_jobs=-1).mean())








