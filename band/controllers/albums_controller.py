import pyramid_handlers

from band.controllers.base_controller import BaseController
from band.infrastructure.credit_card_processor import CreditCardProcessor
from band.services.albums_service import AlbumsService


class AlbumsController(BaseController):
    @pyramid_handlers.action(renderer='templates/albums/index.pt')
    def index(self):
        # data / service  access
        all_albums = AlbumsService.get_albums()

        # return the model
        return {
            'albums': all_albums,
            'stripe_pub_key': CreditCardProcessor.stripe_public_key
        }
