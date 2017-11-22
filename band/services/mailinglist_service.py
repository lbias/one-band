import mailchimp


class MailingListService:
    mailchimp_api = None
    mailchimp_list_id = None

    @staticmethod
    def global_init(api_key, list_id):
        MailingListService.mailchimp_api = api_key
        MailingListService.mailchimp_list_id = list_id

    @staticmethod
    def add_subscriber(email):
        pass
