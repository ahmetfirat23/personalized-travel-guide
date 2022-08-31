import warnings

import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


def trim_data(data):
    sums = data.sum().sort_values(ascending=False)
    cumsum = 0
    index = 0
    total_sum = data.sum().sum()
    for count in sums:
        cumsum += count
        if cumsum / total_sum >= 0.85:
            break
        index += 1
    return data[sums[:index].index].copy(), list(sums[:index].index)


def check_clusters(data):
    """Graph inertia for different n_cluster values"""
    pass_num = data.shape[0]
    inertias = []
    for i in range(1, pass_num//10, pass_num // 100):
        scaler = StandardScaler()
        model = KMeans(n_clusters=i, random_state=42)
        pipeline = make_pipeline(scaler, model)
        pipeline.fit(data)
        inertias.append(pipeline["kmeans"].inertia_)

    plt.plot(list(range(1, pass_num//10, pass_num // 100)), inertias, marker='x')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()


def train_model(data):
    """Train KMeans model
    Add labels to data"""
    warnings.simplefilter(action='ignore', category=FutureWarning)
    warnings.simplefilter(action='ignore', category=UserWarning)
    scaler = StandardScaler()
    model = KMeans(n_clusters=240, random_state=42)
    pipeline = make_pipeline(scaler, model)
    pipeline.fit(data)
    labels = model.predict(data)
    data['labels'] = labels
    return data, pipeline


def graph_model(data, labels):
    model_tsne = TSNE(learning_rate=120, random_state=42)
    transformed = model_tsne.fit_transform(data)
    xs = transformed[:, 0]
    ys = transformed[:, 1]
    plt.scatter(xs, ys, c=labels, alpha=0.7)
    plt.show()


def get_cities(data, model, passenger, city_num):
    """Return most popular cities in passenger's cluster that passenger did not visit"""
    passenger['labels'] = model.predict(passenger)
    cluster_no = passenger['labels'][0]
    data = data[data['labels'] == cluster_no]
    counts = data.drop('labels', axis=1).sum(axis=0)
    cities = counts.sort_values(ascending=False).index[0:city_num * 5].values.tolist()
    rec_cities = cities[:]

    for city in cities:
        if len(rec_cities) <= city_num:
            break
        if passenger.iloc[0][city] != 0:
            rec_cities.remove(city)
    return rec_cities[:city_num]
