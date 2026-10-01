# Analyse de la consommation automobile (dataset MPG)

Analyse exploratoire d'un jeu de données de 398 véhicules américains, européens et japonais commercialisés entre 1970 et 1982, afin d'identifier les facteurs qui expliquent la consommation de carburant.

## Données

| Source | [seaborn-data / mpg.csv](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv) |
|---|---|
| Taille | 398 lignes × 9 colonnes |
| Période | Modèles 1970 à 1982 |

| Colonne | Description |
|---|---|
| `mpg` | Consommation en miles par gallon (plus la valeur est élevée, moins le véhicule consomme) |
| `cylinders` | Nombre de cylindres |
| `displacement` | Cylindrée du moteur |
| `horsepower` | Puissance en chevaux |
| `weight` | Poids en livres |
| `acceleration` | Temps d'accélération |
| `model_year` | Année du modèle |
| `origin` | Provenance : usa, japan, europe |
| `name` | Nom du modèle |

## Outils

Python · pandas

## Démarche

**1. Diagnostic** — Inspection de la structure (`info`, `describe`), recherche de valeurs manquantes, de doublons et de valeurs aberrantes.

**2. Nettoyage** — Une seule colonne incomplète : `horsepower`, avec 6 valeurs manquantes sur 398 (1,5 %). Ces valeurs ont été remplacées par la **médiane** de la colonne plutôt que supprimées : le volume concerné est négligeable, et la médiane reste représentative malgré la présence de quelques véhicules très puissants qui tireraient la moyenne vers le haut. Aucun doublon ni valeur aberrante n'a été détecté.

**3. Analyse** — Statistiques descriptives et agrégations par origine, nombre de cylindres et période, puis croisement de ces variables.

## Résultats

**Consommation moyenne de l'échantillon : 23,5 mpg**

### Par origine

| Origine | Consommation (mpg) | Poids moyen (livres) |
|---|---|---|
| Japon | 30,5 | 2 221 |
| Europe | 27,9 | 2 423 |
| USA | 20,1 | 3 362 |

Les deux classements sont exactement inversés : l'origine la plus légère est la plus sobre.

### Par nombre de cylindres

| Cylindres | Consommation (mpg) |
|---|---|
| 4 | 29,3 |
| 6 | 20,0 |
| 8 | 15,0 |

Les motorisations à 3 et 5 cylindres ont été écartées de la lecture : trop peu représentées pour que leur moyenne soit fiable.

### Évolution dans le temps

| Période | Consommation (mpg) |
|---|---|
| Avant 1976 | 19,4 |
| À partir de 1976 | 27,0 |

Soit un gain de 39 %, concomitant aux chocs pétroliers de 1973 et 1979.

### Croisement origine × période

| Origine | Avant 1976 | À partir de 1976 | Gain |
|---|---|---|---|
| USA | 16,6 | 23,6 | +42 % |
| Europe | 25,1 | 30,4 | +21 % |
| Japon | 26,2 | 32,4 | +24 % |

Les constructeurs américains ont le plus progressé, partant du niveau le plus bas. L'écart demeure néanmoins : les américaines récentes (23,6) consomment encore davantage que les européennes antérieures à 1976 (25,1).

### Véhicule le plus sobre

**Mazda GLC** — 46,6 mpg, 4 cylindres, 65 chevaux, modèle 1980, origine japonaise.

## Conclusion

Le **poids** est le facteur déterminant de la consommation : déplacer une masse plus importante exige davantage d'énergie, et les autres variables du jeu de données ne font que pointer vers lui.

L'**origine** n'est pas une cause mais un indicateur indirect : elle reflète le type de véhicule produit dans chaque pays. Les américaines consomment 50 % de plus que les japonaises parce qu'elles pèsent 50 % de plus. Le **nombre de cylindres** relève de la même logique — un moteur à 8 cylindres équipe un véhicule lourd.

L'**année** agit différemment : elle date un changement de conception. Après les chocs pétroliers, les constructeurs ont allégé leurs modèles, faisant passer la consommation moyenne de 19,4 à 27,0 mpg.

La Mazda GLC réunit tous ces traits : légère, petit moteur, récente.

## Contenu du dépôt

```
mpg.csv            Jeu de données
main.py            Code de l'analyse
requirements.txt   Dépendances Python
.gitignore         Fichiers exclus du dépôt
README.md          Ce fichier
```

## Exécution

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Auteur

El Hadji Birane Cisse Thiam — [GitHub](https://github.com/BiraneThiam2)

Projet réalisé dans le cadre d'une formation en intelligence artificielle.
