import pickle
d = dict(name='bobo',age=20,score=88)
data = pickle.dumps(d)
print(data)

a = pickle.loads(data)
print(a)