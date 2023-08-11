from django.utils.timezone import localtime
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    this_not_leaved_visits = Visit.objects.filter(leaved_at=None)
    for visit in this_not_leaved_visits:
        user = visit.passcard.owner_name
        entered_at = localtime(visit.entered_at)
        duration = visit.format_duration(visit.get_duration(entered_at))
        non_closed_visits = [
            {
                'who_entered': user,
                'entered_at': entered_at,
                'duration': duration,
            }
        ]
        context = {
            'non_closed_visits': non_closed_visits,
        }
        return render(request, 'storage_information.html', context)
