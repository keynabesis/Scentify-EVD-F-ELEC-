from pyscript import document
from js import window
from pyodide.ffi import create_proxy

_proxies = []


def keep_proxy(function):
    """Keep Python callbacks alive for browser events."""
    proxy = create_proxy(function)
    _proxies.append(proxy)
    return proxy

menu_button = document.querySelector(
    ".menu-toggle, #menu-toggle, #menu-btn"
)

nav_menu = document.querySelector(
    ".nav-links, #nav-links, .nav-menu"
)


def toggle_menu(event):
    if nav_menu:
        nav_menu.classList.toggle("active")

        is_expanded = nav_menu.classList.contains("active")
        menu_button.setAttribute(
            "aria-expanded",
            str(is_expanded).lower()
        )


if menu_button and nav_menu:
    menu_button.addEventListener(
        "click",
        keep_proxy(toggle_menu)
    )

current_path = window.location.pathname.lower()
current_page = current_path.split("/")[-1]

if not current_page:
    current_page = "index.html"


nav_links = document.querySelectorAll(
    "nav a, .nav-links a, .navbar a"
)


for link in nav_links:
    href = link.getAttribute("href")

    if href:
        link_page = href.split("/")[-1].split("?")[0].lower()

        if link_page == current_page:
            link.classList.add("active")
        else:
            link.classList.remove("active")

perfume_video = document.getElementById("perfume-ad")

if perfume_video:
    perfume_video.autoplay = False

contact_form = document.querySelector(
    "#contact-form, .contact-form, form[data-contact-form]"
)
if contact_form:

    def submit_contact_form(event):
        event.preventDefault()

        name_field = contact_form.querySelector(
            '[name="name"], #name'
        )

        email_field = contact_form.querySelector(
            '[name="email"], #email'
        )

        message_field = contact_form.querySelector(
            '[name="message"], #message'
        )

        if not name_field or not email_field or not message_field:
            window.alert(
                "Please check the contact form fields."
            )
            return

        name = name_field.value.strip()
        email = email_field.value.strip()
        message = message_field.value.strip()

        if not name or not email or not message:
            window.alert(
                "Please fill in all required fields."
            )
            return

        if "@" not in email or "." not in email.split("@")[-1]:
            window.alert(
                "Please enter a valid email address."
            )
            return

        window.alert(
            f"Thank you, {name}! Your demo inquiry has been received."
        )

        contact_form.reset()


    contact_form.addEventListener(
        "submit",
        keep_proxy(submit_contact_form)
    )

images = document.querySelectorAll("img")


def handle_image_error(event):
    image_element = event.target

    # Hide an image if its file cannot be loaded.
    image_element.style.display = "none"


for image_element in images:
    image_element.addEventListener(
        "error",
        keep_proxy(handle_image_error)
    )
