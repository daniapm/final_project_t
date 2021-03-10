"""Module with the functionality of delete instances in google cloud tasks
"""


from pprint import pprint

import requests
from apiclient.discovery import build
from django.conf import settings


def delete_instances():
    """This function delete instances  in google cloud app engine"""

    appengine = build(serviceName="appengine", version="v1")
    active_instances_dict = (
        appengine.apps()
        .services()
        .versions()
        .instances()
        .list(
            servicesId=settings.SERVICE_ID,
            appsId=settings.PROJECT_ID,
            versionsId=settings.VERSION_ID,
        )
        .execute()
    )
    try:
        list_of_instances = active_instances_dict["instances"]
        for instance in list_of_instances:
            request = (
                appengine.apps()
                .services()
                .versions()
                .instances()
                .delete(
                    servicesId=settings.SERVICE_ID,
                    appsId=settings.PROJECT_ID,
                    versionsId=settings.VERSION_ID,
                    instancesId=instance["id"],
                )
            )
            response = request.execute()
            pprint(response["done"])
            return response["done"]
    except Exception as e:
        print("No key:{} to delete".format(e))
        return e
