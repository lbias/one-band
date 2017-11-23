import os

from pyramid.config import Configurator

import band
import band.controllers.home_controller as home
import band.controllers.albums_controller as albums
import band.controllers.account_controller as account
from band.data.dbsession import DbSessionFactory
from band.email.template_paser import EmailTemplateParser
from band.infrastructure.credit_card_processor import CreditCardProcessor
from band.services.email_service import EmailService
from band.services.mailinglist_service import MailingListService

dev_mode = False


def main(_, **settings):
    config = Configurator(settings=settings)

    init_mode(config)
    init_includes(config)
    init_routing(config)
    init_db(config)
    init_mailing_list(config)
    init_smtp_mail(config)
    init_email_templates(config)

    return config.make_wsgi_app()


def init_email_templates(_):
    EmailTemplateParser.global_init()


def init_smtp_mail(config):
    global dev_mode
    unset = 'YOUR_VALUE'

    settings = config.get_settings()
    smtp_username = settings.get('smtp_username')
    smtp_password = settings.get('smtp_password')
    smtp_server = settings.get('smtp_server')
    smtp_port = settings.get('smtp_port')

    local_dev_mode = dev_mode

    if smtp_username == unset:
        print("WARNING: SMTP server values not set in config file. "
              "Outbound email will not work.")
        local_dev_mode = True  # turn off email if the system has no server.

    EmailService.global_init(smtp_username, smtp_password, smtp_server, smtp_port, local_dev_mode)


def init_db(_):
    top_folder = os.path.dirname(blue_yellow_app.__file__)
    rel_folder = os.path.join('db', 'band.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
    DbSessionFactory.global_init(db_file)


def init_mode(config):
    global dev_mode
    settings = config.get_settings()
    dev_mode = settings.get('mode') == 'dev'
    print('Running in {} mode.'.format('dev' if dev_mode else 'prod'))


def init_mailing_list(config):
    unset = 'THE_API_KEY'

    settings = config.get_settings()
    mailchimp_api = settings.get('mailchimp_api')
    mailchimp_list_id = settings.get('mailchimp_list_id')

    if mailchimp_api == unset:
        print("WARNING: Mailchimp API values not set in config file. "
              "Mailing list subscriptions will not work.")

    MailingListService.global_init(mailchimp_api, mailchimp_list_id)


def init_credit_cards(config):
    unset = 'ADD_YOUR_API_KEY'

    settings = config.get_settings()
    stripe_private_key = settings.get('stripe_private_key')
    stripe_public_key = settings.get('stripe_public_key')

    if stripe_public_key == unset:
        print("WARNING: Stripe API values not set in config file. "
              "Credit card purchases will not work.")

    CreditCardProcessor.global_init(stripe_private_key, stripe_public_key)


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_handler('root', '/', handler=home.HomeController, action='index')

    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, albums.AlbumsController, 'albums')
    add_controller_routes(config, account.AccountController, 'account')

    config.scan()


def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{id}', handler=ctrl)


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
