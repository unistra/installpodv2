# Install via Ansible

## Fichier  d'inventaire
Faire un fichier d'inventaire en se basant sur ceux disponibles
  * inventory : ~/git/installpodv2_ubuntu/inventories/podv2-test-ubuntu.yml


## Fichier de settings
  * Ils peuvent varier suivant les versions. 
  * Dans l'inventory : version_esup: '2.7.3'
  * Dans le répertoire templates/settings/version soit templates/settings/2.7.3 pour cette version, placer le fichier de settings.

## Playbook
  * playbook : ~/git/installpodv2/podv2-deploy.yml

##Rappel Vault
Vous devez disposer de la clé de decryptage du vault que vous mettrez dans le fichier .vault_podv2.txt (où vous voulez, il faudra juste se rappeler le chemin) afin d'eviter de la retaper à chaque fois que vous lancez un playbook.

si vous devez utilisez une autre clef de cryptage, il faudra lancer la commande suivante pour tous les mots de passe utilisés dans la recette:
```
ansible-vault encrypt_string --vault-password-file ~/ansible/.vault_podv2.txt 'mot de passe à crypter' --name 'nom de la variable dans la recette'
```


## git
```
cd ~
cd git
 git clone https://github.com/unistra/installpodv2.git
```

## Certficats
Afin d'activer le https, ajoutez les certificats dans le repertoire files de votre playbook.


## Commande d'install
  * Creer le user sur la machine

```
cd ~/git/installpodv2/
ansible-playbook --inventory ./inventories/podv2-test-ubuntu.yml --tags "user" --vault-password-file ~/ansible/.vault_podv2.txt podv2_deploy.yml -e "user_bastion=<login ent>"
```

```
cd ~/git/installpodv2/
ansible-playbook --inventory ./inventories/podv2-test-ubuntu.yml --tags "nfs,dir,python,git,tierces,encode,elasticsearch,postgresql,rabbitmq,celeryd,settings,initdb,initapp,nginxuwsgi,site,ssl,custom" --vault-password-file ~/ansible/.vault_podv2.txt podv2_deploy.yml -e "user_bastion=<login ent>"
```


## Superutilisateur
  * password du superutilisateur, <user_name> dans l'inventory, pour moi admin , il est crée par le playbook mais avec un password qu on ne connait pas donc on refait le password par suite
```
ssh root@pod26-test
su pod
cd /home/pod/django_projects
workon django_pod
(django_pod) pod@pod26-test:~/django_projects$ python manage.py changepassword admin
Changing password for user '  (admin)'
Password: 
Password (again): 
Password changed successfully for user '  (admin)'

```

## Les services

  * sudo service uwsgi-pod restart
  * sudo service rabbitmq-server restart
  * sudo service celeryd restart
  * sudo service elasticsearch restart
  * sudo service nginx restart


