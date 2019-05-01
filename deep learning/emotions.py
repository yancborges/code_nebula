import tflearn
from tflearn.data_utils import to_categorical, pad_sequences
from tflearn.datasets import imdb

number_of_words = 10000

train, test = imdb.load_data(path='imdb.pkl', n_words=number_of_words, valid_portion=0.1)

X_train, y_train = train
X_test, y_test = test

X_train = pad_sequences(X_train, maxlen=100, value=0.)
X_test = pad_sequences(X_test, maxlen=100, value=0.)

y_train = to_categorical(y_train, nb_classes=2)
y_test = to_categorical(y_test, nb_classes=2)

net = tflearn.input_data([None,100])
net = tflearn.embedding(net, input_dim=number_of_words, output_dim=128)
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, 2, activation='softmax')

net = tflearn.regression(net, optimizer='adam', learning_rate=0.0001, loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(X_train, y_train, validation_set(X_test, y_test), show_metric=True, batch_size=32)

