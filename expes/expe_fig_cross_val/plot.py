import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sparse_ho.utils_plot import configure_plt

configure_plt()

# save_fig = False
save_fig = True
fig_dir = "../../../CD_SUGAR/tex/ICML2020slides/prebuiltimages/"


current_palette = sns.color_palette("colorblind")

p_alphas = np.load("p_alphas.npy")
objs = np.load("objs.npy")

p_alphas_grad = np.load("p_alphas_grad.npy")
objs_grad = np.load("objs_grad.npy")

# ax = plt.gca()
# ax.tick_params(width=10)

fig = plt.figure()
plt.semilogx(
    p_alphas, objs, color=current_palette[0], linewidth=7.0)
plt.semilogx(
    p_alphas, objs, 'bo', label='0-order method (grid-search)',
    color=current_palette[1])
# plt.semilogx(
#     p_alphas_grad, objs_grad, 'bX', label='1rst order method',
#     color=current_palette[2])
plt.xlabel(r"$\lambda / \lambda_{\max}$", fontsize=28)
plt.ylabel("validation loss", fontsize=28)
plt.tick_params(width=5)
plt.legend(fontsize=28)
plt.tight_layout()

if save_fig:
    fig.savefig(
        fig_dir + "cross_val_real_sim.pdf", bbox_inches="tight")
fig.show()

plt.show(block=False)


# plot fig with 0 order and 1rst order methods

fig = plt.figure()
plt.semilogx(
    p_alphas, objs, color=current_palette[0], linewidth=7.0)
plt.semilogx(
    p_alphas, objs, 'bo', label='0-order method (grid-search)',
    color=current_palette[1])
plt.semilogx(
    p_alphas_grad, objs_grad, 'bX', label='1-rst order method',
    color=current_palette[2])
plt.xlabel(r"$\lambda / \lambda_{\max}$", fontsize=28)
plt.ylabel("validation loss", fontsize=28)
plt.tick_params(width=5)
plt.legend(fontsize=28)
plt.tight_layout()

if save_fig:
    fig.savefig(
        fig_dir + "cross_val_and_grad_search_real_sim.pdf", bbox_inches="tight")
fig.show()

plt.show(block=False)