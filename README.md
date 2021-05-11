# Fractale

## Qu'est-ce-qu'une fractale ?

Le mot fractale vient du latin fractus qui signifie brisé, irregulié. Les fractales permettent de décrire les phénomènes naturels qui présentent une certaine irrégularité, d'où l'appellation de << géométrie de la nature et du chaos >>.

- Site sur les nombres complexe et les Fractales" https://complexe.jimdofree.com/les-fractales/d%C3%A9finition/

Dimension non euclidienne => non entière. Périmètre infinie pour une aire finie. Objet dont les propriétés sont invariants par changement d échelle.

=> Principe d autosimilarité. On trouve des similarités en l observant à différents échelles.

Géométrie fractale versus géométrie euclidienne pour devenir des éléments complexe de la nature.

"ART-FRACTAL" https://art-fractal.pagesperso-orange.fr/page24c.html

## Système dynamique
Système dynamique : système qui décrit dans l espace un état qui évolue dans le temps.

Exposant de lyapunov mesure le degré de sensibilité d un système dynamique.

"Qu'est-ce Fractale de Liapounov. Encyclopédie" https://amp.fr.what-this.com/299871/1/fractale-de-liapounov.html

"Lyapunov exponent - Wikipedia" https://en.m.wikipedia.org/wiki/Lyapunov_exponent

## Lyapunov

### Algo

The best : "Les fractales de Lyapunov - Choux romanesco, Vache qui rit et intégrales curvilignes" http://eljjdx.canalblog.com/archives/2008/09/14/10571223.html

https://www.wolframcloud.com/objects/demonstrations/LyapunovFractals-source.nb

http://www.les-mathematiques.net/phorum/read.php?4,749281,749294 -> @Juliens tu peux montrer que le linéarisé du système est asymptotiquement stable au point d'équilibre (−1,0) . Tu peux donc calculer une fonction de Lyapunov V pour le linéarisé. Tu peux en plus montrer que la dérivée de cette fonction de Lyapunov (le long des solution du système) reste négative localement autour du point d'équilibre pour le système complet.

@Mishka l'intérêt des fonctions de Lyapunov c'est de pouvoir montrer la stabilité d'un système dynamique sans avoir à connaitre les solutions. C'est très puissant mais ce n'est pas facile de trouver une fonction de Lyapunov en général.

"Stabilité de Liapounov — Wikipédia" https://fr.m.wikipedia.org/wiki/Stabilit%C3%A9_de_Liapounov

"Fractale de Liapounov — Wikipédia" https://fr.m.wikipedia.org/wiki/Fractale_de_Liapounov

https://hypertextbook.com/chaos/lyapunov-1/

https://fr.wikipedia.org/wiki/Exposant_de_Liapounov

eps_n = f(u_n-1 + eps_n-1) - f(u_n-1)

Cette amplification varie généralement d'un pas au suivant, ce qui conduit à calculer le produit des rapports d'erreurs consécutives :

eps_n / eps0 = Product(eps_i/eps_i-1) = ...

En écrivant epsilon _{n}=e^{\lambda n}\epsilon _{0}}\epsilon_n = e^{\lambda n} \epsilon_0 et en passant à la limite on obtient l'exposant de Liapounov qui représente le logarithme moyen de l'accroissement 

https://arxiv.org/ftp/arxiv/papers/1401/1401.3315.pdf

Usually, the Lyapunov exponent or Lyapunov characteristic exponent of a
dynamical system is a quantity that characterizes the rate of separation of
infinitesimally close trajectories Z(t) and (t) Z0 in phase space. 

Exemple en finance avec réseau de neurones : deux mesures de Lyapunov comme signal de chaos à la bourse de Paris 
http://www.numdam.org/article/JSFS_1994__135_3_45_0.pdf

Pour des processus ayant une composante aléatoire et une composante chaotique, les
réseaux permettent de signaler cette dernière et donc le caractère en partie chaotique
du processus. 

 La rétro-propagation est
une procédure qui minimise la somme des carrés des erreurs par rapport aux
connexions. La procédure consiste à remplacer itérativement les coefficients a^ et ch
jusqu'à atteindre une valeur minimale de la somme des carrés des erreurs.
Il n'est donc pas besoin de définir une forme structurelle de la fonction F(*).
Seule la fonction de transfert #(•)> qui envoie les valeurs des inputs aux cellules
cachées, est définie et permet d'introduire la non linéarité dans la relation entre les
entrées et les sorties.
Dans le cas qui nous concerne, nous ne possédons comme information que la
série univariée [xt] comme représentation temporelle d'un phénomène dont la forme
de la fonction JF(») sous-jacente est ignorée. Le calcul de l'exposant de Lyapunov de
cette fonction passe par la connaissance des dérivées premières. L'algorithme de Wolf
travaille directement sur une estimation des dérivées de la fonction inconnue tandis
qu'avec la méthode de Kaashoek et Van Dijk (1991) à l'aide des réseaux de neurones,
on cherche d'abord à approcher la fonction F(«) afin de déduire ensuite les dérivées.
Ainsi, ils n'obligent pas à spécifier la forme structurelle de F(-) a priori. C'est un
avantage très important car dans le domaine de la non linéarité, il est très difficile,
quasiment impossible même, de déterminer cette forme. Les réseaux de neurones
dépassent cette difficulté et permettent un nouveau mode de détermination de l'exposant de Lyapunov. 

La rétro-propagation est
une procédure qui minimise la somme des carrés des erreurs par rapport aux
connexions. La procédure consiste à remplacer itérativement les coefficients a^ et ch
jusqu'à atteindre une valeur minimale de la somme des carrés des erreurs. 

# Estimateur optimal

http://www.ferdinandpiette.com/blog/2011/04/le-filtre-de-kalman-de-lestimateur-optimal-au-filtre-de-kalman/

Un estimateur dont le biais est nul aura une variance toujours supérieur ou égale à ce que l'on appelle la "borne de Cramer-Rao"

Le filtre de Kalman est donc une méthode d'estimation très puissante. Mais elle possède plusieurs faiblesses. Tout d'abord, le modèle doit être linéaire. Heureusement, il existe une variante de ce filtre, appelé le filtre de Kalman étendu qui permet de résoudre des problèmes non linéaire, bien que la stabilité de l'estimateur ne soit plus assurée. Une autre méthode qui, dans certains cas, est plus puissante que le filtre de Kalman est le filtre particulaire.

https://en.wikipedia.org/wiki/Multilayer_perceptron

In MLPs some neurons use a nonlinear activation function that was developed to model the frequency of action potentials, or firing, of biological neurons.

Learning occurs in the perceptron by changing connection weights after each piece of data is processed, based on the amount of error in the output compared to the expected result. This is an example of supervised learning, and is carried out through backpropagation, a generalization of the least mean squares algorithm in the linear perceptron.

https://en.wikipedia.org/wiki/Universal_approximation_theorem
... multilayer feed-forward architecture itself which gives neural networks the potential of being universal approximators

### Implémentation

https://github.com/shaunramsey/FractalExploration/blob/master/Fractals/Markus-Lyapunov%20Fractals/lyapunov_fractal_stochastic.py

https://github.com/antoinedelplace/PatternFlow/tree/master/fractals/lyapunov_fractal


