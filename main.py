from pgmpy.estimators import ConstraintBasedEstimator

data = pd.DataFrame(np.random.randint(0, 3, size=(2500, 8)), columns=list('ABCDEFGH'))
data['A'] += data['B'] + data['C']
data['H'] = data['G'] - data['A']
data['E'] *= data['F']

est = ConstraintBasedEstimator(data)

print(est.test_conditional_independence('B', 'H'))          # dependent
print(est.test_conditional_independence('B', 'E'))          # independent
print(est.test_conditional_independence('B', 'H', ['A']))   # independent
print(est.test_conditional_independence('A', 'G'))          # independent
print(est.test_conditional_independence('A', 'G',  ['H']))  # dependent