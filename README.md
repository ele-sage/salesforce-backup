# Lancer le conteneur Docker pour Salesforce Backup

## Description du Conteneur

Le conteneur exécute une application Python qui automatise la connexion à Salesforce, détecte l'interface (Lightning ou Classic) et télécharge les fichiers de backup. Les backups sont enregistrés dans un volume bindé (ex: C:\Users\user\backups) sur votre machine locale.

## Prérequis
- Docker et Docker Compose installés.
- Un dossier local pour stocker les backups. ex: `C:\Users\user\backups`
- Un compte Salesforce avec les permissions nécessaires pour effectuer des backups.

## 

## Étapes

1. **Modifier le chemin du volume bindé :**  
   Dans le fichier `compose.yml`, remplacez la valeur de `device` par le chemin absolu de votre dossier local pour stocker les backups.

   ```yaml
      volumes:
        backups:
            driver: local
            driver_opts:
            type: none
            device: /path/to/your/backups
            o: bind
   ```

2. **Créer un fichier .env :**  
   Créez un fichier `.env` à la racine du projet (`/salesforce-backup/.env`) pour définir les variables d'environnement nécessaire pour la conexion à Salesforce.

   Le fichier `.env` doit contenir les variables suivantes :
    - `SF_USERNAME` : Nom d'utilisateur Salesforce.
    - `SF_PASSWORD` : Mot de passe Salesforce.
    - `SF_DOMAIN` : Domaine Salesforce.

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
