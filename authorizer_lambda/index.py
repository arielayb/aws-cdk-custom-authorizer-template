# authorizer_lambda/index.py
def lambda_handler(event, context):
    token = event.get('authorizationToken')
    
    # Logic to validate token (e.g., JWT verification)
    is_authorized = (token == "secret-token")
    effect = "Allow" if is_authorized else "Deny"
    context = {
        "principalId": "user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": 
            {
                "Action": "execute-api:Invoke",
                "Effect": "Allow",
                "Resource": ""
            }
            
        }
    }

    return context
