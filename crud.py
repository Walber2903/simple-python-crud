def add_a_contact(contact_list, contact_name, contact_phone, contact_email, contact_favorite):
  favorite = contact_favorite
  if favorite == "y" or favorite == "Y":
    favorite = True
  else:
    favorite = False
  
  contact = {"name": contact_name, "phone": contact_phone, "email": contact_email, "favorite": favorite}
  contact_list.append(contact)
  print(f"\nThe contact {contact_name} was add to the list with success! \n")
  return

def list_contacts(contact_list):
  print("\nThis is your contact list: ")
  print("\n   Name      |    Phone    |   Email   |   Favorite   \n")
  for index, contact in enumerate(contact_list, start=1):
    contact_name = contact["name"]
    contact_phone = contact["phone"]
    contact_email = contact["email"]
    contact_favorite = contact["favorite"]
    print(f"{index}. {contact_name} | {contact_phone} | {contact_email} | {contact_favorite} \n")
  return

def update_contact(contact_list, contact_index):
  contact_index_verified = int(contact_index) - 1
  while True:
    if(contact_index_verified >= 0 and contact_index_verified < len(contact_list)):
      print("\nChoose a option to update the contact: \n")
      print("1. to update name.\n")
      print("2. to update phone.\n")
      print("3. to update email.\n")
      print("4. to leave update option \n")
      choice = input("Type your update option: ")
      
      if choice == "1":
        contact_list[contact_index_verified]["name"] = input("Type the new name: ")
        print(f"Contact name uptaded to {contact_list[contact_index_verified]['name']}. \n")
      elif choice == "2":
        contact_list[contact_index_verified]["phone"] = input("Type the new phone: ")
        print(f"Contact phone uptaded to {contact_list[contact_index_verified]['phone']}. \n")
      elif choice == "3":
        contact_list[contact_index_verified]["email"] = input("Type the new email: ")
        print(f"Contact email uptaded to {contact_list[contact_index_verified]['email']}. \n")
      elif choice == "4":
        break
    else:
      print("Type a valid index! \n")
  return

def update_favorite(contact_list, index_to_favorite):
  contact_index_verified = int(index_to_favorite) - 1
  if(contact_index_verified >= 0 and contact_index_verified < len(contact_list)):
    option_to_update = input("Type the favorite option y or n: ")
    if option_to_update == "y" or option_to_update == "Y":
      option_to_update = True
    else:
      option_to_update = False
    contact_list[contact_index_verified]["favorite"] = option_to_update
    print(f"Favorite option to contact name: {contact_list[contact_index_verified]['name']} uptaded to {contact_list[contact_index_verified]['favorite']}. \n")
  else:
    print("Type a valid index! \n")
  return

def list_favorites_contact(contact_list):
  favorite_list_contact = []
  print("\nThis is your Favorite Contact list:")
  for contact in contact_list:
    if contact["favorite"]:  
      favorite_contact_name = contact["name"]
      favorite_contact_phone = contact["phone"]
      favorite_contact_email = contact["email"]
      favorite_contact_mark = contact["favorite"]
      favorite_contact = {"name": favorite_contact_name, "phone": favorite_contact_phone, "email": favorite_contact_email, "favorite": favorite_contact_mark}
      favorite_list_contact.append(favorite_contact)
  if (len(favorite_list_contact) == 0):
    print("Favorite contact list is empty! \n")
  else:
    print("\nThis is yours favorites contacts: ")
    print("\n   Name      |    Phone    |   Email   |   Favorite   \n")
    for index, contact in enumerate(favorite_list_contact, start=1):
      print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['favorite']}") 
  return 

def delete_a_contact(contact_list, index_to_delete):
  index_verified_to_delete = int(index_to_delete) - 1
  if(index_verified_to_delete >= 0 and index_verified_to_delete < len(contact_list)):
    for index, contact in enumerate(contact_list):
      if index == index_verified_to_delete:
        contact_list.remove(contact)
        print(f"You removed the contact name: {contact['name']}")
  else:
    print("You don't have this elemento in your list! \n")


contact_list = []

while True:
  print("\nContact List")
  print("1. Add a contact")
  print("2. See contacts list")
  print("3. Update a contact")
  print("4. Modified a contact as favorite")
  print("5. Show your favorite contact list")
  print("6. Delete a contact")
  print("7. Exit()")

  choice = input("Type the number of your choice: ")
  print("\n")

  if choice == "1":
    contact_name = input("Type contact name to add a list. \n")
    contact_phone = input("Type contact phone to add a list. \n")
    contact_email = input("Type contact email to add a list. \n")
    contact_favorite = input("It's a favorite contact? (y) or (n) \n")
    add_a_contact(contact_list, contact_name, contact_phone, contact_email, contact_favorite)
  elif choice == "2":
    if (len(contact_list) == 0):
      print("List Contact is empty \n")
    else:
      list_contacts(contact_list)
  elif choice == "3":
    if (len(contact_list) == 0):
      print("List Contact is empty \n")
    else:
      list_contacts(contact_list)
      contact_index = input("Type index of a contact that you want to update: ")
      update_contact(contact_list, contact_index)
      list_contacts(contact_list)
  elif choice == "4":
    list_contacts(contact_list)
    index_to_favorite = input("Type the index from the contact that you want to turn on your favorite: ")
    update_favorite(contact_list, index_to_favorite)
  elif choice == "5":
    if (len(contact_list) == 0):
      print("List Contact is empty \n")
    else:
      list_favorites_contact(contact_list)
  elif choice == "6":
    if (len(contact_list) == 0):
      print("List Contact is empty \n")
    else:
      list_contacts(contact_list)
      index_to_delete = input("Type the index from the contact that you want to delete: ")
      delete_a_contact(contact_list, index_to_delete)
  elif choice == "7":
    break

print("See you soon! \n")