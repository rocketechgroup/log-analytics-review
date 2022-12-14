# Log Analytics Preview
Test out some amazing features from the new Log Analytics current in Preview. 

## Deploy a log tester to Cloud Function
```
export PROJECT_ID=<replace with your gcp project id>
export SA_NAME_FUNC=cloud-function-log-tester
```

```
gcloud iam service-accounts create ${SA_NAME_FUNC}

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
   --member "serviceAccount:${SA_NAME_FUNC}@${PROJECT_ID}.iam.gserviceaccount.com" \
   --role "roles/logging.logWriter"

gcloud functions deploy log_test \
    --runtime python38 \
    --trigger-http \
    --entry-point log_tester \
    --region europe-west2 \
    --security-level secure-always \
    --run-service-account ${SA_NAME_FUNC}
```

## SQL query samples
There are two SQL query samples shows how to make use of the powerful JSON data type.
See [SQL Samples](sql_samples)

## Additional reading
- [Log Analytics GCP blog](https://cloud.google.com/blog/products/data-analytics/moving-to-log-analytics-for-bigquery-export-users)
- [BigQuery Search Index](https://cloud.google.com/blog/products/data-analytics/pinpoint-unique-elements-with-bigquery-search-features)