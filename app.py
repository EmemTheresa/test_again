import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

# Initialize the main window
root = tk.Tk()
root.title("Leuphana Community App")
screen_width, screen_height = 414, 896  # Dimensions from the image
root.geometry(f"{screen_width}x{screen_height}")

# define global font
formal_font = ("Arial", 16)
formal_font_bold = ("Arial", 16, "bold")
heading_font = ("Arial", 18, "bold")
event_font = ("Arial", 16, "italic")

# Define colors
background_color = "#f2f0f0"
accent_color = "#8B0000"
text_color = "#4B4B4B"
button_bg_color = "#ffffff"  # Button background color
button_active_bg_color = "#d3d3d3"  # Button active background color

# Set background color for the root window
root.configure(bg=background_color)


# Function to clear all widgets from a given frame
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Function to add an image to a given frame
def add_image(frame, file_path, width, height):
    abs_path = os.path.join(os.path.dirname(__file__), file_path)
    img = Image.open(abs_path).resize((width, height), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=img)
    label.image = img
    label.pack()


# Function to open a URL in the web browser
def open_url(url):
    webbrowser.open(url)


# Functions to open specific URLs
def visit_library():
    open_url("https://www.leuphana.de/services/miz/literaturrecherche/digitale-bibliothek.html")


def visit_student_services():
    open_url("https://www.leuphana.de/en/services/student-service.html")


def visit_counselor():
    open_url("https://stw-on.de/en/lüneburg/counselling/psychotherapeutic-counselling-centre-2-2")


def book_appointment():
    open_url("https://www.doctolib.de/")


def visit_sports_page():
    open_url("https://www.leuphana.de/services/hochschulsport.html")


def join_flohmarkt_group():
    open_url("https://t.me/joinchat/VWR-V8VWp2_GOs1F")


def join_sharing_is_caring():
    open_url("https://kurzelinks.de/gc8u")


def join_international_group():
    open_url("https://t.me/leuphana_internationals")


def join_digital_media_students():
    open_url("https://chat.whatsapp.com/EP3Svyshxp956ZU7yJ6qnv")


# create the home page
def create_welcome_page():
    clear_widgets(root)
    add_image(root, "images/homepage.jpg", screen_width, screen_height)

    find_people_button = tk.Button(root, text="JOIN US!", font=formal_font_bold, bg=button_bg_color,
                                   activebackground=button_active_bg_color, fg=accent_color, bd=0,
                                   command=create_main_features_page)
    find_people_button.place(relx=0.5, y=600, anchor=tk.CENTER)


# create the home page
def create_main_features_page():
    clear_widgets(root)

    # Load and display background image
    background_img = Image.open("images/features_background.jpg")
    background_img = ImageTk.PhotoImage(background_img)
    background_label = tk.Label(root, image=background_img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_label = tk.Label(root, text="LEUPHANA", font=heading_font, fg=accent_color, bg=background_color)
    title_label.pack(pady=(50, 0))

    subtitle_label = tk.Label(root, text="COMMUNITY APP", font=heading_font, fg=accent_color, bg=background_color)
    subtitle_label.pack(pady=(0, 50))

    # Define feature buttons with their respective labels and commands
    feature_buttons = [
        ("Information Hub", create_info_hub),
        ("Community Forum", create_community_forum),
        ("Health Resources", create_wellbeing_page),
        ("Community Engagement Initiatives", create_community_connections_page)
    ]

    # Create buttons for each feature with appropriate formatting
    for feature, command in feature_buttons:
        feature_button = tk.Button(root, text=feature, font=(formal_font_bold if feature == "Events" else formal_font),
                                   fg=(accent_color if feature == "Events" else text_color), bg=button_bg_color,
                                   activebackground=button_active_bg_color, bd=0, command=command)
        feature_button.pack(pady=10)


# create the info hub page
def create_info_hub():
    clear_widgets(root)
    add_image(root, "images/info_hub.jpg", screen_width, screen_height)
    tk.Label(root, text="Information Hub", font=formal_font_bold, bg=background_color).place(relx=0.5, y=100,
                                                                                             anchor=tk.CENTER)

    info_text = """Welcome to the Information Hub!"""
    tk.Label(root, text=info_text, font=formal_font, wraplength=screen_width - 40, bg=background_color).place(relx=0.5,
                                                                                                              y=200,
                                                                                                              anchor=tk.CENTER)

    # Buttons to navigate to specific resources
    tk.Button(root, text="Visit Library", command=visit_library, font=formal_font, bg=button_bg_color,
              activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=300, anchor=tk.CENTER)
    tk.Button(root, text="Student Services", command=visit_student_services, font=formal_font, bg=button_bg_color,
              activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=350, anchor=tk.CENTER)

    # Button to return to main features page
    tk.Button(root, text="Back to Features", command=create_main_features_page, font=formal_font_bold,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=400,
                                                                                                      anchor=tk.CENTER)


# create the community forum page
def create_community_forum():
    clear_widgets(root)
    add_image(root, "images/community_forum.jpg", screen_width, screen_height)
    tk.Label(root, text="Community Forum", font=formal_font_bold, bg=background_color).place(relx=0.5, y=100,
                                                                                             anchor=tk.CENTER)

    forum_text = """Welcome to the Community Forum!
    Share your thoughts, ask questions, and connect with other students."""
    tk.Label(root, text=forum_text, font=formal_font, wraplength=screen_width - 40, bg=background_color).place(relx=0.5,
                                                                                                               y=200,
                                                                                                               anchor=tk.CENTER)

    # create the Chatbot Interface
    global text_box, entry_box

    text_box = tk.Text(root, bg="#17202A", fg="#EAECEE", font="Helvetica 14", width=60)
    text_box.place(x=0, y=250, relwidth=1, relheight=0.4)

    scroll_bar = tk.Scrollbar(text_box)
    scroll_bar.place(relheight=1, relx=0.974)

    entry_box = tk.Entry(root, bg="#2C3E50", fg="#EAECEE", font="Helvetica 14", width=55)
    entry_box.place(x=5, rely=0.7, relwidth=0.7, relheight=0.05)

    send_button = tk.Button(root, text="Send", font="Helvetica 13 bold", bg="#ABB2B9", command=send_message, width=10)
    send_button.place(relx=0.77, rely=0.7, relwidth=0.2, relheight=0.05)

    # create a button to return to main features page
    tk.Button(root, text="Back to Features", command=create_main_features_page, font=formal_font_bold,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=700,
                                                                                                      anchor=tk.CENTER)


# create the wellbeing page
def create_wellbeing_page():
    clear_widgets(root)
    add_image(root, "images/wellbeing.jpg", screen_width, screen_height)
    tk.Label(root, text="Well-being Resources", font=formal_font_bold, bg=background_color).place(relx=0.5, y=100,
                                                                                                  anchor=tk.CENTER)

    wellbeing_text = """Well-being Tips:
    - Tip 1: Stay active and exercise regularly.
    - Tip 2: Maintain a balanced diet.
    - Tip 3: Get enough sleep and rest.
    - Tip 4: Take breaks and manage stress effectively."""
    tk.Label(root, text=wellbeing_text, font=formal_font, wraplength=screen_width - 40, bg=background_color).place(
        relx=0.5, y=200, anchor=tk.CENTER)

    # Buttons to access wellbeing resources
    tk.Button(root, text="Contact Counselor", command=visit_counselor, font=formal_font, bg=button_bg_color,
              activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=300, anchor=tk.CENTER)
    tk.Button(root, text="Book Appointment", command=book_appointment, font=formal_font, bg=button_bg_color,
              activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=350, anchor=tk.CENTER)
    tk.Button(root, text="Visit University Sports Page", command=visit_sports_page, font=formal_font,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=400,
                                                                                                      anchor=tk.CENTER)

    # Button to return to main features page
    tk.Button(root, text="Back to Features", command=create_main_features_page, font=formal_font_bold,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=450,
                                                                                                      anchor=tk.CENTER)


# create the community connections page
def create_community_connections_page():
    clear_widgets(root)
    tk.Label(root, text="Community Connections", font=formal_font_bold, bg=background_color).pack(pady=50)

    # Buttons to join various community groups
    tk.Button(root, text="Join Flohmarkt Group", command=join_flohmarkt_group, font=formal_font, bg=button_bg_color,
              activebackground=button_active_bg_color, fg=text_color, bd=0).pack(pady=10)

    tk.Button(root, text="Join Sharing is Caring", command=join_sharing_is_caring, font=formal_font,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).pack(pady=10)

    tk.Button(root, text="Join International Group", command=join_international_group, font=formal_font,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).pack(pady=10)

    tk.Button(root, text="Join Digital Media Students", command=join_digital_media_students, font=formal_font,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).pack(pady=10)

    # Button to return to main features page
    tk.Button(root, text="Back to Features", command=create_main_features_page, font=formal_font_bold,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).pack(pady=20)


def send_message():
    message = entry_box.get()
    if message:
        text_box.config(state=tk.NORMAL)
        text_box.insert(tk.END, "You: " + message + "\n")
        text_box.config(state=tk.DISABLED)
        entry_box.delete(0, tk.END)

        response = get_bot_response(message)
        text_box.config(state=tk.NORMAL)
        text_box.insert(tk.END, "Bot: " + response + "\n")
        text_box.config(state=tk.DISABLED)
        text_box.see(tk.END)


def get_bot_response(message):
    responses = {
        "hello": "Hello! Welcome to the Leuphana Community Forum",
        "hi": "Hi there! Welcome to the Leuphana Community Forum",
        "help": "Sure, I'm here to help. What do you need assistance with?",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(message.lower(), "I'm sorry, I don't understand that.")


# Call the welcome page to start the app
create_welcome_page()

# Run the main event loop
root.mainloop()
