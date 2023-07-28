*****************
Monitoring Podv2
*****************

URLs
====


Deployer les métriques:
======================

1) Ajouter les machines dans le fichier hosts (en fonction des exporters à installer)
2) lancer les playbooks:

.. code::

    ansible-playbook node_exporter.yml -i hosts

3) Ajouter les machines dans Prometheus:


