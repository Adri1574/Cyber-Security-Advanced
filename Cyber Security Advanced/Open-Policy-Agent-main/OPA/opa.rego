package barmanagement #namespace
default allow := false


allow {
    input.request.body.DrinkName == "Beer"
    age := to_number(input.request.body.age)
    age >= 16
}

allow {
    input.request.body.DrinkName == "Fristi"
}

allow {
    input.request.body.Role == "bartender"
}