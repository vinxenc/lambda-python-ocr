from mangum import Mangum
from app import app
# Configure Mangum with explicit API Gateway version
handler = Mangum(app, lifespan="off", api_gateway_base_path="/")
