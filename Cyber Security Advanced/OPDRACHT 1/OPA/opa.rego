package barmanagement #namespace
default allow := false

import input.request.headers.Authorization

allow {
    jwt_token := extract_bearer_token(input.request.headers.Authorization)
    [jwt_header, jwt_payload, jwt_signature] := io.jwt.decode(jwt_token)
    user_age := to_number(jwt_payload.age)
    user_role := jwt_payload.role[_]
    user_role == "customer"
    input.request.body.DrinkName == "Beer"
    user_age >= 16
    input.request.method == "POST"
    input.request.path != "/api/managebar"
}

allow {
    jwt_token := extract_bearer_token(input.request.headers.Authorization)
    [jwt_header, jwt_payload, jwt_signature] := io.jwt.decode(jwt_token)
    user_role := jwt_payload.role[_]
    user_role == "customer"
    input.request.body.DrinkName != "Beer"
    input.request.method == "POST"
    input.request.path != "/api/managebar"
}

allow {
    jwt_token := extract_bearer_token(input.request.headers.Authorization)
    [jwt_header, jwt_payload, jwt_signature] := io.jwt.decode(jwt_token)
    user_role := jwt_payload.role[_]
    user_role == "bartender"
    input.request.method == "POST"
    input.request.path == "/api/managebar"
}

extract_bearer_token(auth_header) = token {
    startswith(auth_header, "Bearer ")
    token := substring(auth_header, 7, -1)
}