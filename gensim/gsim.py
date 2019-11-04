import gensim.downloader as api

model = api.load("glove-wiki-gigaword-100")

result = model.most_similar(positive=['education', 'learned', 'studied'], negative=['cat'])

print("{}: {:.4f}".format(*result[0]))