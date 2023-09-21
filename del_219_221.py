import pickle

with open('list/win_score.pickle', 'rb') as f:
    lst_win_score = pickle.load(f)
with open('list/lose_score.pickle', 'rb') as f:
    lst_lose_score = pickle.load(f)

del lst_win_score[219:222]
del lst_lose_score[219:222]

with open('list/win_score.pickle', 'wb') as f:
    pickle.dump(lst_win_score, f)
with open('list/lose_score.pickle', 'wb') as f:
    pickle.dump(lst_lose_score, f)
