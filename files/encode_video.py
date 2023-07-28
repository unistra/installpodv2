from django.conf import settings

from django.utils import translation
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from pod.video.models import Video
from pod.video.encode import start_remote_encode

LANGUAGE_CODE = getattr(settings, "LANGUAGE_CODE", "fr")


class Command(BaseCommand):
    # args = 'video_id'
    help = "encode video into Pod"

    def add_arguments(self, parser):
        parser.add_argument(
            "video_id",
            type=int,
            help="Indicates the id of the video to encode",
        )

    def handle(self, *args, **options):
        # Activate a fixed locale fr
        translation.activate(LANGUAGE_CODE)
        video_id = options["video_id"]
        try:
            video = Video.objects.get(id=video_id)
            start_remote_encode(video_id)
            self.stdout.write(
                self.style.SUCCESS('Successfully  encoded video "%s"' % (video))
            )
        except ObjectDoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    "******* Video id matching query does not exist: %s *******"
                    % video_id
                )
            )

