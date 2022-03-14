import io
import base64
from classroomapi.models import Result, Resource, Clip
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError


_IMG_BLOB_PREFIX = b'data:image/jpeg;charset=utf-8;base64,'


def create_clips_for_resource(r: Resource, upload_url: str) -> Result:
    images_result = get_images_from_pdf(upload_url)
    if images_result.is_error:
        return Result(error=images_result.error)

    for idx, val in enumerate(images_result.data):
        c = Clip(course_id=r.course_id,
                 resource_id=r.id,
                 content=get_image_from_pdfimgdata(val),
                 description='',
                 type=Clip.ClipType.PDF_PAGE.value,
                 start_location=idx + 1,
                 end_location=idx + 1)
        c.save()
    return Result(data=True)


def get_images_from_pdf(url) -> Result:
    try:
        images = convert_from_path(url,
                                   size=(None, 100),
                                   hide_annotations=True)
        return Result(data=images)
    except PDFInfoNotInstalledError as e:
        return Result(error=str(e))
    except PDFPageCountError as e:
        return Result(error=str(e))
    except PDFSyntaxError as e:
        return Result(error=str(e))


def get_image_from_pdfimgdata(img) -> str:
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_bytes = base64.b64encode(buffered.getvalue())
    return (_IMG_BLOB_PREFIX + img_bytes).decode()
