package example.authz

default allow = false

allow {
    input.user.role == "admin"
    input.method == "GET"
    input.path == "/resource"
}
