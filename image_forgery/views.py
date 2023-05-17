from django.http import HttpResponse, HttpResponseNotFound, FileResponse
from django.template import loader
import uuid, os
from django.views.decorators.csrf import csrf_exempt
from . import cmf_detect, settings
from io import BytesIO
import cv2



def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        random_uuid = uuid.uuid4()
        file_extension = uploaded_file.name.split('.')[-1]
        new_filename = f'{settings.MEDIA_ROOT}{random_uuid}.{file_extension}'


        print(new_filename)
        # do something with the uploaded file, e.g. save it to disk
        with open(new_filename , 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)
        imag = cmf_detect.cmf_Detect(new_filename)
        print("image_path", imag)

            # Read the image file
        img = cv2.imread(imag)

            # Encode the image as a JPEG binary stream
        img_buffer = BytesIO()
        success, encoded_img = cv2.imencode('.jpg', img)
        if success:
            img_buffer.write(encoded_img)

        # Return the encoded image as the response content
        response = HttpResponse(img_buffer.getvalue(), content_type='image/jpeg')
        return response
        
        # Construct the response
        response = HttpResponse(content_type='image/jpeg')
        cv2.imwrite(response, img)
        
        # # Construct the response
        # response = HttpResponse(content_type='image/jpeg')
        # cv2.imwrite(response, imag)
        
        return response
        
       