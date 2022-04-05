import boto3
from botocore.exceptions import ClientError
from classroom.settings import AWS_S3_BUCKET_NAME, AWS_S3_REGION_NAME
import re


s3_client = boto3.client('s3')


def get_bucket_base_url(): return 'https://' + get_bucket_name() + '.s3.' + get_bucket_region() + '.amazonaws.com/'
def get_bucket_name(): return AWS_S3_BUCKET_NAME
def get_bucket_region(): return AWS_S3_REGION_NAME


def _format_file_name(name: str):
    no_spaces = re.sub(r'\s', '_', name.lower())
    return re.sub(r'[^a-z0-9_]', '', no_spaces)


def get_resource_directory(rid): return 'resource/' + str(rid) + '/'
def get_resource_video_file_path(rid, name): return get_resource_directory(rid) + _format_file_name(name) + '.mp4'
def get_resource_video_file_url(rid, name): return get_bucket_base_url() + get_resource_video_file_path(rid, name)
def get_resource_pdf_file_path(rid, name): return get_resource_directory(rid) + _format_file_name(name) + '.pdf'
def get_resource_pdf_file_url(rid, name): return get_bucket_base_url() + get_resource_pdf_file_path(rid, name)


def upload_video_resource(resource_id, file, file_name='video'):
    file_path = get_resource_video_file_path(rid=resource_id, name=file_name)
    url = get_resource_video_file_url(rid=resource_id, name=file_name)
    return _upload_file(file, file_path, url)


def upload_pdf_resource(resource_id, file, file_name='document'):
    file_path = get_resource_pdf_file_path(resource_id, file_name)
    url = get_resource_pdf_file_url(resource_id, file_name)
    return _upload_file(file, file_path, url)


def _upload_file(file, file_path, file_url):
    try:
        s3_client.upload_fileobj(file, get_bucket_name(), file_path, ExtraArgs={'ACL': 'public-read'})
        return file_url, None
    except ClientError as e:
        return None, e


def delete_resource(resource_id):
    objects_to_delete = s3_client.list_objects_v2(Bucket=get_bucket_name(), Prefix=get_resource_directory(resource_id))
    delete_keys = {'Objects': [{'Key': k} for k in [obj['Key'] for obj in objects_to_delete.get('Contents', [])]]}
    if len(delete_keys['Objects']) == 0:
        return
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
