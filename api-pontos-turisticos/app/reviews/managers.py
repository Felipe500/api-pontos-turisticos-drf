from django.db.models import F

from app.common.models import SoftDeletionManager

from app.touristic_points.models import TouristicPoint


class ReviewsManager(SoftDeletionManager):
    @staticmethod
    def create_review(tourist_spot_id: int, current_note: float):
        TouristicPoint.objects.filter(id=tourist_spot_id).update(**{
            'users_reviews': F('users_reviews') + 1,
            'total_review': F('total_review') + current_note
        })
        return True

    @staticmethod
    def update_review(tourist_spot_id: int, new_note: float, last_note: float):
        print('tourist_spot_id ', tourist_spot_id)
        TouristicPoint.objects.filter(id=tourist_spot_id).update(**{
            'total_review': F('total_review') - last_note + new_note
        })
        return True

    @staticmethod
    def delete_review(tourist_spot_id: int, current_note: float):
        TouristicPoint.objects.filter(id=tourist_spot_id).update(**{
            'users_reviews': F('users_reviews') - 1,
            'total_review': F('total_review') - current_note
        })
        return True
