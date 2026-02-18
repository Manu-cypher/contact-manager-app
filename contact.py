import flet as ft
import json
import os

# --- DATA HANDLING ---
CONTACTS_FILE = "contacts.json"

def load_data():
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_data(contacts_list):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts_list, f, indent=4)

def main(page: ft.Page):
    # 1. Page Configuration
    page.title = "Contact Manager"
    page.theme_mode = ft.ThemeMode.LIGHT 
    page.window_width = 400
    page.window_height = 700
    page.padding = 20

    # Load existing contacts
    my_contacts = load_data()

    # 2. UI Elements
    
    # We use STRING names for icons (e.g., "person") to avoid version errors
    txt_name = ft.TextField(label="Name", prefix_icon="person")
    txt_phone = ft.TextField(label="Phone", prefix_icon="phone", keyboard_type=ft.KeyboardType.PHONE)
    
    # The List Container
    contacts_view = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    # 3. Functions
    def delete_contact(e, contact_data):
        if contact_data in my_contacts:
            my_contacts.remove(contact_data)
            save_data(my_contacts)
            refresh_list()
            page.update()

    def refresh_list():
        contacts_view.controls.clear()
        
        for contact in my_contacts:
            # Create a Card for each contact
            card = ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(name="account_circle", size=40, color=ft.colors.BLUE),
                                    ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Text(contact['name'], size=16, weight=ft.FontWeight.BOLD),
                                            ft.Text(contact['phone'], size=12, color=ft.colors.GREY),
                                        ]
                                    ),
                                ]
                            ),
                            # Delete Button
                            ft.IconButton(
                                icon="delete_outline", 
                                icon_color=ft.colors.RED,
                                # We use a lambda to pass the specific contact data
                                on_click=lambda e, c=contact: delete_contact(e, c)
                            )
                        ]
                    )
                )
            )
            contacts_view.controls.append(card)
        page.update()

    def add_click(e):
        if not txt_name.value or not txt_phone.value:
            txt_name.error_text = "Required" if not txt_name.value else None
            txt_phone.error_text = "Required" if not txt_phone.value else None
            page.update()
            return

        new_contact = {"name": txt_name.value, "phone": txt_phone.value}
        my_contacts.append(new_contact)
        save_data(my_contacts)
        refresh_list()
        
        # Reset fields
        txt_name.value = ""
        txt_phone.value = ""
        txt_name.error_text = None
        txt_phone.error_text = None
        txt_name.focus()
        page.update()

    # 4. Button (Works perfectly in Flet 0.25.0)
    add_button = ft.ElevatedButton(
        text="Add Contact", 
        icon="add", 
        bgcolor=ft.colors.BLUE, 
        color=ft.colors.WHITE,
        width=400,
        on_click=add_click
    )

    # 5. Layout Assembly
    page.add(
        ft.Text("My Contacts", size=24, weight=ft.FontWeight.BOLD),
        
        ft.Container(
            padding=10,
            bgcolor=ft.colors.BLUE_GREY_50,
            border_radius=10,
            content=ft.Column([
                txt_name,
                txt_phone,
                add_button
            ])
        ),
        
        ft.Divider(),
        
        ft.Container(
            expand=True,
            content=contacts_view
        )
    )

    refresh_list()

# Start the app
ft.app(target=main)