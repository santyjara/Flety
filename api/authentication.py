class Authenticator:
    pass

    @staticmethod
    def _process_bearer_token(token: str) -> UserRequestModel:
        """
        Processes the authentication bearer token sent as a header with incoming
        requests and returns a `UserRequestModel`.
        """
        try:
            decoded_token = jwt.decode(
                token,
                key=None,
                options={"verify_signature": False, "verify_aud": False},
            )
        except ExpiredSignatureError:
            raise AuthenticationError("Credentials are expired")

        user = UserRequestModel.parse_obj(decoded_token)
        return user
