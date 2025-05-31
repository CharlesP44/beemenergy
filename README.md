# beemenergy
# ![image](https://github.com/user-attachments/assets/1373b66d-3dfc-4d42-b76e-ec2e4c5ae319)
 Beem Energy - Intégration Home Assistant

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

---

## 📊 Tableau de bord Lovelace (optionnel)

Un tableau de bord Lovelace personnalisé est disponible pour visualiser les données de votre batterie Beem.

### 🧩 Carte Power Flow (requis)

La visualisation utilise la carte personnalisée **Power Flow Card Plus**, disponible via HACS.

### Installation via HACS :

1. Ouvrez HACS > Frontend.
2. Recherchez **Power Flow Card Plus**.
3. Cliquez sur "Installer" puis redémarrez Home Assistant si nécessaire.

> ℹ️ Pour plus d’infos : [Power Flow Card Plus sur GitHub](https://github.com/Topix90/power-flow-card-plus)

#### 🔧 Installation

1. Allez dans **Paramètres > Tableaux de bord > Ajouter un tableau de bord**.
2. Cliquez sur **Configurer via YAML** (ou utilisez un *dashboard existant*).
3. Copiez-collez le contenu du fichier [`lovelace_dashboard.yaml`](./lovelace_dashboard.yaml) fourni dans le dépôt.
4. Ajustez les noms des entités si nécessaire (selon votre configuration Home Assistant).

> 💡 Le tableau de bord a été conçu pour une batterie Beem. Vous pouvez bien sûr l’adapter selon vos besoins.

---

### Aperçu

![aperçu lovelace](./screenshots/lovelace_preview.png)
