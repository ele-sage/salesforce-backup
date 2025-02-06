# Lancer le conteneur Docker pour Salesforce Backup

## Prérequis
- Docker et Docker Compose installés.
- Un dossier local pour stocker les backups.
- Un compte Salesforce avec les permissions nécessaires pour effectuer des backups.

## Étapes

1. **Modifier le chemin du volume bindé :**  
   Dans le fichier `compose.yml`, remplacez la valeur de `device` par le chemin absolu de votre dossier local.
   Exemple :
   ```yaml
      device: C:\Users\user\backups
   ```

2. **Créer un fichier .env :**  
   Créez un fichier `.env` à la racine du projet (`/salesforce-backup/.env`) pour définir les variables d'environnement nécessaire pour la conexion à Salesforce.
   Exemple de contenu du fichier `.env` :
   ```
    SF_USERNAME=your_username
    SF_PASSWORD=your_password
    SF_DOMAIN=https://your_domain.lightning.force.com
   ```

3. **Lancer le conteneur Docker :**  
   Exécutez la commande suivante dans le dossier du projet :
   ```bash
   docker-compose up --build
   ```

4. **Accéder au conteneur :**  
   Le conteneur `sf-backup` se lancera et utilisera le dossier bindé défini pour stocker les backups.
