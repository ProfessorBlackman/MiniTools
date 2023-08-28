import json

import cloudinary
import cloudinary.uploader
import cloudinary.api
import decouple


class CloudinaryService:
    CLOUDINARY_URL = decouple.config("CLOUDINARY_URL")
    config = cloudinary.config(secure=True)

    def upload_image(self, file_to_upload: str, public_id: str):
        cloudinary.uploader.upload(file_to_upload,
                                   public_id=public_id, unique_filename=False, overwrite=True)

        src_url = cloudinary.CloudinaryImage(public_id).build_url()

        return src_url

    def getAssetInfo(self, public_id: str):
        image_info = cloudinary.api.resource(public_id)
        print("****3. Get and use details of the image****\nUpload response:\n", json.dumps(image_info, indent=2), "\n")

        if image_info["width"] > 900:
            update_resp = cloudinary.api.update(public_id, tags="large")
        elif image_info["width"] > 500:
            update_resp = cloudinary.api.update(public_id, tags="medium")
        else:
            update_resp = cloudinary.api.update(public_id, tags="small")

        # Log the new tag to the console.
        print("New tag: ", update_resp["tags"], "\n")
        return image_info
