from power.configuration.gcloud import GCloud

obj = GCloud()

obj.sync_folder_from_gcloud(gcp_bucket_url = "power24", filename="power.zip", destination="tests")