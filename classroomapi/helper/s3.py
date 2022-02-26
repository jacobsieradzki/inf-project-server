import boto3
from botocore.exceptions import ClientError
from classroom.settings import AWS_S3_BUCKET_NAME, AWS_S3_REGION_NAME


s3_client = boto3.client('s3')


def get_bucket_base_url(): return 'https://' + get_bucket_name() + '.s3.' + get_bucket_region() + '.amazonaws.com/'
def get_bucket_name(): return AWS_S3_BUCKET_NAME
def get_bucket_region(): return AWS_S3_REGION_NAME


def get_resource_directory(rid): return 'resource/' + str(rid) + '/'
def get_resource_video_file_path(rid): return get_resource_directory(rid) + 'video.mp4'
def get_resource_video_file_url(rid): return get_bucket_base_url() + get_resource_video_file_path(rid)
def get_resource_pdf_file_path(rid): return get_resource_directory(rid) + 'document.pdf'
def get_resource_pdf_file_url(rid): return get_bucket_base_url() + get_resource_pdf_file_path(rid)


def upload_video_resource(resource_id, file):
    file_path = get_resource_video_file_path(resource_id)
    return _upload_file(resource_id, file, file_path, get_resource_video_file_url)


def upload_pdf_resource(resource_id, file):
    file_path = get_resource_pdf_file_path(resource_id)
    return _upload_file(resource_id, file, file_path, get_resource_pdf_file_url)


def _upload_file(resource_id, file, file_path, get_url):
    try:
        s3_client.upload_fileobj(file, get_bucket_name(), file_path, ExtraArgs={'ACL': 'public-read'})
        file_url = get_url(resource_id)
        return file_url, None
    except ClientError as e:
        return None, e


def delete_resource(resource_id):
    objects_to_delete = s3_client.list_objects_v2(Bucket=get_bucket_name(), Prefix=get_resource_directory(resource_id))
    delete_keys = {'Objects': [{'Key': k} for k in [obj['Key'] for obj in objects_to_delete.get('Contents', [])]]}
    return s3_client.delete_objects(Bucket=get_bucket_name(), Delete=delete_keys)


def get_object(key):
    try:
        return s3_client.get_object(Bucket=get_bucket_name(), Key=key)
    except Exception:
        return None


def get_object_text(key):
    retrieved_object = get_object(key)
    if not retrieved_object:
        return None
    contents = retrieved_object.get('Body').read()
    return contents.decode('utf-8')
