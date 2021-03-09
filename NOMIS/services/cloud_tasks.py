"""Module with the functionality of the queues in google cloud tasks
"""

from pprint import pprint

from google.cloud import tasks_v2beta3
from googleapiclient import discovery
from django.conf import settings


def resume_queues():
    """This function resume the queues in google cloud tasks
    """
    try:
        service = discovery.build('cloudtasks', 'v2')
        name = 'projects/{}/locations/{}/queues/{}'.format(settings.PROJECT_ID,
                                                        settings.LOCATION_ID,
                                                        settings.QUEUES_ID)
        request = service.projects().locations().queues().resume(name=name)
        response = request.execute()
        pprint(response['state'])
        return (response['state'])
    except Exception as e:
        return(e)

def pause_queues():
    """This function pause the queues in google cloud tasks"""
    try:
        service = discovery.build('cloudtasks', 'v2')
        name = 'projects/{}/locations/{}/queues/{}'.format(settings.PROJECT_ID,
                                                        settings.LOCATION_ID,
                                                        settings.QUEUES_ID)
        request = service.projects().locations().queues().pause(name=name)
        response = request.execute()
        pprint(response['state'])
        return (response['state'])
    except Exception as e:
        print('{}'.format(e))
        return(e)
