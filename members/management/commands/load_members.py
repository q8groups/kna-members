from optparse import make_option
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand, CommandError, NoArgsCommand
from members.models import member,ministers
class Command(NoArgsCommand):
    help = 'Help text goes here'

    def traverse(self):
        member.objects.all().delete()
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".jpg"):
                    f = open(os.path.join(root, file),"r")
                    name =  os.path.join(root, file).split("/")[-1].split(".")[0]
                    m = member()
                    m.name = name
                    suf = SimpleUploadedFile(str(self.counter)+".jpg",f.read(), content_type='image/jpeg')
                    m.photo.save(str(self.counter)+".jpg", suf, save=False)
                    m.save()
                    self.counter=self.counter+1

    def traverse2(self):
        ministers.objects.all().delete()
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".jpg"):
                    f = open(os.path.join(root, file),"r")
                    name =  os.path.join(root, file).split("/")[-1].split(".")[0]
                    m = ministers()
                    m.name = name
                    suf = SimpleUploadedFile(str(self.counter)+".jpg",f.read(), content_type='image/jpeg')
                    m.photo.save(str(self.counter)+".jpg", suf, save=False)
                    m.save()
                    self.counter=self.counter+1


    def handle(self, **options):
         print "This is a command"
         self.path = "/Users/q80/Pictures/committee/"
         self.counter = 0
         self.traverse()
         self.path = "/Users/q80/Pictures/ministres/"
         self.counter = 0
         self.traverse2()