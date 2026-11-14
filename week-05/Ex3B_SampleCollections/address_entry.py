contact_info = {
    "name": "Epha Nesenw",
    "address": "0114 Oak Street",
    "city": "Oakland",
    "state": "CA",
    "zip": "94604"
}

print(contact_info["name"])
print(contact_info["address"])
print(contact_info["city"] + ", " + contact_info["state"] + " " + contact_info["zip"])

contact_info.pop("name")

full_name ={
    "first name": "Epha",
    "last name": "Nesenw"
}
print(full_name)
full_name.update({"honorific": "Ms."})
print(full_name)

contact_info.update(full_name)
print(contact_info)

print(contact_info["honorific"], contact_info["first name"], contact_info["last name"])
print(contact_info["address"])
print(contact_info["city"] + ", " + contact_info["state"] + " " + contact_info["zip"])

