#!/usr/bin/python

# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from filer.models.imagemodels import Image


class Command(BaseCommand):
    help = "List all images in Filer module"

    def handle(self, *args, **options):
        try:
            for image in Image.objects.all():
                self.stdout.write(f"----------------------")
                self.stdout.write(
                    f"{image} - {image.width}x{image.height} - {image.mime_type} - {image.file}"
                )

                if image.exif:
                    self.stdout.write(f"{image.exif}")

        except Exception as err:
            self.stdout.write(f"[+] ERROR: {err}!!!")
            raise CommandError(f"Program INFO:[{err}]")
