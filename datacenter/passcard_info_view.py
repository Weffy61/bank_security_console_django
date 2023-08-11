from django.utils.timezone import localtime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits_serialized = []

    for visit in this_passcard_visits:
        if visit.leaved_at:
            duration_in_sec = visit.get_duration(visit.entered_at, visit.leaved_at)
            duration = visit.format_duration(seconds=duration_in_sec)
            this_passcard_visits_serialized.append({
                'entered_at': localtime(visit.entered_at),
                'duration': duration,
                'is_strange': visit.is_visit_long(visit.get_duration(visit.entered_at, visit.leaved_at))
            })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_serialized
    }
    return render(request, 'passcard_info.html', context)


