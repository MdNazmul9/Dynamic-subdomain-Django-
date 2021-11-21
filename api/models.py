from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
import os
class Institute(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255)
    controller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='controller')

    class Meta:
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        super(Institute, self).save(*args, **kwargs)
        with open('/etc/hosts', 'rt') as f:
            # newdomain = self.subdomain+settings.ALLOWED_HOSTS[2]
            newdomain = self.subdomain+'.example.com'
            # print(newdomain)
            # settings.ALLOWED_HOSTS.append(newdomain)
            s = f.read() + '\n' + '127.0.0.1\t%s'%newdomain
            with open('/tmp/etc_hosts.tmp', 'wt') as outf:
                outf.write(s)

        os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')
    def __str__(self):
        return str(self.subdomain)

        
class InstituteAware(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    

class Member(InstituteAware):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='creator')

    def __str__(self):
        return str(self.name)

