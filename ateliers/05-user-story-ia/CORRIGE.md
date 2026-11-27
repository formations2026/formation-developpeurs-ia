# Corrigé — Atelier 5 : Revoir une user story « IA » (40 min)

> Branche formateur. Contenu d'introduction, pas un conseil juridique : la politique de l'entreprise,
> le service juridique et le DPO tranchent.

## Étape 1 — La grille des risques remplie
| Risque identifié | Catégorie | Gravité (1-3) | Remédiation proposée |
|---|---|---|---|
| Titres de réunion et participants envoyés à un LLM cloud (titres parfois très sensibles : « Entretien préalable ») | RGPD | 3 | N'envoyer que créneau, effectif, équipements ; fournisseur sous contrat |
| Lecture des agendas de **tous** les participants | RGPD | 3 | Ne lire que les disponibilités, pas les contenus |
| Priorité donnée au plus haut niveau hiérarchique | Biais, éthique | 3 | Priorité selon le besoin (effectif, équipement), jamais le grade |
| Annulation automatique sans recours | Éthique, RGPD (décision automatisée) | 2 | Notification, puis confirmation humaine avant annulation |
| Détection de présence par badge | RGPD, éthique (surveillance des salariés) | 3 | Supprimer, ou bouton « je suis là » ; sinon information des salariés et des représentants du personnel |
| Conservation deux ans « pour améliorer le modèle » | RGPD (finalité, durée) | 3 | Conservation courte, aucune réutilisation pour entraîner un modèle |
| Injection de prompt via un titre de réunion | Sécurité | 2 | Ne transmettre aucun texte libre au modèle |
| Transfert hors Union européenne | RGPD | 2 | Vérifier la localisation et les garanties du contrat |
| Coût non borné (un appel par réservation) | Coût | 1 | Plafond mensuel, cache, règles simples avant l'IA |

## Étape 2 — La user story réécrite
> **En tant que** salarié, **je veux** que l'outil me propose trois salles adaptées à ma réunion,
> **afin de** choisir rapidement.

Critères d'acceptation :
1. Le modèle ne reçoit que le créneau, le nombre de participants et les équipements demandés.
2. Aucun nom, titre de réunion ni niveau hiérarchique n'est transmis ni utilisé.
3. Le salarié choisit la salle : aucune réservation automatique.
4. Une réservation non utilisée déclenche une **notification**, puis une annulation seulement après **confirmation**.
5. Les salariés sont informés qu'une IA propose les salles.
6. Les requêtes au modèle ne sont pas conservées au-delà de 30 jours (durée à valider avec le DPO).

La valeur pour l'utilisateur est intacte : il gagne du temps. Seuls les risques ont disparu.

## Étape 3 — La note de décision
Exemple complet : `docs/adr/012-suggestion-salle.md`.

## Classement au sens du règlement européen sur l'IA (bonus)
- **Version initiale** : un système qui évalue ou classe des salariés (priorité selon le grade, suivi de présence)
  touche aux domaines de l'emploi listés comme **à haut risque** : à faire analyser par le juridique.
- **Version remédiée** : un assistant qui propose des salles sur des critères matériels relève vraisemblablement
  du niveau **transparence** (informer qu'une IA intervient). À confirmer par le juridique.

## Étape 4 — L'exercice de code (biais)
Le test qui révèle le biais, puis la correction : [`test_corrige_atelier5.py`](test_corrige_atelier5.py)
et [`validation_noms_corrigee.py`](validation_noms_corrigee.py).

```python
@pytest.mark.parametrize("nom", ["Zoé N'Diaye-Lefèvre", "O'Brien", "Nguyễn Thị Minh Khai", "李小龍"])
def test_la_version_initiale_refuse_de_vrais_noms(nom):
    assert valider_nom_initiale(nom) is False   # le biais est prouvé
```
**La meilleure réponse** est souvent de **supprimer la règle** : « non vide et de longueur raisonnable »
(`valider_nom_minimal`) suffit. Le biais venait d'une validation inutile.

## Débrief (10 min)
- **« La priorité hiérarchique est-elle acceptable ? »** → Non : elle désavantage systématiquement les mêmes personnes, sans lien avec le besoin.
- **« Qu'est-ce qui a été le plus souvent oublié ? »** → L'injection par les titres, la conservation, le badge.
- **« Votre version garde-t-elle la valeur ? »** → C'est le critère de réussite : une remédiation qui tue la fonctionnalité n'en est pas une.

## Grille d'évaluation
| Critère | Acquis | En cours |
|---|---|---|
| Au moins six risques, dont un de chaque catégorie | | |
| Remédiation concrète pour chaque risque | | |
| User story réécrite, critères vérifiables | | |
| La valeur pour l'utilisateur est conservée | | |
