import copy
from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required

from notification.models import Notification

@login_required
def tweet_notification(request):
    # Assistance from Peter
    current_user = request.user
    notif = Notification.objects.filter(target_user=current_user)
    notif_copy = copy.deepcopy(list(notif))
    for n in notif:
        n.message_visibility = False
        n.save()
    return render(request, "notification.html", {"notifications": notif_copy})