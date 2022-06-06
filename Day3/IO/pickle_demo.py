import pickle

d = dict(name='Bob', age=20, score=88)

with open('dump.txt', 'wb') as f:
    data = pickle.dumps(d)
    pickle.dump(d, f)

print(data)

with open('dump.txt', 'rb') as f:
    reborn = pickle.load(f)
print(reborn)
