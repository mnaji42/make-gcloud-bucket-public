# make-google-cloud-bucket-public

## Prerequisite

Make sure `python` is installed

Make sure `gcloud cli` is installed
see documentation [here](https://cloud.google.com/sdk/docs/install?hl=fr)

Make sure `google-cloud-storage` is installed or run

```
pip install google-cloud-storag
```

## Connexion

Make your local application to temporarily use your own user credentials for API access, run:

```
gcloud auth application-default login
```

## Make your bucket public

Run the following command and it's done:

```
python3 make-bucket-public.py
```
