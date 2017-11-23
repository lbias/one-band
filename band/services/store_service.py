from band.data.account import Account
from band.data.album import Album
from band.data.dbsession import DbSessionFactory
from band.data.purchase import AlbumPurchase
from band.infrastructure.credit_card_processor import CreditCardProcessor


class StoreService:
    @staticmethod
    def purchase_album(user: Account, album: Album,
                       amount_paid_usd: float, stripe_token: str):
        desc = "Purchase album: " + album.name

        charge = CreditCardProcessor.complete_stripe_purchase(stripe_token,
                                                              desc, amount_paid_usd)
        print(charge)
        StoreService.__record_purchase(user.id, album.id, amount_paid_usd, desc)

    @staticmethod
    def __record_purchase(user_id: int, album_id: int,
                          amount_paid_usd: float, description: str):
        session = DbSessionFactory.create_session()

        purchase = AlbumPurchase()
        purchase.amount_paid = amount_paid_usd
        purchase.user_id = user_id
        purchase.album_id = album_id
        purchase.description = description

        session.add(purchase)
        session.commit()

    @staticmethod
    def get_purchased_album_ids(user_id: int):
        session = DbSessionFactory.create_session()
        # TODO: ...
