import io
import base64
from classroomapi.models import Result
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError


_IMG_BLOB_PREFIX = b'data:image/jpeg;charset=utf-8;base64,'


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
