import boto3
from . import datetime
from . import s3


transcribe_client = boto3.client('transcribe', region_name=s3.get_bucket_region())


def start_video_resource_transcription(resource_id):
    # try:
        response = transcribe_client.start_transcription_job(
            TranscriptionJobName=_get_transcription_job_name(resource_id),
            IdentifyLanguage=True,
            MediaFormat='mp4',
            Media={
                'MediaFileUri': s3.get_resource_video_file_url(resource_id)
            },
            OutputBucketName=s3.get_bucket_name(),
            OutputKey=_get_transcription_job_path(resource_id),
            Subtitles={
                'Formats': ['vtt']
            },
            Tags=[{
                'Key': 'resource_id',
                'Value': str(resource_id)
            }]
        )
        return response, None
    # except Exception as e:
    #     return None, e


def _get_transcription_job_name(resource_id):
    return 'resource_' + str(resource_id) + '_' + datetime.get_date_time_string()


def _get_transcription_job_path(resource_id):
    return s3.get_resource_directory(resource_id) + 'transcription.json'
