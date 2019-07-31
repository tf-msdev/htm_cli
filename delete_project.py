from swaggerAPIClient.swagger_client.api import project_admin_api

to_delete = [474]

for proj in to_delete:
    print(proj)
    reply = project_admin_api.ProjectAdminApi().api_v1_admin_project_project_id_delete("Token TVRBeE1qY3pOVEkuRUNDYm9BLnlCbzNQNTBIR19PRFZvbTdsSVRJOVRlbVZUSQ==", proj, _preload_content=False)
    print(reply.data.decode())