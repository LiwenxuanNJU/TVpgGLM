# experimental results of tv_model from selected two neurons
import sys
sys.path.append("/Users/roger/Dropbox/TVpgGLM-v1/TVpgGLM/libs")

import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from hips.plotting.colormaps import harvard_colors

sns.set_style("white")
paper_rc = {'lines.linewidth': 1, 'lines.markersize': 10,
            'font.size': 15, 'axes.labelsize':15, 'axes.titlesize':15,
            'xtick.labelsize': 15, 'ytick.labelsize': 15}
sns.set_context("paper", rc = paper_rc)
plt.ion()

color = harvard_colors()[0:10]

with open('/Users/roger/Dropbox/TVpgGLM-v1/TVpgGLM/results/exp_tv_N2.pickle', 'rb') as f:
     lps1, lps2, lps3, lps4, lps5,\
     W_mean1, W_mean2, W_mean3, W_mean4, W_mean5, W_std1, W_std2, W_std3, W_std4, W_std5, W_smpls, \
     Y_1st, Y_2nd, Y_3rd, Y_123,\
     fr_mean1, fr_mean2, fr_mean3, fr_mean4, fr_mean5, fr_std1, fr_std2, fr_std3, fr_std4, fr_std5 = pickle.load(f)

########################
##static model weights##
########################
fig, ax = plt.subplots(1,3)
sns.heatmap(W_mean1[:,:,0], ax=ax[0], annot=True, vmin=-1, vmax=1)
sns.heatmap(W_mean2[:,:,0], ax=ax[1], annot=True, vmin=-1, vmax=1)
sns.heatmap(W_mean3[:,:,0], ax=ax[2], annot=True, vmin=-1, vmax=1)
ax[0].set_yticks([])
ax[0].set_xticks([])
ax[1].set_yticks([])
ax[1].set_xticks([])
ax[2].set_yticks([])
ax[2].set_xticks([])
ax[0].set_xlabel('Post')
ax[0].set_ylabel('Pre')
ax[0].set_title('Before Learning')
ax[1].set_xlabel('Post')
ax[1].set_ylabel('Pre')
ax[1].set_title('During Learning')
ax[2].set_xlabel('Post')
ax[2].set_ylabel('Pre')
ax[2].set_title('after Learning')
plt.tight_layout()

plt.savefig("/Users/roger/Dropbox/TVpgGLM-v1/TVpgGLM/fig/exp_static_N2_weights.pdf")
####################
##tv_model weights##
####################
N_smpls = 10
fig, ax = plt.subplots(2,2)
for i in range(2):
    for j in range(2):
        sns.tsplot(data=W_smpls[N_smpls // 2:, i, :, j, 0], ax=ax[i, j], color=color[1])
        if i == 1:
            ax[i,j].set_xlabel('Time', fontweight="bold")
        if j == 0:
            ax[i,j].set_ylabel('Weights', fontweight="bold")

plt.tight_layout()
plt.savefig("/Users/roger/Dropbox/TVpgGLM-v1/TVpgGLM/fig/exp_tv_N2_weights.pdf")
#################################
##plot likelihood via iteration##
#################################
plt.plot(lps5)
plt.plot(lps4+170)
plt.title('log likelihood of fitted model')
fig, ax = plt.subplots(1,2)
ax[0].plot(lps5)
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Log Likelihood")
ax[0].set_title('Static')
ax[0].set_ylim(-5550, -5300)
ax[1].plot(lps4+100)
ax[1].set_xlabel("Iteration")
ax[1].set_ylabel("Log Likelihood")
ax[1].set_title('TV')
ax[1].set_ylim(-5550, -5300)
plt.savefig("/Users/roger/Dropbox/TVpgGLM-v1/TVpgGLM/fig/exp_N2_likhd.pdf")