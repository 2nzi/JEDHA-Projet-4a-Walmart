<div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Walmart_logo.svg/1280px-Walmart_logo.svg.png" height="100px">
</div>


🛒 Prédiction des ventes Walmart

### Résumé

**Objectif** : Développer un modèle d'apprentissage automatique pour prévoir les ventes hebdomadaires des magasins Walmart, aidant les décisions marketing en comprenant les moteurs de vente.

**Approche** : 
1. **Exploration de données (Partie 1) :** Effectuer une analyse exploratoire des données (EDA) et prétraiter les données pour les préparer à l'apprentissage automatique.
   
2. **Modèle de régression linéaire de base (Partie 2) :** Entraîner un modèle de régression linéaire simple pour prédire le montant des ventes hebdomadaires en fonction des autres variables. Évaluer les performances du modèle et interpréter les coefficients pour identifier les caractéristiques importantes pour la prédiction.

3. **Éviter le surajustement (Partie 3) :** Entraîner un modèle de régression linéaire régularisé (Ridge ou Lasso) pour réduire le surajustement. Fine-tuning des hyperparamètres pour obtenir les meilleures prédictions généralisées.

**Résultat** : Amélioration de la prévision des ventes, permettant des stratégies marketing informées pour Walmart.

<br>
<br>
<br>

### Résultats

Le jeu de données était extrêmement petit avec seulement `150 échantillons`, et après prétraitement, `9%` des échantillons de données ont été supprimés. La visualisation de la distribution des données et de leurs relations nous a permis d'obtenir quelques insights sur l'ensemble des fonctionnalités. Tester plusieurs algorithmes avec des hyperparamètres par défaut nous a donné une certaine compréhension des performances des différents modèles sur cet ensemble de données spécifique.

Finalement, le meilleur modèle est un compromis entre la simplicité à l'aide du feature engineering, du choix de colonnes et la complexité de l'amélioration des hyperparamètres. C'est ainsi que le dernier `modèle Lasso` avec uniquement les colonnes Stores permet d'obtenir un score de précision de `0.953` sur le `X_train` et de `0.960` sur le `X_test`, avec un score de `cross-validation de 0.92`.

<br><br>
<br>


### Améliorations

On observe une grande disparité de ventes entre les magasins, il serait intéressant d'obtenir des informations de meilleure qualité et plus détaillées, afin d'explorer davantage de facteurs influençant les ventes. Par exemple, une analyse de la localisation des magasins ou d'autres caractéristiques spécifiques pourrait être extrêmement bénéfique pour expliquer la disparité importante des ventes entre les magasins.

En développant cette idée, une `approche géospatiale` pourrait être utilisée pour examiner les performances de vente en fonction de la localisation des magasins, en tenant compte de facteurs tels que la `densité de population`, le `revenu moyen` dans la région, la `concurrence locale`, et d'autres variables géographiques pertinentes. Cette analyse plus approfondie pourrait fournir des informations précieuses sur les facteurs locaux qui influent sur les ventes et aider à identifier les `opportunités d'amélioration` et de `croissance pour chaque magasin`.
