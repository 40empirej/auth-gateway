import os
import logging
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth_gateway.auth import Auth
from auth_gateway.database import Database

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the FastAPI app
app = FastAPI()

# Initialize the authentication and database dependencies
auth = Auth()
database = Database()

# Define the authentication scheme
security = HTTPBearer()

# Define the route for authentication
@app.post("/authenticate")
async def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        # Authenticate the user
        user = await auth.authenticate(credentials.credentials)
        # If authentication is successful, create a JWT token
        token = await auth.create_token(user)
        return {"token": token}
    except Exception as e:
        # Log any exceptions that occur during authentication
        logger.error(f"Error authenticating user: {e}")
        return JSONResponse(content={"error": "Invalid credentials"}, status_code=401)

# Define the route for protected resources
@app.get("/protected")
async def protected_resource(token: str = Depends(auth.get_token)):
    try:
        # Verify the JWT token
        user = await auth.verify_token(token)
        return {"message": f"Hello, {user['username']}!"}
    except Exception as e:
        # Log any exceptions that occur during token verification
        logger.error(f"Error verifying token: {e}")
        return JSONResponse(content={"error": "Invalid token"}, status_code=401)