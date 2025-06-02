# ![image](https://github.com/user-attachments/assets/c42b3ca3-a681-4091-a13c-f2d0f8f4fc9c) Beem Energy - Intégration Home Assistant ![image](https://github.com/user-attachments/assets/b16dce18-3b0b-4108-9b37-4ebd67372f71)
 
Intégration **non officielle** permettant de connecter les équipements **Beem Energy** à Home Assistant.


> ⚠️ Actuellement, seule la **batterie Beem** est pleinement testée. D'autres équipements sont en cours de validation.

---
## ⚙️ Fonctionnalités / ## ✨ Fonctionnalités
☀️ Détection et détails des équipements solaires connectés
📊 Récupération automatique des données live toutes les 60 secondes
🔋 Affichage de la capacité, charge, production, consommation
🔐 Stockage sécurisé du mot de passe dans Home Assistant
🔁 Rafraîchissement automatique du token expiré


## 🚧 État actuel

Cette intégration est en cours de développement et nécessite des retours de la communauté, notamment pour :
- Tester avec d’autres produits Beem (panneaux, prises, etc.)
- Remonter les bugs ou comportements inattendus
- Suggérer des améliorations

---

## 🛠️ Installation / 🧰 Installation via HACS
### 1. Via HACS (recommandé à terme)
Pas encore disponible via le store HACS officiel.

### 2. Via HACS (Dépôts personnalisés)
1. Ouvrez HACS dans Home Assistant
2. Cliquez sur Intégrations puis sur les 3 points en haut à droite
3. Sélectionnez Dépôts personnalisés
4. Entrez : https://github.com/<TON_COMPTE>/<TON_REPO>
   Type : Intégration
5. Une fois ajouté, recherchez **Beem Energy** dans HACS et installez-le
6. Redémarrez Home Assistant

### 3. Installation manuelle
1. Téléchargez les fichiers de ce dépôt.
2. Copiez le dossier `beem_integration` dans le répertoire `custom_components/` de votre instance Home Assistant.
3. Redémarrez Home Assistant.
5. Ajoutez l’intégration via **Paramètres > Appareils et services > Ajouter une intégration** puis cherchez **Beem Energy**.

---

## 🔐 Configuration / 🔧 Configuration
1. Allez dans Paramètres > Appareils & Services
2. Cliquez sur Ajouter une intégration
3. Recherchez Beem Energy
4. Saisissez 
   - Votre **adresse email** utilisée sur l’application Beem
   - Votre **mot de passe** utilisée sur l’application Beem

⚠️ Remarque : votre token d’authentification est renouvelé automatiquement si expiré.

---

## 👨‍💻 Codeowners & Développement
🧑‍💻 Auteur : @CharlesP44


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

**Il n’est pas affilié officiellement à Beem Energy.**

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
