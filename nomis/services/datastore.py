"""Module with the functionality of set entities in google cloud data store
"""


from google.cloud import datastore
from django.conf import settings


def set_datastore_range():
    """This function set the entities in google cloud datastore
    """
    try:
        client = datastore.Client()
        complete_key = client.key(settings.ENTITY_KIND, settings.ID_NAME)
        task = datastore.Entity(key=complete_key)

        task.update(
            {
                "category": "Learning DJANGO TODAY 8 marzo",
                "done": True,
                "priority": 10,
                "description": "Learn more and more python AND DJANGO",
            }
        )
        client.put(task)
        result = client.get(complete_key)
        print(result)
        return ("UPDATED")
    except Exception as e:
        print('{}'.format(e))
        return(e)
