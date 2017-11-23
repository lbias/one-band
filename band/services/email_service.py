class EmailService:
    __smtp_username = None
    __smtp_password = None
    __smtp_server = None
    __smtp_port = None
    __is_debug_mode = False
    __from_address = 'Talk Python Demo <demo@talkpython.fm>'

    @staticmethod
    def global_init(username, password, server, port, is_debug):
        EmailService.__is_debug_mode = is_debug
        EmailService.__smtp_username = username
        EmailService.__smtp_password = password
        EmailService.__smtp_port = int(port)
        EmailService.__smtp_server = server
