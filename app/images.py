from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

# ImageKit SDK only requires private_key for server-side uploads
# public_key and url_endpoint are only needed for client-side rendering
image_kit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
)

# Store endpoint separately for frontend URL construction
IMAGEKIT_URL_ENDPOINT = os.getenv("IMAGEKIT_URL")