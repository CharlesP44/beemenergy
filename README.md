# beemenergy
# 🐝 Beem Energy - Intégration Home Assistant

Intégration personnalisée pour [Home Assistant](https://www.home-assistant.io/) permettant de connecter les équipements Beem Energy (batterie, panneaux solaires, prises connectées, etc.) à votre installation domotique.

> ⚠️ Actuellement, seule la **batterie Beem** est pleinement testée. D'autres équipements sont en cours de validation.

---

## ✨ Fonctionnalités

- Récupération des données en temps réel de la batterie Beem :
  - État de charge
  - Puissance entrante/sortante
  - Historique de production/consommation
- Rafraîchissement automatique des données
- Gestion de l’authentification avec renouvellement du token

---

## 🚧 État actuel

Cette intégration est en cours de développement et nécessite des retours de la communauté, notamment pour :
- Tester avec d’autres produits Beem (panneaux, prises, etc.)
- Remonter les bugs ou comportements inattendus
- Suggérer des améliorations

---

## 🛠️ Installation

### 1. Via HACS (recommandé à terme)
> Pas encore disponible via le store HACS officiel.

### 2. Installation manuelle

1. Téléchargez les fichiers de ce dépôt.
2. Copiez le dossier `beem_integration` dans le répertoire `custom_components/` de votre instance Home Assistant.
3. Redémarrez Home Assistant.
4. Ajoutez l’intégration via **Paramètres > Appareils et services > Ajouter une intégration** puis cherchez **Beem Energy**.

---

## 🔐 Configuration

L'intégration nécessite :
- Votre **adresse email** utilisée sur l’application Beem
- Votre **mot de passe** utilisée sur l’application Beem

Ces informations sont utilisées uniquement pour récupérer un **token d’accès sécurisé** et ne sont pas stockées localement.

---

## 🧪 Tests & retours

Si vous disposez d’autres produits Beem (hors batterie), votre aide est précieuse pour tester et faire évoluer l’intégration.

N’hésitez pas à :
- Ouvrir une *issue* pour signaler un bug
- Proposer une amélioration via une *pull request*
- Rejoindre la discussion sur le [forum HACF](https://forum.hacf.fr)

---

## 🙏 Remerciements

Merci à la communauté HACF pour les échanges et en particulier à @jrvrcd pour l’aide initiale sur l’authentification.

---

## 📄 Licence

Ce projet est distribué sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d’informations.
