import pyramid_handlers

from band.controllers.base_controller import BaseController
from band.services.albums_service import AlbumsService


class AlbumsController(BaseController):
    @pyramid_handlers.action(renderer='templates/albums/index.pt')
    def index(self):
        # data / service access
        all_albums = AlbumsService.get_albums()
        user = self.logged_in_user

        # return the model
        return {'albums': all_albums}
