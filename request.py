[7:24 PM, 12/2/2024] Zohaib Cyberify: from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from typing import Annotated
from jwt import decode
from models.login import User

security = HTTPBearer()
private_key = "dkjimfkmdfm#8jcenvnuunueuhurhdhdjhdfytwygd"

async def get_current_user(security_details: Annotated[HTTPAuthorizationCredentials, Depends(security)]):   
    try:
        token = security_details.credentials
        user_info = decode(token, private_key, algorithms=["HS256"])
        print("user info", user_info)
        user_id = user_info["user_id"]
        user = await User.filter(id=user_id).first()
        if not user:
            raise Exception("")
        return user
    except Exception as e:
        print(e)
        raise HTTPException(401, "Unauthorized")
      
@router.get('/todo')
async def get_todo(user: Annotated[User, Depends(get_current_user)]):
    print(user)
