from django.utils.timezone import localtime
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visit = Visit()
    storehouse = Visit.objects.filter(leaved_at=None)
    for one_visit in storehouse:
        user = one_visit.passcard.owner_name
        entered_at = localtime(one_visit.entered_at)
        duration = visit.format_duration(visit.get_duration(entered_at))
        non_closed_visits = [
            {
                'who_entered': user,
                'entered_at': entered_at,
                'duration': f'{duration["hours"]:02d}:{duration["minutes"]:02d}:{duration["seconds"]:02d}',
            }
        ]
        context = {
            'non_closed_visits': non_closed_visits,
        }
        return render(request, 'storage_information.html', context)
