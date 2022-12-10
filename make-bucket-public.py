from google.cloud import storage

bucket_name = '<the_name_of_your_bucket>'
my_bucket = client.get_bucket(bucket_name)

acl_access = ['allUsers', ] #['allUsers, 'allAuthenticatedUsers']

public_access_policy = my_bucket.get_iam_policy(requested_policy_version=3)

public_access_policy.bindings.append(
  {"role": "roles/storage.objectViewer", "members": acl_access}
)

my_bucket.set_iam_policy(public_access_policy)
