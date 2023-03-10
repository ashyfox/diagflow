# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import dialogflowcx_v3  #pip install google-cloud-dialogflow-cx
import google.auth
from pprint import pprint
from googleapiclient import discovery
from google.oauth2 import service_account
from oauth2client.client import GoogleCredentials
import os
from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3beta1.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3beta1.types import session
from google.api_core.exceptions import AlreadyExists
import pytz
from datetime import datetime

def create_entity_type():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/bill/Desktop/python/diagflow_create_enity/seminar-and-workshop-c0371351149b.json"


    project_id = "seminar-and-workshop"


    api_endpoint = "us-central1-dialogflow.googleapis.com:443"
    client_options = {"api_endpoint": api_endpoint}
    client = dialogflowcx_v3.EntityTypesClient(client_options=client_options)
    parent = "projects/seminar-and-workshop/locations/us-central1/agents/e6cd039c-7d0e-418b-b8dd-14d460263881"
    # Initialize request argument(s)
    df = dialogflowcx_v3.EntityType()

    df.display_name = "display_name_value"

    #----------- kind map -----------
    df.kind = "KIND_MAP"
    entity_entries = [
        df.Entity(value="william", synonyms=["senior", "coding"]),
        df.Entity(value="aaron", synonyms=["manager", "speeching"]),
        df.Entity(value="julia", synonyms=["junior", "testing"]),
    ]

    # Set the entities field to the list of entity entries
    df.entities = entity_entries

    # #----------- kind list -----------
    # df.kind = "KIND_LIST"
    # # Define the entities with their synonyms
    # entities = [
    #     df.Entity(value="william", synonyms=["william"]), #correct
    #     df.Entity(value="aaron", synonyms=["manager", "speeching"]), #error

    # ]

    # # Set the entities field to the list of entities
    # df.entities = entities



    request = dialogflowcx_v3.CreateEntityTypeRequest(
        parent = parent,
        entity_type = df,
    )
    # # Make the request
    # response = client.create_entity_type(request=request)
    # # Handle the response
    # print(response)


    try:
        # code for creating the entity type
        response = client.create_entity_type(request=request)
        print("Entity type created:", response)
    except AlreadyExists as e:
        error_message = str(e)
        start_index = error_message.find("entityTypes/") + len("entityTypes/")
        end_index = error_message.find("'", start_index)
        entity_type_id = error_message[start_index:end_index]
        display_name_start_index = error_message.find("'") + 1
        display_name_end_index = error_message.find("'", display_name_start_index)
        display_name = error_message[display_name_start_index:display_name_end_index]
        now = datetime.now(pytz.timezone('Asia/Shanghai'))
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Entity type already exists with display name '{display_name}'")
        with open("error_log.txt", "a") as file:
            file.write(f"{time_str} Entity type with display name '{display_name}' already exists.\n")

if __name__ == '__main__':
    create_entity_type()