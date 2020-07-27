import numpy as np
from scipy.io import loadmat
from scipy.signal import butter,filtfilt
from scipy.fftpack import fft, ifft
from plotly.subplots import make_subplots
from sklearn.model_selection import train_test_split


def process_data_split(filename, split = True, train_size=0.75, random_state=7, time=False):
    S1 = loadmat(filename)
    x = S1['training_data'][0][0]
    x = np.append(x, S1['training_data'][0][1], axis=0)
    x = np.append(x, S1['training_data'][0][2], axis=0)
    x = np.append(x, S1['training_data'][0][3], axis=0)
#     tim = S1['Info'][0][0][5][0]
    print("x shape - ",end="")
    print(x.shape == (160, 400, 10))
    y = np.zeros((160,4))
    y[0:40,0] = 1
    y[40:80,1] = 1
    y[80:120,2] = 1
    y[120:,3] = 1
    print("y sum - ", end="")
    print(all(np.sum(y, axis=0) == (np.array([40,40,40,40]))))
    if split == True:
        return train_test_split(x, y, train_size=train_size, random_state=random_state)
    else:
        if time:
            return x, y, tim
        else:
            return x, y

def butter_lowpass_filter(data, cutoff, fs, order, btype='low'):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype, analog=False)
    y = filtfilt(b, a, data)
    return y

def plot_eeg_split(data, fs = 400, order = 3, plotshow = True, ret = False):

    
    cutoffd = np.array([0.5,4])
    delta = butter_lowpass_filter(data, cutoffd, fs, order,'bandpass')
    
    cutofft = np.array([4,7.5])
    theta = butter_lowpass_filter(data, cutofft, fs, order,'bandpass')
    
    cutoffa = np.array([7.5,12])
    alpha = butter_lowpass_filter(data, cutoffa, fs, order,'bandpass')
    
    cutoffb = np.array([12,30])
    beta = butter_lowpass_filter(data, cutoffb, fs, order,'bandpass')
    
    cutoffg = np.array([30,75])
    gamma = butter_lowpass_filter(data, cutoffg, fs, order,'bandpass')
    
    

    if plotshow:
        fig = go.Figure()
        fig = make_subplots(rows=6, cols=1,shared_xaxes=True, vertical_spacing=0.05,
                        subplot_titles=("Full Signal","Delta","Theta", "Alpha","Beta","Gamma"))

        fig.append_trace(go.Scatter(
            x = tim,        
            y = data,
                    line =  dict(shape =  'spline' ),
                    name = 'OG signal'
                    ),row=1,col=1)

        fig.append_trace(go.Scatter(
                    x = tim,   y = delta,
                    line =  dict(shape =  'spline' ),
                    name = 'fsignal; cutoff =  '+ str(cutoffd)
                    ),row=2,col=1)

        fig.append_trace(go.Scatter(
                    x = tim,   y = theta,
                    line =  dict(shape =  'spline' ),
                    name = 'fsignal; cutoff =  '+ str(cutofft)
                    ),row=3,col=1)

        fig.append_trace(go.Scatter(
                    x = tim,   y = alpha,
                    line =  dict(shape =  'spline' ),
                    name = 'fsignal; cutoff =  '+ str(cutoffa)
                    ),row=4,col=1)

        fig.append_trace(go.Scatter(
                    x = tim,   y = beta,
                    line =  dict(shape =  'spline' ),
                    name = 'fsignal; cutoff =  '+ str(cutoffb)
                    ),row=5,col=1)

        fig.append_trace(go.Scatter(
                    x = tim,   y = gamma,
                    line =  dict(shape =  'spline' ),
                    name = 'fsignal; cutoff =  '+ str(cutoffg)
                    ),row=6,col=1)

        fig.update_layout(
            autosize=False,
            width=980,
            height=800,
        )
        fig.show()
    
    if ret:
        return np.array([alpha, beta, gamma, delta, theta]).transpose()

def bandwise_split(filename, split = True, train_size=0.75, random_state=7):
    x,y = process_data_split(filename, split = False)
    I = x.shape[0]
    J = x.shape[2]
    Y = []
    X_filt = []
    for i in range(I):
        for j in range(J):
            X_filt.append(plot_eeg_split(x[i,:,j], ret=True, plotshow=False))
            Y.append(y[i])
    X_filt = np.array(X_filt)
    Y_filt = np.array(Y)
    if split == True:
        return train_test_split(X_filt, Y_filt, train_size=train_size, random_state=random_state)
    else:
        return X_filt, Y_filt