#!/usr/bin/python

# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from filer.models.imagemodels import Image

from filer_optimizer.utils import store_as_webp


class Command(BaseCommand):
    help = "List all images in Filer module"

    def handle(self, *args, **options):
        try:
            for image in Image.objects.all():
                self.stdout.write("----------------------")
                self.stdout.write(
                    f"{image} - {image.width}x{image.height} - {image.mime_type} - {image.file}"
                )
                try:
                    store_as_webp(image)
                except Exception as err:
                    self.stdout.write(f"[+] ERROR-WEBP: {err}!!!")
        except Exception as err:
            self.stdout.write(f"[+] ERROR: {err}!!!")
            raise CommandError(f"Program INFO:[{err}]")
