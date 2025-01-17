from login_window import LoginWindow


class MainController:
    def __init__(self, window, connector):
        self.window = window
        self.connector = connector
        self.login_window = None
        self.bind()

    def bind(self):
        self.window.connection_action.triggered.connect(self.show_login_window)

    def show_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.submitClicked.connect(self.on_login_window_confirm)
        self.login_window.show()

    def on_login_window_confirm(self, username):
        self.window.text_editor.setText(f"Your name is: {username}")